#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import nnpy

NANO_HOST = "127.0.0.1"
NANO_PORT = 5558
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test(size):
    client = nnpy.Socket(nnpy.AF_SP, nnpy.PUSH)
    client.connect("tcp://%s:%d" % (NANO_HOST, NANO_PORT))
    msg = bytes("0" * size)
    for i in range(0, COUNT):
        client.send(msg)
    client.send("quit")
    client.close()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        print("message size: %d" % size)
        result = timeit.timeit("test(%d)" % size,
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

