import json
from confluent_kafka import Producer

def produce_inventory_order():
    # Kafka producer configuration
    kafka_config = {'bootstrap.servers': 'localhost:9092'}

    # Create Kafka producer
    producer = Producer(kafka_config)

    # Simulate inventory events data
    inventory_events = [
        {"type": "inventory", "item_id": "123", "quantity": 10},
        {"type": "inventory", "item_id": "456", "quantity": 20}
    ]

    # Send inventory events to Kafka topic
    for event in inventory_events:
        producer.produce('inventory_orders', json.dumps(event).encode('utf-8'))

    # Flush producer to send messages
    producer.flush()

produce_inventory_order()
