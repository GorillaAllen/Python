import matplotlib.pyplot as plt

#設定字體:微軟正黑
plt.rcParams["font.family"] = "Microsoft JhengHei"

drink_frq_list = ["幾乎無飲酒","小酌","暴飲"]
age_list = ["18-29歲","30-39歲", "40-49歲"]
total_pct_list = [0.7014,0.1938,0.1048]


plt.pie(total_pct_list, labels = drink_frq_list,
        autopct = "%.2f%%", #設定顯示每塊的小數點
        textprops={'fontsize': 14}) #設定字體大小
plt.title("18歲~49歲男性人口過去一個月飲酒調查", fontsize = 16)
plt.show
plt.savefig("18歲~49歲男性人口過去一個月飲酒調查.jpg", dpi =300, facecolor = "#EEEEEE")
