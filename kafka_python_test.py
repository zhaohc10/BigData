
from kafka.client import SimpleClient
from kafka.consumer import SimpleConsumer
from kafka.consumer import KafkaConsumer
from kafka.common import TopicPartition
from collections import namedtuple


# kafka = SimpleClient("localhost:9092")
# print("After connecting to kafka")
# consumer = SimpleConsumer(kafka, "hashtag-group", "anomaly")
# consumer.seek(0, 0) #to start reading from the beginning of the queue.
# # seek(offset, whence=None, partition=None)[source]
# # Alter the current offset in the consumer, similar to fseek
# #
# # Parameters:
# # offset – how much to modify the offset
# # whence –where to modify it from, default is None
# #     None is an absolute offset
# #     0 is relative to the earliest available offset (head)
# #     1 is relative to the current offset
# #     2 is relative to the latest known offset (tail)
# # partition – modify which partition, default is None. If partition is None, would modify all partitions.

#*****************************************************************************************
# # Consume topic1-all; topic2-partition2; topic3-partition0
# kafka.set_topic_partitions("topic1", ("topic2", 2), {"topic3": 0})
#
# # Consume topic1-0 starting at offset 123, and topic2-1 at offset 456
# # using tuples --
# kafka.set_topic_partitions(("topic1", 0, 123), ("topic2", 1, 456))
#
# # using dict --
# kafka.set_topic_partitions({ ("topic1", 0): 123, ("topic2", 1): 456 })

#*****************************************************************************************

# https://github.com/cuyu/python-demo/blob/master/demo_kafka.py
_TOPIC_NAME = 'anomaly'
_BROKERS = ['localhost:9092'] #['localhost.com:9092', 'systest-auto-deployer:9092']
_GROUP_ID = 'my_group'

consumer = KafkaConsumer(group_id='ddd',
                             auto_offset_reset='smallest', #largest
                             enable_auto_commit=False, ## true时，Consumer会在消费消息后将offset同步到zookeeper，这样当Consumer失败后，新的consumer就能从zookeeper获取最新的offset
                             bootstrap_servers=_BROKERS)
# consumer = KafkaConsumer(bootstrap_servers=_BROKERS)
consumer.assign([TopicPartition(_TOPIC_NAME, 0)])
tp = TopicPartition(_TOPIC_NAME, 0)
print (consumer.committed(TopicPartition(_TOPIC_NAME, 0)))
# consumer.subscribe(topics=[_TOPIC_NAME])
# # Subscribe to a regex topic pattern
# consumer.subscribe(pattern='^awesome.*')
print(consumer.topics())
# partition = TopicPartition(topic=_TOPIC_NAME, partition=consumer.partitions_for_topic(_TOPIC_NAME))
# consumer.seek_to_beginning()
# consumer.seek(TopicPartition(_TOPIC_NAME, 0), 0)
consumer.seek(tp,50) # 10 stands for start consumer from 10th offset
a = []
for m in consumer:
    if len(a) < 5:
        print(m.offset)
        a.append(m.offset)
        # consumer.commit()
    # else:
    #     a =[]

ProduceRequestPayload = namedtuple("ProduceRequestPayload",
    ["topic", "partition", "messages"])

ProduceResponsePayload = namedtuple("ProduceResponsePayload",
    ["topic", "partition", "error", "offset"])




#****************************************************************
#
# consumer1 = KafkaConsumer('anomaly',
#                           group_id='telegraf',
#                           bootstrap_servers=_BROKERS)
# tp = TopicPartition(_TOPIC_NAME, 0)
# consumer1.assign([tp])
# consumer1.seek(tp,0)
# a=[]
# print(len(a))
# for message in consumer1:
#     a.append(message.value)
#     if (len(a) >= 5):
#         print(message.offset)
#         a = []
# #
# # consumer2 = KafkaConsumer('nginx',
# #                           group_id='nginx',
# #                           bootstrap_servers=_BROKERS)
# # print(consumer2.seek(0,2))
