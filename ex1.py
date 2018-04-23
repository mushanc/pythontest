import urllib.request

for i in range(1,100):
    try:
        file = urllib.request.urlopen("http://yum.iqianyue.xom", timeout= 0.5)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->", e)
