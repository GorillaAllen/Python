import matplotlib.pyplot as plt

#設定字體:微軟正黑
plt.rcParams["font.family"] = "Microsoft JhengHei"

bmi_level_list = ["過輕","正常","過重","肥胖"]
total_pct_list = [0.0329, 0.401, 0.297, 0.2692]


plt.pie(total_pct_list, labels = bmi_level_list,
        autopct = "%.2f%%", #設定顯示每塊的小數點
        textprops={'fontsize': 14}) #設定字體大小
plt.title("民國105-108年台灣男性體位分布", fontsize = 16)
plt.show
plt.savefig("民國105-108年台灣男性體位分布.jpg", dpi =300, facecolor = "#EEEEEE")
