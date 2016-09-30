#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
from confluent_kafka import Producer

TOPIC = "t"
KAFKA_HOST = "127.0.0.1"
KAFKA_PORT = 9092
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test(size):
    producer = Producer({"bootstrap.servers": KAFKA_HOST})
    msg = "0" * size
    for i in range(0, COUNT):
        producer.produce(TOPIC, msg)
    producer.flush()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        print("message size: %d" % size)
        result = timeit.timeit("test(%d)" % size,
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

