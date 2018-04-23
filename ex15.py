import re
import urllib.request
def craw(url):
    html1= urllib.request.urlopen(url).read()
    html1= str(html1)
    pat1 = '<div id = "plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1= result1[0]
    pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(' \
           '.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)
    urllib.request.urlretrieve("http://"+imagelist[0],"d:/python/mm.jpg")
craw("https://list.jd.com/list.html?tid=1001053&page=2")