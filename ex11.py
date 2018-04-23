import re
pattern= "\n"
string = '''http://www.baidu.com
jo345python234
http://www.iqiyuan.com'''
result =  re.search ('\n', string)
print(result)

p = '\w\d\python\w'
s = ''
result = re.search(p, string )
print(result)