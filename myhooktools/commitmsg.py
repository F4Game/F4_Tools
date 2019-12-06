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
                if len(_msg_info)<5:
                    self.access = 0
                    print("\033[0;31;36m msg:\"%s\" len < 5 \033[0m" % str.strip(_msg_info), end="")
        except FileNotFoundError:
            print("\033[0;31;33m \t%s not find \033[0m" % ".git/COMMIT_EDITMSG")
            self.access = 0
        except Exception as e:
            self.access = 0
            raise e
        else:
            print("\033[0;31;36m msg:\"%s\" len < 5 \033[0m" % str.strip(_msg_info), end="")
        return self.access


if __name__ == '__main__':
    hook_obj = GitCommitMsg()
    access = hook_obj.CheckMsg()
    sys.exit(access)