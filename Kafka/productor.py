# MetricCollector
from kafka import KafkaProducer
import json

topicName = 'ebay_log'
serverAddr = 'localhost:9092'
producer = KafkaProducer(bootstrap_servers=serverAddr, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
logData = {}
producer.send(topicName, logData)