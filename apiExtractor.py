import re 
import requests
import sys

from urllib.parse import urlparse
source = sys.argv[1]

if 'http' in sys.argv[1]:
    headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\"", "Accept": "application/json, text/plain, */*", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://new-m.pay.naver.com/historybenefit/paymenthistory", "Accept-Encoding": "gzip, deflate", "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
    c = requests.get(source, headers=headers).content
    c = c.decode('utf-8')
    path = urlparse(sys.argv[1]).path
    path = path[1:].split('?')[0]
    path = path.replace('/','--')
    f = open('dummy/'+path,'w',encoding='utf-8')
    f.write(c)
    f.close()
    
    
else:
    f = open('test.js','r')
    c = f.read()
    f.close()

regex = r"(\/[A-z-0-9.]{2,17})\/[A-z0-9-\?=\/]*"
regex = re.compile(regex)
mo  = regex.search(c)
#print(mo)
index = 0
#print(mo.group())
#print(mo.span())

result = ''
while True:
    try:
        mo = regex.search(c,index)
        index = mo.span()[1]
        result+=mo.group()+'\n'
        print(mo.group())
    except Exception as e:
 #       print(e)
        break

f = open('result2.txt','w')
f.write(result)
f.close()

#for r in result:
 #   print(r)