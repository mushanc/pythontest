import re
string = "rrapythondadapython_jdskpythonflawej234python23234"
pattern = ".python."
result1 = re.match(pattern, string)
result2 = re.search(pattern, string ).span()
print(result1)
print(result2)

pattern2 = re.compile(".python.")
result3 = pattern2.findall(string)
print(result3)

result4 = re.sub(pattern,"php", string )
result5 = re.sub(pattern, "feed", string, 2)
print(result4)
print(result5)

p = "[a-zA-z]+://[\S]*[.com|.cn]"
string = "<a href= 'http://www.baidu.com'>百度首页</a>"
r = re.search(p, string)
print(r)

p = "(0\d{2}|0\d{3})-\d{8}"
string = "02340043503040571-9028535670345"
r = re.search(p, string )
print(r)

p= "\w+([.+-]\w+)*@\w+([.+-]\w+)*\.\w+([.+-]\w+)*"
string = "daflirw240_3galjg2@saf.comafjajf"
r= re.search(p, string)
print(r)