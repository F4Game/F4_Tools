# -*- coding:utf-8 -*-
import sys

class CommitMsgException(Exception):
    pass

class GitCommitMsg:

    def __init__(self, args):
        self._msg_info = args[1]

    def Print(self):
        print(self._msg_info)

if __name__ == '__main__':
    hook_obj = GitCommitMsg(sys.argv)
    hook_obj.Print()