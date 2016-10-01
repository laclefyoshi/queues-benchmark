#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import nnpy

NANO_HOST = "127.0.0.1"
NANO_HOST_RECEIVER_PORT = 5558
NANO_HOST_SENDER_PORT = 5557

class Broker(object):
    def __init__(self):
        self.receiver = nnpy.Socket(nnpy.AF_SP, nnpy.PULL)
        self.receiver.bind("tcp://%s:%d" % (NANO_HOST, NANO_HOST_RECEIVER_PORT))
        self.sender = nnpy.Socket(nnpy.AF_SP, nnpy.PUSH)
        self.sender.bind("tcp://%s:%d" % (NANO_HOST, NANO_HOST_SENDER_PORT))
    def _send(self, msg):
        self.sender.send(msg)
    def start(self):
        while True:
            msg = self.receiver.recv()
            _send(msg)

def run():
    broker = Broker()
    print("start nanomsg broker...")
    broker.start()

if __name__ == "__main__":
    run()

