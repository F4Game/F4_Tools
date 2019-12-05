# -*- coding:utf-8 -*-
import sys

class CommitMsgException(Exception):
    pass

class GitCommitMsg:

    def __init__(self, args):
        self.root_path = args[0]
        self.commit_file_path = args[1]
        self.commit_msg = args[2]

    def Print(self):
        print(self.root_path)
        print(self.commit_file_path)
        print(self.commit_msg)


if __name__ == '__main__':
    hook_obj = GitCommitMsg(sys.argv)
    hook_obj.Print()