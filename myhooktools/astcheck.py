# -*- coding:utf-8 -*-

import ast

class PreHookException(Exception):
    def __init__(self, info):
        self.err_info = info

class Vistator(ast.NodeVisitor):

    def visit_Print(self):
        raise PreHookException("code find print!!!")

    def visit_Name(self,node):
        if node.id == "print":
            self.visit_Print()

    def visit_arg(self,node):
        pass

    def visit_FunctionDef(self, node):
        pass

    def generic_visit(self,node):
        super(Vistator,self).generic_visit(node)

    def visit(self, node):
        super(Vistator,self).visit(node)
