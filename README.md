# LogSearch

We have several parts, which will describe as follow.  
*LogDataProducer.py* serve on every server machine.  
*LogDataConsumer.py* serve on Kafka clusters.  

Basically, *producer* on online-servers parses log and publishes which to Kafka clusters, and *consumer* subscribes log data message, and save which to MySql.  

Finally, We use *flask* to provide log-search web api.
