#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
from nats.io import Client

TOPIC = "t"
NATS_HOST = "127.0.0.1"
NATS_PORT = 4222
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test(size):
    client = Client()
    options = {"servers": ["nats://%s:%d" % (NATS_HOST, NATS_PORT)]}
    client.connect(**options)
    msg = "0" * size
    for i in range(0, COUNT):
        client.publish(TOPIC, msg)
    client.publish(TOPIC, "quit")
    client.close()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        print("message size: %d" % size)
        result = timeit.timeit("test(%d)" % size,
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

