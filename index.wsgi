# -*- coding: utf-8 -*-

import os
import sae
import web

from chat import WeixinInterface

urls = (
'/weixin','WeixinInterface'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(self.app_root, 'templates')
render = web.templates.render(self.templates_root)

app = web.application(urls,global()).wsgifuc()
application = sae.create_wsgi_app(app)
