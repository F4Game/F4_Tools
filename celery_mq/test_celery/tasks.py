# -*- coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals

from .celery import app

i = 0

@app.task
def add(x, y):
    global i
    i+=1
    print("add ok",i)
    return x + y


@app.task
def mul(x, y):
    global i
    i += 1
    print("mul ok",i)
    return x * y


@app.task
def xsum(numbers):
    global i
    i += 1
    print("xsum ok ",i)
    return sum(numbers)