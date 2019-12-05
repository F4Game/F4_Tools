# -*- coding:utf-8 -*-

import ast

class PreHookException(Exception):
    pass

class Vistator(ast.NodeVisitor):

    def visit_Print(self,node):
        raise PreHookException("code find print!!!")

    def visit_Name(self,node):
        pass

    def visit_arg(self,node):
        pass

    def visit_FunctionDef(self, node):
        pass

    def generic_visit(self,node):
        super(Vistator,self).generic_visit(node)

    def visit(self, node):
        super(Vistator,self).visit(node)