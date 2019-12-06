#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
argv = sys.argv

sys.path.append(argv[1])
import myhooktools.precommithook as commit


if __name__ == '__main__':
    hook_obj = commit.GitPreHook(sys.argv)
    access = hook_obj.CheckCode()
    sys.exit(access)
