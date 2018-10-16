from KafkaInstance.DataConsumer import DataConsumer
from DBInstance.DBInstance import DBInstance
if __name__ == '__main__':
    logDataConsumer = DataConsumer(topicName='ebay_metric', serverAddr='localhost:9092',
                                   groupId='test_log_data_consumer',
                                   dbInstance=DBInstance("localhost", "wyn", "123456", "ebay_log"))
    logDataConsumer.ReceiveAndSaveToDB()
