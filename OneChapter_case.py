# urllib是Python中的标准库，包含了从网络请求数据，处理cookie，改变请求头和用户代理这些元数据的等等一些函数。
# BeautifulSoup不是Python的标准库，它通过定位HTML标签来格式化和组织复杂的网络信息。
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
'''
网络采集问题：网页数据格式不友好，网站服务器宕机，目标数据的标签找不到等等。
主要可能发生两种异常：
    1.网页在服务器上不存在
        异常发生时，程序会返回HTTP错误（如“404 Page Not Found”，“500 Internal Server Error”等）。
        所有类似情形，urlopen函数都会抛出“HTTPError”异常。
2.服务器不存在
    如果服务器不存在，urlopen会返回一个None对象。（与其他语言中的null类似）
'''
'''
BeautifulSoup库里的主要对象：
1.BeautifulSoup对象
2.标签Tag对象
3.NavigableString对象
    用来表示标签里的文字，不是标签。
4.Comment对象
    用来查找HTML文档的注释标签，<!-- 像这样 -->
'''
def getImg(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features="html.parser")
        # 只能获取页面中的第一个指定的标签，就是body中的第一个img
        img = bsObj.body.img
    except AttributeError as e:
        return None
    return img

img = getImg("http://www.baidu.com/")
if img == None:
    print("Img could not be found")
else:
    print(img)

