#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import redis

TOPIC = "t"
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test():
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    subscriber = client.pubsub()
    subscriber.subscribe(TOPIC)
    i = 0
    for msg in subscriber.listen():
        i += 1
        if i >= COUNT:
            break

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        result = timeit.timeit("test()",
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

