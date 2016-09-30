#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import zmq
from zmq.eventloop import ioloop, zmqstream

ZMQ_HOST = "127.0.0.1"
ZMQ_HOST_RECEIVER_PORT = 5558
ZMQ_HOST_SENDER_PORT = 5557

class Broker(object):
    def __init__(self):
        self.receiver = None
        self.sender = None
        context = zmq.Context()
        self.receiver = context.socket(zmq.PULL)
        self.receiver.connect("tcp://%s:%d" % (ZMQ_HOST, ZMQ_HOST_RECEIVER_PORT))
        self.sender = context.socket(zmq.PUSH)
        self.sender.connect("tcp://%s:%d" % (ZMQ_HOST, ZMQ_HOST_SENDER_PORT))
    def _send(self, msg):
        self.sender.send(msg[0])
    def start(self):
        stream = zmqstream.ZMQStream(self.receiver)
        stream.on_recv(self._send)

def run():
    ioloop.install()
    broker = Broker()
    broker.start()
    print("start zmq broker...")
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()

