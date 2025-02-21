
import asyncio
import nats

# NATS Server URL
NATS_URL = "nats://localhost:4222"

# Subject to send messages to
SUBJECT = "test.subject2"

async def send_message():
    try:
        # Connect to NATS server
        nc = await nats.connect(NATS_URL)
        
        # Message to send
        message = "Hello from Python NATS Sender!"
        
        # Publish the message
        await nc.publish(SUBJECT, message.encode("utf-8"))
        
        print(f"📤 Sent message to '{SUBJECT}': {message}")
        
        # Close the NATS connection
        await nc.close()
        
    except nats.aio.errors.NatsError as e:
        print("❌ NATS error:", e)

# Run the sender
if __name__ == '__main__':
    asyncio.run(send_message())
