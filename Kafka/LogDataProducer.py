# MetricCollector
from KafkaInstance.DataProducer import DataProducer
if __name__ == '__main__':
    logDataConsumer = DataProducer(topicName='ebay_log', serverAddr='localhost:9092', groupId='test_log_data_producer')
    logData = {'corr_id': 'ejsQ5ufDFCmyHG6v',
               'url_api': 'sample/login',
               'node_id': 'NSflDxKmr2AR',
               'ri': 'OgXI76Q5z9++',
               'parent_ri': 'NSflDxKmr2AAR'}
    logDataConsumer.PublishData(logData)