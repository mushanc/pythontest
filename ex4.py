import urllib.request
import urllib.parse
import string
import re
import os
import urllib.error

def tieba(url, begin, end ):
    count = 1
    for i in range(begin, end ):
        sName = 'd:/python/' + str(i).zfill(5) +'.html'
        print ('正在下载'+ str(i) + '个页面，并保存为' +sName)
        m = urllib.request.urlopen(url +str(i)).read()
        dirpath = 'd:/python/'
        dirname = str(i)
        new_path = os.path.join(dirpath, dirname)
        if not os.path.isdir(new_path):
            os.makedirs(new_path)
#            f = open('d:/python/' + str(i) + '/' + str(i) + '.html', 'wb')
#           f.write(m)
#          f.close()
        page_data = m.decode('utf-8','replace')
        page_image = re.compile('<img src=\"(.+?)\"')
        print(page_image.findall(page_data))
        for image in page_image.findall(page_data):
            pattern = re.compile(r'^https://.*.png$')
            if pattern.match(image):
                try:
                    image_data = urllib.request.urlopen(image).read()
                    image_path = dirpath+ dirname + '/'+ str(count) + '.png'
                    count +=1
                    print(image_path)
                    with open(image_path, 'wb') as image_file:
                        image_file.write(image_data)
                    image_file.close()
                except urllib.error.URLError as e:
                    print('Download failed')
        with open(sName,'wb') as file:
            file.write(m)
        file.close()

if __name__ == "__main__":
    url = "https://tieba.baidu.com/p/"
    begin =2
    end = 7
    tieba(url,begin,end )