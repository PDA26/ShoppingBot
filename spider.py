# coding = utf-8
import urllib.error

from bs4 import BeautifulSoup
import re
import sqlite3
import urllib.request as r



pat_link = re.compile(r'href="(.*?)"')

def getData(url):
    res = []
    for i in range(0, 10):
        curr = url + str(i * 25)
        html = askURL(curr)
        #print(html)
        soup = BeautifulSoup(html, "html.parser")


    return res

#get info of one url
def askURL(url):
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29'
    }
    request = r.Request(url= url, headers=head)
    html = ""
    try:
        response = r.urlopen(request, timeout= 5)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(e)
    return html


if __name__ == "__main__":
    html = askURL('http://bbs.hupu.com')
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="t-info"):
        item = str(item)
        #print(item)
        link = re.findall(pat_link, item)
        print(link[0])