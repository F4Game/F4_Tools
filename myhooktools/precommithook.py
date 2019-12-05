# -*- coding:utf-8 -*-

import myhooktools.astcheck as ast_check
import ast

__all__ = ["GitPreHook"]


class GitPreHook:

    def __init__(self, args):
        self._root_path = args[1]
        self._commit_file_path = args[2:]

    def CheckCode(self):
        for _file_name in self._commit_file_path:
            filename = self._root_path + "/" + _file_name
            print("filename",filename)
            with open(filename,"r",encoding='UTF-8') as fp:
                _file_context=fp.read()
                _file_node_tree = ast.parse(_file_context)
                print("123")
                _ast_check_obj = ast_check.Vistator()
                _ast_check_obj.visit(_file_node_tree)

