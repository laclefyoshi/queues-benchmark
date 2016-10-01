#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import zmq

ZMQ_HOST = "127.0.0.1"
ZMQ_PORT = 5558
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test(size):
    context = zmq.Context()
    client = context.socket(zmq.PUSH)
    client.connect("tcp://%s:%d" % (ZMQ_HOST, ZMQ_PORT))
    msg = bytes("0" * size)
    for i in range(0, COUNT):
        client.send(msg)
    client.close()
    context.destroy()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        print("message size: %d" % size)
        result = timeit.timeit("test(%d)" % size,
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

