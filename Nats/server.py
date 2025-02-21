# import asyncio
# import websockets
# import json

# async def receive_messages():
#     uri = "ws://localhost:8080"

#     async with websockets.connect(uri) as ws:
#         print("✅ Connected to NATS WebSocket!")

#         # Subscribe to a subject
#         sub_message = {
#             "op": "sub",
#             "subject": "test.subject",
#             "sid": 1
#         }
#         await ws.send(json.dumps(sub_message))
#         print("📩 Subscribed to 'test.subject'")

#         # Listen for messages
#         try:
#             while True:
#                 response = await ws.recv()
#                 print(f"📨 Received: {response}")
#         except websockets.exceptions.ConnectionClosed:
#             print("🔴 Connection closed")

# # Run the receiver client
# asyncio.run(receive_messages())
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
