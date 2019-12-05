# -*- coding:utf-8 -*-

import myhooktools.astcheck as ast_check
import ast

__all__ = ["GitPreHook"]


def IsCheckFile(filename):
    if filename.find("myhooktools") != -1:
        return False
    return True


class GitPreHook:

    def __init__(self, args):
        self.access = 1
        self._root_path = args[1]
        self._commit_file_path = args[2:]

    def CheckCode(self):
        for _file_name in self._commit_file_path:
            filename = self._root_path + "/" + _file_name
            if not IsCheckFile(filename):
                continue
            print("check - file:", filename, end="")
            try:
                with open(filename, "r", encoding='UTF-8') as fp:
                    _file_context = fp.read()
                    _file_node_tree = ast.parse(_file_context)
                    _ast_check_obj = ast_check.Vistator()
                    _ast_check_obj.visit(_file_node_tree)
            except ast_check.PreHookException as e:
                print("\033[0;31;40m \t%s \033[0m" % e.err_info)
                self.access = 0
            except Exception as e:
                self.access = 0
                raise e
            else:
                print("")
        return self.access
