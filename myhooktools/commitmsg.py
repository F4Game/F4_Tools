# -*- coding:utf-8 -*-
import sys
argv = sys.argv
sys.path.append(argv[1])

class GitCommitMsg:

    def __init__(self, args):
        self.access = 1
        self._msg_info = args[2]
        print(self._msg_info)

    def CheckMsg(self):
        if len(self._msg_info)<5:
            self.access = 0
            print("\033[0;31;40m \t%s len < 5 \033[0m" % self._msg_info)

if __name__ == '__main__':
    hook_obj = GitCommitMsg(sys.argv)
    access = hook_obj.CheckMsg()
    sys.exit(access)