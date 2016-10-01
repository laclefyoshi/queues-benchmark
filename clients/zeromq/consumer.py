#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import zmq

ZMQ_HOST = "127.0.0.1"
ZMQ_PORT = 5557
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test():
    context = zmq.Context()
    client = context.socket(zmq.PULL)
    client.connect("tcp://%s:%d" % (ZMQ_HOST, ZMQ_PORT))
    for i in range(0, COUNT):
        msg = client.recv()
    client.close()
    context.destroy()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        result = timeit.timeit("test()",
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

