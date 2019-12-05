#!/usr/bin/env python
# -*- coding:utf-8 -*-

from myhooktools.precommithook import GitPreHook
import sys


if __name__ == '__main__':
    hook_obj = GitPreHook(sys.argv)
    hook_obj.Print()

