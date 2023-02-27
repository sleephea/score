def FormDataToDict(rawFormData):
    strAllStrip = rawFormData.replace(" ", "")  # 去除全部空格
    # print(strAllStrip)
    strSplitEnter = strAllStrip.split('\n')  # 以回车为分隔
    # print(strSplitEnter)
    formData = dict(map(lambda s: s.split(':'), strSplitEnter))  # 列表里每一个元素以':'为分隔生成字典
    return formData
