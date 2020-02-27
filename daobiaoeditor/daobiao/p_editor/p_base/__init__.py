import p_editor
import os


class BaseEditor:
    def __init__(self):
        self.m_fileName = "第一份导表.xls"
        self.m_writePath = "../objs/"
        self.m_defineName = "Defines"
        self.m_objName = "Person"
        self.Init()

    def Init(self):
        self.m_start = "//导表开始\n"
        self.m_end = "\n//导表结束\n"
        self.m_rootPath = "../session/"
        self.m_objPath = "Sheet1"
        self.m_definePath = "Sheet2"

        self.m_editor = p_editor.Editor(self.m_rootPath, self.m_fileName, self.m_objPath)
        self.m_define = p_editor.Editor(self.m_rootPath, self.m_fileName, self.m_definePath)

    def WriteAllLoad(self):
        sText = self.GetLoad()
        self.WriteLoad(sText)

    def WriteAllDfeine(self):
        sText = self.GetDefine()
        self.WriteDefine(sText)

    def WriteAllObj(self):
        for iIndex in range(len(self.m_editor.m_objDataList)):
            index, sText = self.GetObjContent(iIndex + 2)
            self.WriteObj(index, sText)

    def WriteObj(self, iIndex, sText):
        sFilepath = self.m_writePath + self.m_objName.lower() + str(iIndex) + ".cs"
        self.Write(sFilepath, sText)

    def WriteLoad(self, sText):
        sFilepath = self.m_writePath + "load.cs"
        self.Write(sFilepath, sText)

    def WriteDefine(self, sText):
        sFilepath = self.m_writePath + "define.cs"
        self.Write(sFilepath, sText)

    def GetObjContent(self, iIndex):
        pass

    def GetObjId(self, iIndex):
        return self.m_editor.GetAtr(iIndex + 2, "ID")

    def GetDefine(self):
        sText = """
using System.Collections;
using System.Collections.Generic;

public enum %s
{
""" % (self.m_defineName)
        for iIndex in range(len(self.m_define.m_sDefine)):
            sDefine = "\t" + self.m_define.m_sDefine[iIndex] + "=" + \
                      self.m_define.m_sDefineValue[iIndex] + ",//" + \
                      self.m_define.m_sDefineName[iIndex] + "\n"
            sText += sDefine
        sText += "\n}"
        return sText

    def GetLoad(self):
        sName = self.m_objName
        sContent = ""
        for iIndex in range(len(self.m_editor.m_objDataList)):
            index = self.GetObjId(iIndex)
            s = "\t\tthis." + sName.lower() + "Dict.Add(" + str(index) + ", new " + sName + str(index) + "());\n"
            sContent += s
        sText = """
using System.Collections;
using System.Collections.Generic;

public class %sFactory
{
    private Dictionary<int,Person> %sDict = new Dictionary<int, %s>();
    
    public %sFactory()
    {
%s
    }

    public %s Create%s(int %sId)
    {
        return this.%sDict[%sId].Clone();
    }
}
        """ % (sName, sName.lower(), sName, sName, sContent, sName, sName, sName.lower(), sName.lower(), sName.lower())
        return sText

    def Write(self, sFilepath, sText):
        sText = self.m_start + sText + self.m_end
        # 不存在直接开搞
        if not os.path.exists(sFilepath):
            with open(sFilepath, "w", encoding="utf-8") as f:
                f.writelines(sText)
        else:
            start = 0
            end = 0
            with open(sFilepath, 'r', encoding="utf-8") as f:
                sContent = f.readlines()
                f.close()
            for index, line in enumerate(sContent):
                if "//导表开始" in line:
                    start = index
                if "//导表结束" in line:
                    end = index
            if start >= end:
                print("写入失败，头尾标识有误")
            del sContent[start:end + 1]
            sContent.insert(start, sText)
            with open(sFilepath, 'w', encoding="utf-8") as f:
                f.writelines(sContent)
