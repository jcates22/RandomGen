from google.cloud import

# Replace with your project ID and topic name
project_id = "terraform-gcp-412301"
topic_name = "topic1"

# Replace with the service attachment endpoint obtained from Private Service Connect configuration
service_attachment_endpoint = "pubsub-endpoint.p.googleapis.com:443"

# Create a Pub/Sub subscriber client using the service attachment endpoint
subscriber = pubsub_v1.SubscriberClient(channel=service_attachment_endpoint)

# Define a callback function to handle received messages
def callback(message):
  print(f"Received message: {message.data.decode('utf-8')}")

# Create a subscription and specify the callback function
subscription_path = subscriber.topic_path(project_id, topic_name)
subscription = subscriber.create_subscription(subscription_path, ack_settings=pubsub_v1.types.PubSubMessage.AckSettings(auto_ack=True))

# Listen for messages on the subscription
future = subscriber.subscribe(subscription, callback)

# Wait for the subscription to be closed
try:
  future.result()
except KeyboardInterrupt:
  future.cancel()
  print("Subscription cancelled.")

# Cleanup (optional, close the subscriber client)
subscriber.close()
