#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import nsq

TOPIC = "t"
NSQ_HOST = "127.0.0.1"
NSQ_PORT = 4150
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test(size):
    writer = nsq.Writer(["%s:%d" % (NSQ_HOST, NSQ_PORT)])
    msg = "0" * size
    for i in range(0, COUNT):
        writer.pub(TOPIC, msg)
    nsq.run()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        print("message size: %d" % size)
        result = timeit.timeit("test(%d)" % size,
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

