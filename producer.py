
import json
from confluent_kafka import Producer

def produce_delivery_order():
    # Kafka producer configuration
    kafka_config = {'bootstrap.servers': 'localhost:9092'}

    # Create Kafka producer
    producer = Producer(kafka_config)

    # Simulate delivery events data
    delivery_events = [
        {"type": "delivery", "order_id": "1001", "status": "pending"},
        {"type": "delivery", "order_id": "1002", "status": "shipped"}
    ]

    # Send delivery events to Kafka topic
    for event in delivery_events:
        producer.produce('delivery_orders', json.dumps(event).encode('utf-8'))

    # Flush producer to send messages
    producer.flush()

produce_delivery_order()
