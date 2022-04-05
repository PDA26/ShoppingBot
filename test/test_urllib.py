import urllib.request as r
import urllib.parse

# #post
# data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding = 'utf')
# response = r.urlopen("http://httpbin.org/post", data = data)
# print(response.read().decode('utf'))

# #get
# try:
#     response = r.urlopen("http://httpbin.org/get", timeout = 3)
#     print(response.read().decode('utf'))
# except urllib.error.URLError:
#     print("time out!")


# response = r.urlopen("http://www.baidu.com")
# print(response.getheader('Server'))


headers = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29"
}

url = "https://www.douban.com"
#url = "http://httpbin.org/post"
data = bytes(urllib.parse.urlencode({"cnm" : "nmb"}), encoding = 'utf')
req = r.Request(url = url, data = data, headers = headers, method = "POST")
request = r.urlopen(req)
print(request.read().decode('utf'))