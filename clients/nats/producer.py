#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
from nats.io import Client
import tornado.gen
import tornado.ioloop

TOPIC = "t"
NATS_HOST = "127.0.0.1"
NATS_PORT = 4222
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

size = 0

@tornado.gen.coroutine
def test():
    client = Client()
    options = {"servers": ["nats://%s:%d" % (NATS_HOST, NATS_PORT)]}
    yield client.connect(**options)
    msg = "0" * size
    for i in range(0, COUNT):
        yield client.publish(TOPIC, msg)
    yield client.publish(TOPIC, "quit")
    yield client.flush()

if __name__ == "__main__":
    for s in range(*MSGSIZE):
        size = s
        print("message size: %d" % size)
        result = timeit.timeit("tornado.ioloop.IOLoop.instance().run_sync(test)",
                               setup="from __main__ import test;import tornado.ioloop",
                               number=1)
        print("processing time: %f" % result)

