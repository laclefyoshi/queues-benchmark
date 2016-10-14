#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import pika

TOPIC = "t"
RABBITMQ_HOST = "127.0.0.1"
RABBITMQ_PORT = 5672
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

def test(size):
    params = pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT)
    con = pika.BlockingConnection(params)
    chan = con.channel()
    chan.queue_declare(queue=TOPIC)
    msg = "0" * size
    for i in range(0, COUNT):
        chan.basic_publish(exchange="", routing_key=TOPIC, body=msg)
    chan.basic_publish(exchange="", routing_key=TOPIC, body="quit")
    con.close()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        print("message size: %d" % size)
        result = timeit.timeit("test(%d)" % size,
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

