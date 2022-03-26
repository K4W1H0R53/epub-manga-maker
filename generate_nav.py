import os
import sys

root = sys.path[0]

contents = []
landmark = []
count = 0   # 计数器

with open(root+"\\contents.txt",'r',encoding='UTF-8-sig') as f:
    contents_table= f.read().splitlines()

for i in contents_table:
    print(i.split('|',1)[0])

# command= input("是否含有目录/目录是否和封面在同一页(y/n):")
# if command == "y":
#     count=+1
#     contents.append("表紙 && 目次")
#     print("添加章节: 表紙 && 目次","当前章节数:",count)