# -*- coding:utf-8 -*-
import sys
path = sys.argv[1]
sys.path.append(path)

msg_path = path + "/" + ".git/COMMIT_EDITMSG"

class GitCommitMsg:

    def __init__(self):
        self.access = 1

    def CheckMsg(self):
        try:
            with open(msg_path, "r", encoding='UTF-8') as fp:
                _msg_info = fp.read()
                if len(self._msg_info)<5:
                    self.access = 0
                    print("\033[0;31;40m \t%s len < 5 \033[0m" % self._msg_info)
        except FileNotFoundError as e:
            print("\033[0;31;33m \t%s not find \033[0m" % ".git/COMMIT_EDITMSG")
            self.access = 0
        except Exception as e:
            self.access = 0
            raise e
        else:
            print("")


if __name__ == '__main__':
    hook_obj = GitCommitMsg()
    access = hook_obj.CheckMsg()
    sys.exit(access)