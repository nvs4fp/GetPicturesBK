#Initialized by Levi Li
#Date: 19-Apr-2017
#Discription: Just for the study
#History
#--------------------------------------------------------
#Date               Useer                   Discription
#19-Apr-
#19-Apr-2017        Levi Li                 Create
#19-Apr-2017        Levi Li                 Create
#--------------------------------------------------------
'''

'''

import requests
if __name__ == "__main__":
    print('Hello python!')
    res=requests.get(r"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1492305816848_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%A1%83%E8%8A%B1")
    print(res.content)

