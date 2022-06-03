#!/user/bin/env python
# _*_coding:utf-8_*_
from pydub import AudioSegment
import re
num=1
def is_Chinese(ch):
    if '\u4e00' <= ch <= '\u9fff' or 'a'<=ch<='z' or 'A'<=ch<='Z':
            return True
    return False
with open("file1.txt",'r',encoding='utf-8') as f: #打开歌词文件
    time_list = []
    lyric_list = []
    #循环获取每一句歌词时间戳，
    k=0
    while True:
      line = f.readline()
        if not line:
            break
        if(k%4==0 or k%4==3):
            k=k+1
            continue
        if(k%4==2):
            k=k+1
            lyric_list.append(line)
            continue

        line = line.strip('\n')
        time_list.append(line.split(' --> ')[0])
        time_list.append(line.split(' --> ')[1])
        k=k+1

print(len(time_list))
print(len(lyric_list))

with open('file1.txt','w+') as f: #截取音频名称与歌词保存位置
    cout = 0
    for i,j in zip(range(int(len(time_list)/2)),lyric_list):
        cout += 1
        start_time = time_list[i*2]  # 获取开始截取时间戳

        if i < len(time_list) - 1:

            stop_time = time_list[i*2 + 1]  # 获取结束时间戳

            file_name = "file1.wav"  # 歌曲保存路径

            sound = AudioSegment.from_wav(file_name)
            
            start_time=60000*float(start_time.split(':')[1]) + float(start_time.split(':')[2].split(',')[0])*1000+float(start_time.split(':')[2].split(',')[1])
            stop_time = 60000 * float(stop_time.split(':')[1]) + float(stop_time.split(':')[2].split(',')[0])*1000+float(stop_time.split(':')[2].split(',')[1])
            #print("ms:", start_time, "~", stop_time)  # 打印 开始时间与结束时间

#################################
            word = sound[start_time:stop_time]  # 截取
            f.write(str(num)+"_{}.wav".format(cout)+'|'+j.replace(' ',',')[:-1]+"。\n") #截取的音频名字与对应歌打印

            word.export('file_{}.wav'.format(cout), format="wav",  # 保存位置
                       tags={'artist': 'AppLeU0', 'album': cout})
            ############################################
            i=i+1


