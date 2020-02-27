import xlrd
import p_editor.p_encode

# xls文件obj的聚合公式
xls = """   
&"@"&
B3
&"|"&
C3
&"|"&
D3
&"|"&
E3
&"|"&
F3
&"|"&
G3
&"|"&
H3
&"@"&
"""


class Editor:
    def __init__(self, sRootPath, sXlrdName, sSheetName):
        self.m_RootPath = sRootPath  # session根目录(xlrd根目录)
        self.m_XlrdObj = None
        self.m_keyList = []  # 表中字段名称
        self.m_typeList = []  # 表中各字段类型
        self.m_objDataList = []  # 表中对象的全部数据
        self.m_sXlrdName = sXlrdName  # 文件名
        self.m_sSheetName = sSheetName  # 表名

        self.m_sDefine = []  # 枚举名
        self.m_sDefineValue = []  # 枚举值
        self.m_sDefineName = []  # 枚举解释

        if sSheetName == "Sheet1":
            self.LoadXlrd(sXlrdName, sSheetName)
        elif sSheetName == "Sheet2":
            self.LoadDefine(sXlrdName, sSheetName)

    def LoadXlrd(self, sXlrdName, sSheetName):
        wb = xlrd.open_workbook(filename=self.m_RootPath + sXlrdName)
        ws = wb.sheet_by_name(sSheetName)
        self.m_XlrdObj = ws

        # 第一行默认都是字段名称
        # 第一列默认都是对象数据
        for keyIndex in range(ws.ncols):
            self.m_keyList.append(ws.cell(0, keyIndex).value)
        self.m_keyList.pop(0)
        # 第二行默认都是字段类型
        for typeIndex in range(ws.ncols):
            self.m_typeList.append(ws.cell(1, typeIndex).value)
        self.m_typeList.pop(0)
        # 第三行默认都是字段属性
        for objValueIndex in range(ws.nrows - 2):
            self.m_objDataList.append(ws.cell(objValueIndex + 2, 0).value)

    def LoadDefine(self, sXlrdName, sSheetName):
        wb = xlrd.open_workbook(filename=self.m_RootPath + sXlrdName)
        ws = wb.sheet_by_name(sSheetName)

        # 第一列默认都是枚举名
        for d in range(ws.nrows):
            self.m_sDefine.append(ws.cell(d, 0).value)
        # 第二列默认都是枚举值
        for dv in range(ws.nrows):
            self.m_sDefineValue.append(ws.cell(dv, 1).value)
        # 第三列默认都是解释
        for dn in range(ws.nrows):
            self.m_sDefineName.append(ws.cell(dn, 2).value)

    def GetAtr(self, iIndex, sAtr):
        for index in range(len(self.m_keyList)):
            if self.m_keyList[index] == sAtr:
                return p_editor.p_encode.Encode(self.m_XlrdObj.cell(iIndex, index + 1).value,
                                                self.m_typeList[index])
        return None
