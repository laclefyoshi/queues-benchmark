#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import nnpy

NANO_HOST = "127.0.0.1"
NANO_PORT = 5557
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test():
    client = nnpy.Socket(nnpy.AF_SP, nnpy.PULL)
    client.connect("tcp://%s:%d" % (NANO_HOST, NANO_PORT))
    for i in range(0, COUNT):
        msg = client.recv()
    client.close()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        result = timeit.timeit("test()",
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

