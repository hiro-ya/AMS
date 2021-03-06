#!/usr/bin/env python
# coding: utf-8

import json


class Topic(object):
    def __init__(self):
        self.root = None
        self.id = None
        self.template = {}
        self.all = None
        self.private = None

    def set_root(self, root):
        self.root = root
        self.all = self.root+"/#"
        if self.id is not None:
            self.private = self.root+"/"+self.id

    def set_id(self, _id):
        self.id = str(_id)
        if self.root is not None:
            self.private = self.root+"/"+self.id

    def set_message(self, message):
        self.template = message

    def load(self, path):
        with open(path, "r") as f:
            self.template = json.load(f)

    def get_template(self):
        return self.template

    @staticmethod
    def get_root(topic):
        splitted_topic = topic.split("/")
        return splitted_topic[0]

    @staticmethod
    def get_id(topic):
        splitted_topic = topic.split("/")
        if len(splitted_topic) < 2:
            return None
        return splitted_topic[1]

    @staticmethod
    def serialize(message):
        return json.dumps(message)

    @staticmethod
    def unserialize(payload):
        return json.loads(payload)
