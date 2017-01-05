# coding:utf-8

from kafka.client import KafkaClient
from kafka.producer import KafkaProducer
from kafka.consumer import KafkaConsumer
from kafka.common import TopicPartition, ConsumerTimeout
import threading, time, uuid, logging

from utils import HeapQueue, LineParser, TSFrame


class KafkaWorker(threading.Thread):
    stop_consumer = False
    interval = 5

    def __init__(self, is_X, brokers, group, topic, start_offset, ts_frame, id=None):

        """
        :param is_X:            - for specify topic type in data manager
        :param brokers:         - Kafka location
        :param group:           - Kafka consumer group
        :param topic:           - Kafka topic
        :param start_offset:    - first time offset consume from the topic
        :param id:              - Kafka client id

        """

        super(KafkaWorker, self).__init__(daemon=True)

        self._is_X = is_X
        self._ts_frame = ts_frame

        self._kafka_brokers = brokers
        self._kafka_group = group
        self._kafka_topic = topic
        self._kafka_start_offset = start_offset  # 'smallest'

        self._consumer = self._create_kafka_consumer()

    def _create_kafka_consumer(self):
        consumer = KafkaConsumer(self._kafka_topic,
                                 bootstrap_servers=self._kafka_brokers,
                                 auto_offset_reset=self._kafka_start_offset,
                                 # largest #当zookeeper中没有初始的offset时，或者超出offset上限时的处理方式 。
                                 enable_auto_commit=False,
                                 ## true时，Consumer会在消费消息后将offset同步到zookeeper，这样当Consumer失败后，新的consumer就能从zookeeper获取最新的offset
                                 client_id=str(uuid.uuid1()) if id == None else id,
                                 group_id=self._kafka_group)  # discard old ones

        return consumer

    def run(self):
        while self.stop_consumer == False:
            try:
                for m in self._consumer:
                    stream_str = m.value
                    if self._is_X:
                        self._ts_frame.push_X(stream_str)
                    else:
                        self._ts_frame.push_Y(stream_str)
                        # print(stream_str)

                    self._consumer.commit()

            except ConsumerTimeout:
                logging.info('kafka worker run: ConsumerTimeout. Check new message in the next round...')

    def stop(self):
        self.stop_consumer = True


if __name__ == '__main__':

    brokers = 'localhost:9092'
    x_topic = 'anomaly'
    y_topic = 'nginx'

    ts_frame = TSFrame(capacity=10)

    X_consumer = KafkaWorker(True, brokers, 'autoshift', x_topic, 'largest', ts_frame)
    X_consumer.start()

    Y_consumer = KafkaWorker(False, brokers, 'autoshift', y_topic, 'largest', ts_frame)
    Y_consumer.start()

    while 1:
        print('*****'*10)
        time.sleep(3)
        print(ts_frame.pop())
        print('len of ts_frame: ', ts_frame.len())
        print(ts_frame.nsmallest(2))
        print('len pf ts_frame after nsmallest: ', ts_frame.len())






























