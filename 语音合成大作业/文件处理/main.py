import os
import csv
import re
#将txt文件存入csv文件
newfile=open(r'metadata.csv','w',encoding='utf-8',newline='')
writer=csv.writer(newfile,delimiter='|')
#writer.writerow(["id","transcription","normalized_transcription"])
with open('data.txt','r',encoding='utf-8')as lines:
    for line in lines:
        list=line.strip().split('|')
        writer.writerow(list)
newfile.close()







