import urllib.request,gzip,re,http.cookiejar,urllib.parse
import sys

def ungzip(data):
    try:
        print('loading......')
        data = gzip.decompress(data)
        print('gzip is successing!')
    except:
        print("gzip fail")
    return data