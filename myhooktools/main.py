#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
argv = sys.argv[1]

sys.path.append(argv[1])
import myhooktools.precommithook as commit


if __name__ == '__main__':
    hook_obj = commit.GitPreHook(sys.argv)
    hook_obj.CheckCode()
