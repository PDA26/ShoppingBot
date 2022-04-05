import re

from bs4 import BeautifulSoup
file = open('./baidu.html', 'rb')
html = file.read()
bs = BeautifulSoup(html, 'html.parser')


##tag
#print(bs.title)
#print(bs.head)

# #NavigableString
# print(type(bs.title.string))

# #BeautifulSoup
# print(type(bs))



#traversal
#print(bs.head.contents[0])

#search
# find_all()
t_list = bs.find_all('a')
print(t_list)

#regex  search()
t_list = bs.find_all(re.compile('a'))
print(t_list)
