import json

import requests

from tools.FormDataToDict import FormDataToDict


# 请求某个班的所有人员数据，并返回所需数据
def GetClassMembers(classNumber, cookie):
    base_url = "http://103.239.153.109/sdjyweb/business/train/unit/queryClassRyxx.action"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Cookie": cookie,
    }

    rawFormData = '''sEcho: 
    iColumns: 14
    sColumns: 
    iDisplayStart: {displayStart}
    iDisplayLength: 10
    mDataProp_0: aac147
    mDataProp_1: ahc404name
    mDataProp_2: aac003
    mDataProp_3: aac004
    mDataProp_4: aac011name
    mDataProp_5: aac009name
    mDataProp_6: aae321
    mDataProp_7: ahc426name
    mDataProp_8: chz003
    mDataProp_9: hcc105
    mDataProp_10: chz083
    mDataProp_11: chz084
    mDataProp_12: chz085
    mDataProp_13: ahc400
    sSearch: undefined
    bRegex: false
    sSearch_0: 
    bRegex_0: false
    bSearchable_0: true
    sSearch_1: 
    bRegex_1: false
    bSearchable_1: true
    sSearch_2: 
    bRegex_2: false
    bSearchable_2: true
    sSearch_3: 
    bRegex_3: false
    bSearchable_3: true
    sSearch_4: 
    bRegex_4: false
    bSearchable_4: true
    sSearch_5: 
    bRegex_5: false
    bSearchable_5: true
    sSearch_6: 
    bRegex_6: false
    bSearchable_6: true
    sSearch_7: 
    bRegex_7: false
    bSearchable_7: true
    sSearch_8: 
    bRegex_8: false
    bSearchable_8: true
    sSearch_9: 
    bRegex_9: false
    bSearchable_9: true
    sSearch_10: 
    bRegex_10: false
    bSearchable_10: true
    sSearch_11: 
    bRegex_11: false
    bSearchable_11: true
    sSearch_12: 
    bRegex_12: false
    bSearchable_12: true
    sSearch_13: 
    bRegex_13: false
    bSearchable_13: true
    ahb500: {classNumber}'''

    membersData = []
    for i in range(0, 61, 10):  # 为啥范围设置[0, 60]步长为10？因为应该查看，几乎所有班级都不会超过60人，而接口的写法必须是10个数据为一组返回
        # print(i)
        formData = FormDataToDict(rawFormData.format(classNumber=classNumber, displayStart=i))
        response = requests.post(base_url, headers=headers, data=formData)  # 发送请求，并返回数据
        aSetMembersData = json.loads(response.text)["aaData"]  # 返回一个列表，列表里有一个班所有学生的各种信息的字典
        for memberData in aSetMembersData:  # 将一组中所有的单条学生信息字典都拿出来，放到membersData列表中
            membersData.append(memberData)

    # print(membersData)
    return membersData
    # 3502606
