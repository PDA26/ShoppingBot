# coding = utf-8
import urllib.error

from bs4 import BeautifulSoup
import re
import sqlite3
import urllib.request as r

def getData(url):
    res = []
    for i in range(0, 10):
        url = url + str(i * 25)
        res += (askURL(url))

    return res

#get info of one url
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29"
    }
    request = r.Request(url= url, headers=head)
    html = ""
    try:
        response = r.urlopen(request)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html









if __name__ == "__main__":
    ttl = getData('http://movie.douban.com/top250?start=')