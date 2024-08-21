import matplotlib.pyplot as plt

#設定字體:微軟正黑
plt.rcParams["font.family"] = "Microsoft JhengHei"

marriage_list = ["未婚,含離婚與喪偶","已婚",]
pct_list = [59.85,40.15]


plt.pie(pct_list, labels = marriage_list,
        autopct = "%.2f%%", #設定顯示每塊的小數點
        textprops={'fontsize': 14}) #設定字體大小
plt.title("20~49歲男性婚姻關係調查", fontsize = 16)
plt.show
plt.savefig("20~49歲男性婚姻關係調查.jpg", dpi =300, facecolor = "#EEEEEE")
