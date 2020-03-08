# -*- coding:utf-8 -*-

from test_celery.tasks import add,xsum,mul


for i in range(1):
    add.delay(i,i+1)
    xsum.delay([i+1,i,i-1])
    mul.delay(i,i*i)

print("ok")