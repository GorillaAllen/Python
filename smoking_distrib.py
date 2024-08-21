import matplotlib.pyplot as plt

#設定字體:微軟正黑
plt.rcParams["font.family"] = "Microsoft JhengHei"

smoking_frq_list = ["不抽菸","有在抽菸"]
smoking_pct_list = [76.6,23.4]


plt.pie(smoking_pct_list, labels = smoking_frq_list,
        autopct = "%.2f%%", #設定顯示每塊的小數點
        textprops={'fontsize': 14}) #設定字體大小
plt.title("男性吸菸人口統計", fontsize = 16)
plt.show
plt.savefig("男性吸菸人口統計.jpg", dpi =200, facecolor = "#EEEEEE")