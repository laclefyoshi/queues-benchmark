#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
from confluent_kafka import Consumer, KafkaError

TOPIC = "t"
KAFKA_HOST = "127.0.0.1"
KAFKA_PORT = 9092
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test():
    consumer = Consumer({"bootstrap.servers": KAFKA_HOST,
                         "group.id": "g",
                         "default.topic.config": {"auto.offset.reset": "largest"}})
    consumer.subscribe([TOPIC])
    while True:
        msg = consumer.poll()
        if msg == "quit":
            break
        if not msg.error():
            pass
        elif msg.error().code() != KafkaError._PARTITION_EOF:
            break
    consumer.close()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        result = timeit.timeit("test()",
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

