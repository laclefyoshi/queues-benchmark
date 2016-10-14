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

def handler(body):
    if body.data == "quit":
        print body
        tornado.ioloop.IOLoop.instance().stop()

@tornado.gen.coroutine
def test():
    client = Client()
    options = {"servers": ["nats://%s:%d" % (NATS_HOST, NATS_PORT)]}
    yield client.connect(**options)
    yield client.subscribe(TOPIC, "", handler)

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        result = timeit.timeit("test();tornado.ioloop.IOLoop.instance().start()",
                               setup="from __main__ import test;import tornado.ioloop",
                               number=1)
        print("processing time: %f" % result)

