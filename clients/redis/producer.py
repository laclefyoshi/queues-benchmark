#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import redis

TOPIC = "t"
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test(size):
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    msg = "0" * size
    for i in range(0, COUNT):
        client.publish(TOPIC, msg)

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        print("message size: %d" % size)
        result = timeit.timeit("test(%d)" % size,
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

