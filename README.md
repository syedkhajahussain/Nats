#NATS Messaging System with Docker and Python
This project demonstrates how to run a NATS server using Docker and communicate with it using Python.

🚀 Running NATS with Docker
To start the NATS server using Docker, run the following command:

sh

docker run -p 4222:4222 -p 8080:8080 -v /path/to/nats.conf:/etc/nats.conf -ti nats:latest -c /etc/nats.conf
🔹 Explanation of the Command
docker run → Runs a new container.
-p 4222:4222 → Maps NATS server port (4222) to the host.
-p 8080:8080 → Maps NATS monitoring port (8080) to the host.
-v /path/to/nats.conf:/etc/nats.conf → Mounts the NATS configuration file into the container.
-ti nats:latest → Runs the latest NATS server image.
-c /etc/nats.conf → Specifies the configuration file to use.
📥 Installing Dependencies
Ensure you have Python 3.10+ installed. Install required dependencies:


pip install nats-py psycopg2
📡 Running the Subscriber (Receiver)
This script subscribes to a NATS subject and prints received messages.


import asyncio
import nats

NATS_URL = "nats://localhost:4222"
SUBJECT = "my.subject"

async def message_handler(msg):
    print(f"📩 Received on [{msg.subject}]: {msg.data.decode()}")

async def subscribe():
    nc = await nats.connect(NATS_URL)
    await nc.subscribe(SUBJECT, cb=message_handler)
    print(f"✅ Subscribed to subject: {SUBJECT}")

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(subscribe())
Run the subscriber

python subscriber.py
📤 Running the Publisher (Sender)
This script publishes a message to the NATS subject.

python
Copy
Edit
import asyncio
import nats

NATS_URL = "nats://localhost:4222"
SUBJECT = "my.subject"

async def publish_message():
    nc = await nats.connect(NATS_URL)
    
    message = "Hello, this is a test message!"
    await nc.publish(SUBJECT, message.encode())

    print(f"📤 Sent message to '{SUBJECT}': {message}")
    await nc.close()

if __name__ == "__main__":
    asyncio.run(publish_message())
Run the publisher

python publisher.py
✅ Testing
Start the NATS server using the Docker command above.
Run the subscriber (python subscriber.py).
Send a message using the publisher (python publisher.py).
The subscriber should print the received message.
🔍 Monitoring NATS Server
To check the NATS monitoring UI, open:
🔗 http://localhost:8080

📌 Notes
Replace /path/to/nats.conf with the actual path to your NATS configuration file.
Modify nats.conf if needed to customize authentication and logging.
Ensure Docker is running before starting the NATS container.
The NATS subject is dynamically created, so no manual setup is needed.
🚀 Happy Messaging with NATS! 🎯
