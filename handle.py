# -*- coding: utf-8 -*-

import hashlib
import web
import os
import time
import xml.etree.ElementTree as ET
import talkrob


class Handle(object):
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):

        data = web.input()
        if len(data) == 0:
            return "hello, this is handle view"
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = "zhanglaoguang"

        l = [token, timestamp, nonce]
        l.sort()
        sha1 = hashlib.sha1()
        sha1.update(l[0].encode('utf-8'))
        sha1.update(l[1].encode('utf-8'))
        sha1.update(l[2].encode('utf-8'))
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature", hashcode, signature)
        print("echostr vlaue is :", echostr)
        if hashcode == signature:
            return echostr
        else:
            print("鉴权信息不匹配！")

    def POST(self):
        str_xml = web.data()
        root = ET.fromstring(str_xml)
        msgType = root.find("MsgType").text
        fromUser = root.find("FromUserName").text
        toUser = root.find("ToUserName").text
        if msgType == "text":
            content = talkrob.talk(root.find("Content").text)
            return self.render.reply_text(fromUser, toUser, time.time(), content)


class Test(object):
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        print("app_root的地址是：", self.app_root)
        print("templates_root的地址是：", self.templates_root)
        return self.render.reply_text(1, 2, 3, 4)
