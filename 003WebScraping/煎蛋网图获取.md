```python
>>> import requests
>>> url = "http://jandan.net/ooxx"
>>> wb_data = requests.get(url)
>>> print(wb_data)
<Response [200]>
```
返回状态码200，状态码不是200的都不算正常访问。
```python
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(wb_data.text, 'lxml')
>>> img = soup.select("div > div > div.text > p > img")
```

获取所有链接的src部分
```
for i in img:
    pic_link = ("http:" + i.get('src'))
    print(pic_link)
```

获取多个页面
```python
>>> urls = ['http://jandan.net/ooxx/page-{}'.format(str(i)) for i in range(1,12)]
```
![code](https://github.com/xiucz/python/blob/master/003WebScraping/pictures/20170928.jpg)
## Reference_info
http://mp.weixin.qq.com/s/d7v3tO7i6n9X6CLExUcryQ
