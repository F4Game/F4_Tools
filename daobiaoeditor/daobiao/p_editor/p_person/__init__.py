import p_editor.p_base as base


class PersonEditor(base.BaseEditor):
    def __init__(self):
        super(PersonEditor, self).__init__()
        self.m_fileName = "第一份导表.xls"  # 导表文件名
        self.m_writePath = "../objs/"  # 要导入的路径
        self.m_defineName = "Defines"  # define 类型
        self.m_objName = "Person"
        self.Init()

    def GetObjContent(self, iIndex):
        sText = """
using System.Collections.Generic;

public class Person2 : Person
{
    private int personID = %s;                   // int ID
    private Defines efftype = %s;// 字符串枚举
    private float f = %s;                     // float
    private string s = "%s";         // string
    private List<int> vi = new List<int> %s;// list-int
    private List<string> vs = new List<string> %s; // list-string
    private List<float> vf = new List<float> %s; // list-float
}

        """ % (self.m_editor.GetAtr(iIndex, "ID"),
               self.m_defineName + "." + self.m_editor.GetAtr(iIndex, "字符串枚举"),
               self.m_editor.GetAtr(iIndex, "浮点数"),
               self.m_editor.GetAtr(iIndex, "字符串"),
               self.m_editor.GetAtr(iIndex, "整数列表"),
               self.m_editor.GetAtr(iIndex, "字符串列表"),
               self.m_editor.GetAtr(iIndex, "浮点数列表"))
        return self.m_editor.GetAtr(iIndex, "ID"), sText
