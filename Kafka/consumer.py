from kafka import KafkaConsumer
from DBInstance.DBInstance import DBInstance

topicName = 'ebay_metric'
serverAddr = 'localhost:9092'

dbInstance = DBInstance()

consumer = KafkaConsumer(topicName)
for logData in consumer:
    # save log to mysql
    dbInstance.SaveToDB(logData)