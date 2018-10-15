from kafka import KafkaConsumer
from DBWriter.DBWriter import DBWriter

topicName = 'ebay_metric'
serverAddr = 'localhost:9092'

dbWriter = DBWriter()

consumer = KafkaConsumer(topicName)
for logData in consumer:
    # save log to mysql
    dbWriter.save(logData)