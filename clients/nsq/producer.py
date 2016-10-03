#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import nsq
import tornado
import time
import logging
logging.basicConfig(level=logging.ERROR)

TOPIC = "t"
NSQ_HOST = "127.0.0.1"
NSQ_PORT = 4150
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

size = 0

@tornado.gen.coroutine
def test_go():
    writer = nsq.Writer(["%s:%d" % (NSQ_HOST, NSQ_PORT)])
    yield tornado.gen.sleep(1)
    msg = "0" * size
    for i in range(0, COUNT):
        writer.pub(TOPIC, msg)
    writer.pub(TOPIC, "quit")

def test(s):
    size = s
    tornado.ioloop.IOLoop.instance().run_sync(test_go)

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        print("message size: %d" % size)
        result = timeit.timeit("test(%d)" % size,
                               setup="from __main__ import test;import tornado",
                               number=1)
        print("processing time: %f" % result)

