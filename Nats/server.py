
import asyncio
import nats

# NATS Server URL
NATS_URL = "nats://localhost:4222"

# List of subjects to subscribe to
SUBJECTS = ["test.*", "chat.messages"]

# Function to handle incoming NATS messages
async def message_handler(msg):
    subject = msg.subject
    message = msg.data.decode("utf-8")  # Decode the message from bytes to string
    print(f"📩 Received message on '{subject}': {message}")

# Main function to subscribe to NATS subjects
async def main():
    try:
        # Connect to NATS server
        nc = await nats.connect(NATS_URL)

        # Subscribe to each subject
        for subject in SUBJECTS:
            await nc.subscribe(subject, cb=message_handler)

        print("✅ Listening for messages...")

        # Keep the event loop running
        while True:
            await asyncio.sleep(1)

    except nats.aio.errors.NatsError as e:
        print("❌ NATS error:", e)
    except KeyboardInterrupt:
        print("\n🔴 Stopping NATS receiver.")

# Run the receiver
if __name__ == '__main__':
    asyncio.run(main())
