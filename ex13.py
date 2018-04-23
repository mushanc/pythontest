import urllib.request
import urllib.parse

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login" \
      "&loginsubmit=yes&loginhash=L768q"
postdata = urllib.parse.urlencode({
    "username":"weisuen",
    "password":"aA123456"
}).encode("utf-8")
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/38.0.2125.122 Safari/573.36 SE 2.X '
                             'MetaSr 1.0')
data = urllib.request.urlopen(req).read()
fhandle = open("d:/python/1.html","wb")
fhandle.write(data)
fhandle.close()
url2 = "http://bbs.chinaunix.net"
req2= urllib.request.Request(url2)
req2.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/38.0.2125.122 Safari/573.36 SE 2.X '
                             'MetaSr 1.0')
data2 = urllib.request.urlopen(req2).read()
fhandle = open("d:/python/2.html", "wb")
fhandle.write(data2)
fhandle.close()

