#Initialized by Levi Li
#Date: 19-Apr-2017
#Discription: Just for the study
#History
#--------------------------------------------------------
#Date               Useer                   Discription
#16-Apr-2017        Levi Li                 Initial
#16-Apr-2017        Levi Li                 Submit into git hub
#--------------------------------------------------------
'''
<img class="main_img img-hover" data-imgurl="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=4225527214,2698476519&amp;fm=23&amp;gp=0.jpg" src="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=4225527214,2698476519&amp;fm=23&amp;gp=0.jpg" style="background-color: rgb(182, 173, 173); width: 295px; height: 197px;">

'''

import requests
if __name__ == "__main__":
    print('Hello python!')
    res=requests.get(r"https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1492305816848_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E6%A1%83%E8%8A%B1")
    print(res.content)

