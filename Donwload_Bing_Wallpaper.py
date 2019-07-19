import requests
from bs4 import BeautifulSoup
import time
import os
from os import path
ph=(path.dirname(__file__))
r = requests.get('https://cn.bing.com/')
soup = BeautifulSoup(r.content,"html5lib")
imgurl = ("https://cn.bing.com/"+(str(soup.link).split("/")[1]).split('"')[0])
imgtitle=((imgurl.split(".")[3]).split("_")[0])
name=ph+"\\"+(time.strftime("%Y%m%d", time.localtime())+"_"+imgtitle+".jpg")
print(name)
p = requests.get(imgurl)
with open(name, 'wb') as f:
	f.write(p.content) 
r = requests.get('https://cn.bing.com/?FORM=BEHPTB&ensearch=1')
soup = BeautifulSoup(r.content,"html5lib")
imgurl = ("https://cn.bing.com/"+(str(soup.link).split("/")[1]).split('"')[0])
imgtitle=((imgurl.split(".")[3]).split("_")[0])
name=ph+"\\"+(time.strftime("%Y%m%d", time.localtime())+"_"+imgtitle+".jpg")
print(name)
p = requests.get(imgurl)
with open(name, 'wb') as f:
	f.write(p.content) 
