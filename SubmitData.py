import time

from tools.GetClassMembers import GetClassMembers
from tools.SubmitUnitData import SubmitUnitData


# 将处理的数据POST提交至网站，实现自动化提交
def SubmitData(allScoreDataFromExcel, classNumbers, cookie):
    # 提交所有班的所有人员数据
    for i in range(len(classNumbers)):
        # 请求某个班的所有人员数据
        members = GetClassMembers(classNumbers[i], cookie)
        for member in members:
            print("姓名：" + member["aac003"] + "\t学生编号：" + str(member["ahc400"]) + "\t联系电话：" + str(member["aae005"]))
            # 构建提交表单，并提交
            for unitScore in allScoreDataFromExcel[i]:
                if unitScore[2] == member["aae005"]:  # 如果判断Excel数据里某个班的某个学生电话号码与当前要提交信息的该电话号码一致，那么将他的成绩信息也查出来，以便信息提交
                    # 根据这些信息构建formData
                    formData = {"hcc105": (1 if unitScore[5] == '是' else 0),  # 是否合格，合格为1
                                "chz083": unitScore[4],  # 理论成绩
                                "chz084": '',  # 实操成绩
                                "chz085": unitScore[3],  # 综合成绩
                                "ahc400": member["ahc400"]}
                    print(formData)
                    # 提交这一位同学的成绩的信息
                    SubmitUnitData(formData, cookie)
        time.sleep(10)
    return 0


"""

POST录入成绩接口
Request URL: http://103.239.153.109/sdjyweb/proxy/qdaio-ggjy/d3/d32501/updateHc40
Request Method: POST
Status Code: 200 OK
Remote Address: 127.0.0.1:7890
Referrer Policy: strict-origin-when-cross-origin

Connection: keep-alive
Content-Type: text/html;charset=UTF-8
Date: Mon, 06 Sep 2021 11:05:04 GMT
Keep-Alive: timeout=4
Proxy-Connection: keep-alive
Server: nginx/1.14.0
Transfer-Encoding: chunked

Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Content-Length: 54
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: WMONID=5h_Kln4_HZ2; JSESSIONID_GGFWDT=OWe6xvHPWIjy5OFRwKvaTPX6bEK9-zTAg7jIc2HSRJ5bIxfdXIla!639384706!NONE
Host: 103.239.153.109
Origin: http://103.239.153.109
Proxy-Connection: keep-alive
Referer: http://103.239.153.109/sdjyweb/business/unit/toWorkspaceTrain.action
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
X-Requested-With: XMLHttpRequest

hcc105: 0
chz083: 98
chz084: 80
chz085: 56
ahc400: 20722488

"""

"""

sEcho: 3
iColumns: 14
sColumns: 
iDisplayStart: 10
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
ahb500: 1827593

"""

"""
查询某个班的所有人员接口

Request URL: http://103.239.153.109/sdjyweb/business/train/unit/queryClassRyxx.action
Request Method: POST
Status Code: 200 OK
Remote Address: 127.0.0.1:7890
Referrer Policy: strict-origin-when-cross-origin

Connection: keep-alive
Content-Length: 5649
Content-Type: application/json;charset=UTF-8
Date: Mon, 06 Sep 2021 11:53:21 GMT
Keep-Alive: timeout=4
Proxy-Connection: keep-alive
Server: nginx/1.14.0

Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
Content-Length: 1038
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: WMONID=5h_Kln4_HZ2; JSESSIONID_GGFWDT=OWe6xvHPWIjy5OFRwKvaTPX6bEK9-zTAg7jIc2HSRJ5bIxfdXIla!639384706!NONE
Host: 103.239.153.109
Origin: http://103.239.153.109
Proxy-Connection: keep-alive
Referer: http://103.239.153.109/sdjyweb/business/unit/toWorkspaceTrain.action
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
X-Requested-With: XMLHttpRequest

sEcho: 12
iColumns: 14
sColumns: 
iDisplayStart: 0
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
ahb500: 2161811

"""
