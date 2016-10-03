#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
from stompest.config import StompConfig
from stompest.sync import Stomp
from stompest.protocol import StompSpec

TOPIC = "/t"
ACTIVEMQ_HOST = "127.0.0.1"
ACTIVEMQ_PORT = 61613
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test():
    config = StompConfig("tcp://%s:%d" % (ACTIVEMQ_HOST, ACTIVEMQ_PORT))
    client = Stomp(config)
    client.connect()
    client.subscribe(TOPIC, {StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL})
    while True:
        f = client.receiveFrame()
        client.ack(f)
        if f.body == "quit":
            client.disconnect()
            break

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        print("message size: %d" % size)
        result = timeit.timeit("test()",
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

