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
        sha1.update(l[0].encode('utf-8'))
        sha1.update(l[1].encode('utf-8'))
        sha1.update(l[2].encode('utf-8'))
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature", hashcode, signature)
        print("echostr vlaue is :", echostr)
        if hashcode == signature:
            return echostr
        else:
            return"啥也没返回！"


