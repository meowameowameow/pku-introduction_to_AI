import os
import csv
import re
#用于改变字幕文件的格式
#1
# newfile=open(r'newww.txt','w',encoding='utf-8')
# myi=0
# with open('new.txt','r',encoding='utf-8')as lines:
#     for line in lines:
#         if myi%2==0:
#             tmp=line.strip()+'|'
#             newfile.write(tmp)
#         else:
#             tmp=line.strip()+'\n'
#             newfile.write(tmp)
#         myi+=1
# newfile.close()
# newfile=open(r'new.txt','w',encoding='utf-8')
#
# with open('POS.txt','r',encoding='utf-8') as lines:
#     for line in lines:
#         tmp=re.sub(r'/[a-z]*\s','',line)
#         newfile.write(tmp)
#         #print(tmp)
# newfile.close()

#2
# newfile=open(r't2new.txt','w',encoding='utf-8')
# myi=0
# with open('t2.txt','r',encoding='utf-8')as lines:
#     for line in lines:
#         if myi%2==0:
#             tmp = re.sub(r'#\d', '', line)
#             newfile.write(tmp)
#         myi+=1
# newfile.close()

#3
# newfile=open(r'new.txt','w',encoding='utf-8')
#
# with open('POS.txt','r',encoding='utf-8') as lines:
#     for line in lines:
#         tmp=re.sub(r'/[a-z]*\s','',line)
#         newfile.write(tmp)
#         #print(tmp)
# newfile.close()