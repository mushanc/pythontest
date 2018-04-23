import urllib.request
import urllib.error

try:
    urllib.request.urlopen("http://110.53.30.87:8123")
except urllib.error.URLError as e:
 #   print(e.code)
    print(e.reason)