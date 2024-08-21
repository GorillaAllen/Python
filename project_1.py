import csv
#此程式目的為把資料整合成不分行政區之資料. 新的[]需要被建立以便輸出成新的csv

with open(r"D:\PY專案\106人口資料-婚姻,年齡,學歷.csv", encoding = "utf8") as data:
    readfile = csv.reader(data)
    oldfile = list(readfile)

#打造[]並放進欄位名
newdata=[]
newdata.append(oldfile[0])

#因原始資料以行政區區分,此段程式把資料整合成不分行政區之資料
age_list = ["15 ~ 19 歲", "20 ~ 24 歲", "25 ~ 29 歲", #為了下方段落搜尋索引而打造
"30 ~ 34 歲","35 ~ 39 歲","40 ~ 44 歲","45 ~ 49 歲",
"50 ~ 54 歲","55 ~ 59 歲","60 ~ 64 歲","65 ~ 69 歲",
"70 ~ 74 歲","75 ~ 79 歲","80 ~ 84 歲","85 ~ 89 歲",
"90 ~ 94 歲","95 ~ 99 歲","100歲以上"]

for k in range(len(age_list)): 
    newline=[] #新建一個[]以便後面append進newdata
    newline.append(age_list[k]) #加入欄位名稱
    newline = newline + [0 for i in range(29)] #使newline成為有30個元素的list.除了欄位,其餘為0
    for i in range(1, len(oldfile) ):
        if oldfile[i][0] == age_list[k]: #以欄位名稱為搜索依據
            for j in range(1,30): 
                newline[j] += int(oldfile[i][j]) #找到符合的行,將需要的值加入newline
    newdata.append(newline)
    
#此段為確認上方加總正確用
# sum = 0
# for i in range(1,19):
#     sum = sum + newdata[i][1]
# print(sum)
    

# print(newdata)

with open(r"D:\PY專案\arranged_2017_survey.csv", "w", newline="", encoding = "utf8") as writerdata:
    wf = csv.writer(writerdata)
    for row in newdata:
        wf.writerow(row)

    
 