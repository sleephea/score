from GetAllScoreDataFromExcel import GetAllScoreDataFromExcel
from SubmitData import SubmitData

if __name__ == '__main__':
    allScoreDataFromExcel = GetAllScoreDataFromExcel()  # 返回值为一个嵌套列表，三层嵌套，最外层为各个班的数据，第二层为某个版各个学生的数据，最内层为学生信息列表
    # print(allScoreDataFromExcel)

    # 一班 2166609 二班 2166610 三班 2161811 四班 2166611 五班 2166612 六班 2161812 七班 2166613
    classNumbers = [2166609, 2166610, 2161811, 2166611, 2166612, 2161812, 2166613]

    cookie = "WMONID=5h_Kln4_HZ2; JSESSIONID_GGFWDT=M3W_e7azuNTvHQGXussuBJEDsQCoHuMJR1rJ0ktlLH5I1v9fbkPi!996039092!NONE"

    SubmitData(allScoreDataFromExcel, classNumbers, cookie)


'''
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
