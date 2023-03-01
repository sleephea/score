from GetAllScoreDataFromExcel import GetAllScoreDataFromExcel
from SubmitData import SubmitData

if __name__ == '__main__':
    allScoreDataFromExcel = GetAllScoreDataFromExcel()  # 返回值为一个嵌套列表，三层嵌套，最外层为各个班的数据，第二层为某个版各个学生的数据，最内层为学生信息列表
    # print(allScoreDataFromExcel)

    # 一班 3502606 二班 3489682 三班 3489695 四班 3489696 五班 3502610 六班 3502611 七班 3489697 八班 3502612 九班 3502613十班 3489698 十一班 3489699 
    classNumbers = [3502606, 3489682, 3489695, 3489696, 3502610, 3502611, 3489697, 3502612, 3502613, 3489698, 3489699]

    cookie = "WMONID=59IkNTQDYXP; JSESSIONID_GGFWDT=QAybVKe3--6eB6m8opQnkZl9HJaE9oqL3S3OM5SbloX4Je1nReOb!1462964836!-1321469817"

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
