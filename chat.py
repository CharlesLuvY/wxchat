# -*- coding:utf-8 -*-
import web
from handle import Handle
from web.template import ALLOWED_AST_NODES

ALLOWED_AST_NODES.append('Constant')
urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()