def use_proxy(proxy_addr, url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener =urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data

proxy_addr = "180.104.223.18:8118"

data = use_proxy(proxy_addr, "http://www.baidu.com")
print(len(data))