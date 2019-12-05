# github_pre_hook


## 原理

针对commit提交的文件名称，定位其绝对路径，并通过ast语法树判断是否符合规范。

## 主要用途

简单的进行代码检测，或者预防内存泄露（在python协程中引用某个对象导致）。

## 构建github代码检测

- 把 pre-commit 文件加入到 .git/hook/ 目录下
- 针对ast库语法树，来对自己感兴趣的模块进行筛选

```python
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
```

## 如何自定义

针对不同的标签：
- Name
- arg
- FunctionDef
- ...

来进行相应的筛选操作，例如这里对print进行了一个简单筛选，只要代码中存在print，则会直接对commit操作进行回撤。

## 标签怎么查看

```python
# 格式输出解析函数
def nodeTree(node:str):
    str2list = list(node.replace(' ', ''))
    count = 0
    for i, e in enumerate(str2list):
        if e == '(':
            count += 1
            str2list[i] = '(\n{}'.format('|   ' * count)
        elif e == ')':
            count -= 1
            str2list[i] = '\n{})'.format('|   ' * count)
        elif e == ',':
            str2list[i] = ',\n{}'.format('|   ' * count)
        elif e == '[':
            count += 1
            str2list[i] = '[\n{}'.format('|   ' * count)
        elif e == ']':
            count -= 1
            str2list[i] = '\n{}]'.format('|   ' * count)

    return ''.join(str2list)

expr = """
@dec
def add(arg1, arg2):
    print(arg1+arg2)
"""
expr_ast = ast.parse(expr)
v = CVistor()
v.visit(expr_ast)
node_tree = ast.dump(expr_ast)

print(nodeTree(node_tree))

---------------------------result-------------------------
Module(
|   body=[
|   |   FunctionDef(
|   |   |   name='add',
|   |   |   args=arguments(
|   |   |   |   args=[
|   |   |   |   |   arg(
|   |   |   |   |   |   arg='arg1',
|   |   |   |   |   |   annotation=None
|   |   |   |   |   ),
|   |   |   |   |   arg(
|   |   |   |   |   |   arg='arg2',
|   |   |   |   |   |   annotation=None
|   |   |   |   |   )
|   |   |   |   ],
|   |   |   |   vararg=None,
|   |   |   |   kwonlyargs=[
|   |   |   |   |   
|   |   |   |   ],
|   |   |   |   kw_defaults=[
|   |   |   |   |   
|   |   |   |   ],
|   |   |   |   kwarg=None,
|   |   |   |   defaults=[
|   |   |   |   |   
|   |   |   |   ]
|   |   |   ),
|   |   |   body=[
|   |   |   |   Expr(
|   |   |   |   |   value=Call(
|   |   |   |   |   |   func=Name(
|   |   |   |   |   |   |   id='print',
|   |   |   |   |   |   |   ctx=Load(
|   |   |   |   |   |   |   |   
|   |   |   |   |   |   |   )
|   |   |   |   |   |   ),
|   |   |   |   |   |   args=[
|   |   |   |   |   |   |   BinOp(
|   |   |   |   |   |   |   |   left=Name(
|   |   |   |   |   |   |   |   |   id='arg1',
|   |   |   |   |   |   |   |   |   ctx=Load(
|   |   |   |   |   |   |   |   |   |   
|   |   |   |   |   |   |   |   |   )
|   |   |   |   |   |   |   |   ),
|   |   |   |   |   |   |   |   op=Add(
|   |   |   |   |   |   |   |   |   
|   |   |   |   |   |   |   |   ),
|   |   |   |   |   |   |   |   right=Name(
|   |   |   |   |   |   |   |   |   id='arg2',
|   |   |   |   |   |   |   |   |   ctx=Load(
|   |   |   |   |   |   |   |   |   |   
|   |   |   |   |   |   |   |   |   )
|   |   |   |   |   |   |   |   )
|   |   |   |   |   |   |   )
|   |   |   |   |   |   ],
|   |   |   |   |   |   keywords=[
|   |   |   |   |   |   |   
|   |   |   |   |   |   ]
|   |   |   |   |   )
|   |   |   |   )
|   |   |   ],
|   |   |   decorator_list=[
|   |   |   |   Name(
|   |   |   |   |   id='dec',
|   |   |   |   |   ctx=Load(
|   |   |   |   |   |   
|   |   |   |   |   )
|   |   |   |   )
|   |   |   ],
|   |   |   returns=None
|   |   )
|   ]
)
```


## 具体效果

```shell
=====================pre-commit========================
check - file: D:/github_pre_hook/test/test_print.py     code find print!!!
========================end============================
                 Please check the code
```

```python
test_print.py

# -*- coding:utf-8 -*-
print("test-print")


def Print():
    print("test-print")


def test():
    print = 1

```

## 如何绕过检查

> git commit -m "xxx" --no-verify

## 后续扩展

还可以对 commit -m "desc" 中的desc进行检查，更有趣的可以对代码进行规范化
