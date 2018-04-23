import urllib.request
import urllib.parse
import string

def tieba(url,begin,end):
    for i in range(begin,end+1):
        sName = 'd:/python/' + str(i).zfill(5) + '.html'
        print('正在下载' + str(i)+'个页面'+sName)
        m = urllib.request.urlopen(url+str(i)).read()
        with open(sName, 'wb') as file:
            file.write(m)
        file.close()
if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/'
    begin = 1
    end = 3
    tieba(url,begin,end)