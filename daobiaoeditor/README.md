# 前言

本导表目前只支持xls格式的文件（wps表格文件），最初设计是为了能够自动化生成C#对象代码及其枚举类型以及该对象工厂类的一个自动化生成工具。


## 使用规则

### 表格填写规范


![image](https://github.com/AllenGX/daobiaoeditor/blob/master/daobiao/session/pic.png)

1. 目前xls文件只用到了2个表——Sheet1和Sheet2。除此以外的其他表不做解析
2. Sheet1用作obj对象生成，Sheet2用作枚举类型生成。
3. Sheet1书写规则:
    - 第一行必须是属性名
    - 第二行必须是属性类型，类型目前支持七种——整数（int），浮点数（float），字符串（string），整数列表（list-int），浮点数列表（list-float），字符串列表（list-string），枚举字符串（define-string）
    - 第一列必须为obj对象，对应的值为其他列的合并，合并规则如下
    ```
    # xls文件obj的聚合公式
    xls = """   
        &"@"&B3&"|"&C3&"|"&D3&"|"&E3&"|"&F3&"|"&G3&"|"&H3&"@"&
    """
    ```
    - 列表对象之间用,号隔开
4. Sheet2书写规则:
    - 第一列为枚举类型对象名
    - 第二列为枚举类型值
    - 第三列为该枚举类型描述

### 使用方法
在  daobiaoeditor\daobiao\p_editor  目录下创建自己的p_XXX模块 并在该模块的 __init__.py 文件内定义自己的editor类型，格式如下：

```python
import p_editor.p_base as base

class PersonEditor(base.BaseEditor):
    def __init__(self):
        super(PersonEditor, self).__init__()
        self.m_fileName = "第一份导表.xls"  # 导表文件名
        self.m_writePath = "../objs/"  # 要导入的路径
        self.m_defineName = "Defines"  # define 类型
        self.m_objName = "Person"   # 导入的对象名称
        self.Init()

    def GetObjContent(self, iIndex):
        参照person书写自己的解析函数
```

书写完毕后，在 daobiaoeditor\daobiao\p_editor\loadeditor.py 文件内加入自己的editor对象

```python
import p_editor.p_person as person
# 加入你的editor

editorList = [
    person.PersonEditor(),
    # 并在此创建它
]

for ed in editorList:
    ed.WriteAllObj()
    ed.WriteAllDfeine()
    ed.WriteAllLoad()

```

最后执行 python loadeditor.py 即可
