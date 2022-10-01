import urllib.request
import random
import re
import pykakasi
from pykakasi import kakasi

kakasi = kakasi()
kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')
conv = kakasi.getConverter()

# 偽裝瀏覽器
x=str(input("輸入動畫季度:"))
url="https://acgsecrets.hk/bangumi/"+x+"/"
# 模擬請求頭
# 完整請求頭
headers={
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"
}
# 設置一個請求器
req=urllib.request.Request(url,headers=headers)
# 發起請求
response=urllib.request.urlopen(req)
da=response.read().decode("utf-8")
# 讀取一行
# da=response.readline()
re_d=re.compile(r'<div class="anime_info anime_names site-content-float"><h3 class="entity_localized_name">(.*?)</h3><div class="notranslate entity_original_name">')
reo=re.compile(r'</div><div class="notranslate entity_original_name">(.*?)</div></div><div class="anime_specs"><div class="anime_tag">')
finCT=re_d.findall(da)
print(finCT)

fo=reo.findall(da)

foJE=[]
for i in range(len(fo)):
    fo0=conv.do(fo[i])
    foJE.insert(i,fo0)
print(foJE)

print(finCT)
finCTJE=[]
for j in range(len(finCT)):
    f=finCT[j]+"_"+fo[j]+"_"+foJE[j]
    finCTJE.insert(j,f)
print(type(finCTJE))

z="\n".join(fo)
Flist=finCTJE

SEC=str(input("是否建立整合TXT檔(Y/N):"))

if SEC == "Y":
    FCTJE=open(r'y:\\DATA\\python\\ANIMSQL\\'+x+'.txt',"wb")
    FCTJE.write("\n".join(finCTJE).encode())#lis轉字串並寫入
    FCTJE.write("".join("\nend").encode())#lis轉字串並寫入
    FCTJE.close()
    print("執行結束")
else:
    print("執行結束")


z0=conv.do(z)

# 中日羅整合，next gui列表