#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: www.py
@time: 2020/9/13
@desc:
'''
from webs.controllers.index import route_index
from application import app

app.register_blueprint(route_index,url_prefix = "/")