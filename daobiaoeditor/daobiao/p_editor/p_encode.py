def Encode(sData, sType):
    if sType == "int":
        return EncodeInt(sData)
    elif sType == "float":
        return EncodeFloat(sData)
    elif sType == "string":
        return EncodeString(sData)
    elif sType == "list-int":
        return EncodeList_Int(sData)
    elif sType == "list-float":
        return EncodeList_Float(sData)
    elif sType == "list-string":
        return EncodeList_String(sData)
    elif sType == "define-string":
        return EncodeDefine_String(sData)


def EncodeInt(sData):
    return str(int(sData))


def EncodeString(sData):
    return sData


def EncodeFloat(sData):
    return str(sData) + "f"


def EncodeList_Int(sData):
    return "{" + sData + "}"


def EncodeList_Float(sData):
    sAtrList = sData.split(",")
    sResult = "{"
    for index in range(len(sAtrList)):
        sResult += sAtrList[index] + "f"
        if index != len(sAtrList):
            sResult += ","
    sResult += "}"
    return sResult


def EncodeList_String(sData):
    return "{" + sData + "}"


def EncodeDefine_String(sData):
    return sData