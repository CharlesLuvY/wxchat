# -*- coding: utf-8 -*-


import requests
import json


def talk(content):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    s = requests.session()
    d = {"userInfo": {
        "apiKey": "89311862f779453d891b003e28091e6a",
        "userId": "1"
    }, "perception": {
        "inputText": {
            "text": content
        }
    }
    }
    data = json.dumps(d)
    r = s.post(url, data=data)
    text = json.loads(r.text)
    '''print(text)
    print(text["results"])'''
    return text["results"][0]["values"]["text"]