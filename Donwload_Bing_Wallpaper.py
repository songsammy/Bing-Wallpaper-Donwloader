import requests
from bs4 import BeautifulSoup
import time
r = requests.get('https://cn.bing.com/')
soup = BeautifulSoup(r.content,"html5lib")
imgurl = ("https://cn.bing.com/"+(str(soup.link).split("/")[1]).split('"')[0])
imgtitle=((imgurl.split(".")[3]).split("_")[0])
name=(time.strftime("%Y%m%d", time.localtime())+"_"+imgtitle+".jpg")
print(imgurl)
p = requests.get(imgurl)
with open(name, 'wb') as f:
    f.write(p.content)                      
