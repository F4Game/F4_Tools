# -*- coding:utf-8 -*-

__all__= ["GitPreHook"]

class PreHookException(Exception):
    pass


class GitPreHook:

    def __init__(self, args):
        print("all ->>>>> args",args)
        self.root_path = args[1]
        self.commit_file_path = args[2]

    def Print(self):
        print(self.root_path)
        print("commit_file_path->>>>>>>>>>",self.commit_file_path)
    def CheckCode(self):
        pass
        # for file_name in self.commit_file_path:
        #     print()
        #     with open(self.root_path+"/"+file_name) as fp:
        #         print(fp.read())
