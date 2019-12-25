# -*- coding: utf-8 -*-

import hashlib
import web


class Handle(object):
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
        map(sha1.update, l)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature", hashcode, signature)
        if hashcode == signature:
            return echostr
        else:
            return"啥也没返回！"


