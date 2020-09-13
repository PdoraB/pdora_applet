#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: index.py
@time: 2020/9/13
@desc:
'''
from flask import Blueprint
route_index = Blueprint("index_page",__name__)


@route_index.route("/")
def index():
    return "hello word"