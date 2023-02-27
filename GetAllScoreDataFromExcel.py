# 处理下载下来的原始Excel表格

import xlwings as xw  # 导入xlwings库


def GetAllScoreDataFromExcel():
    wb = xw.Book(r'D:\创新创业\计算机等级考试信息录入\RawData\烟台大学计划书成绩816-魔改.xlsx')  # 建立Excel表连接

    rawExcelData = []
    for i in range(0, 7):  # 迭代 0 到 6 之间的数字，即表中的0 ~ 6 Sheet。
        rawExcelData.append(wb.sheets[i].range('A2').expand().value) # 为了去掉头，从A2行开始读取)
        # print(rawExcelData[i])

    return rawExcelData  # 返回一个嵌套列表，里面有各个班的列表
