#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
root_path = sys.argv[1]
print(root_path)
sys.path.append(root_path)

import myhooktools.precommithook as commit

if __name__ == '__main__':
    hook_obj = commit.GitPreHook(sys.argv)
    hook_obj.Print()

