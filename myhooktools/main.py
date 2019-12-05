#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

class PreHookException(Exception):
    pass


class GitPreHook:

    def __init__(self,args):
        self.root_path = args[0]
        self.commit_file_path = args[1]
        self.commit_msg = args[2]

    def Print(self):
        raise PreHookException(self.root_path)
        raise PreHookException(self.commit_file_path)
        raise PreHookException(self.commit_msg)



if __name__ == '__main__':
    hook_obj = GitPreHook(sys.argv)
    hook_obj.Print()