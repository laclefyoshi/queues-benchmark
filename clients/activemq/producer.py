#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
from stompest.config import StompConfig
from stompest.sync import Stomp

TOPIC = "/t"
ACTIVEMQ_HOST = "127.0.0.1"
ACTIVEMQ_PORT = 61613
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test(size):
    config = StompConfig("tcp://%s:%d" % (ACTIVEMQ_HOST, ACTIVEMQ_PORT))
    client = Stomp(config)
    client.connect()
    msg = "0" * size
    for i in range(0, COUNT):
        client.send(TOPIC, msg)
    client.send(TOPIC, "quit")
    client.disconnect()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        print("message size: %d" % size)
        result = timeit.timeit("test(%d)" % size,
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

