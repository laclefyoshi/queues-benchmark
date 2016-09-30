#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import pika

TOPIC = "t"
RABBITMQ_HOST = "127.0.0.1"
RABBITMQ_PORT = 5672
MSGSIZE = (1000, 100000, 1000)  # min, max, step
COUNT = 1000

i = 0

def callback(chan, method, header, body):
    i += 1
    if i >= COUNT:
        chan.close()

def test():
    params = pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT)
    con = pika.BlockingConnection(params)
    chan = con.channel()
    chan.basic_consume(callback, queue=TOPIC, no_ack=True)
    chan.start_consuming()

if __name__ == "__main__":
    for size in range(*MSGSIZE):
        result = timeit.timeit("test()",
                               setup="from __main__ import test",
                               number=1)
        print("processing time: %f" % result)

