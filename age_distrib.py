import matplotlib.pyplot as plt

#設定字體:微軟正黑
plt.rcParams["font.family"] = "Microsoft JhengHei"

age_list = ["20~24歲","25~29歲","30~34歲",
               "35~39歲","40~44歲","45~49歲"]
pct_list = [8.27,8.28,8.44,9.98,9.08,8.86]

# plt.bar(hei_list, pct_list)
# plt.title("台灣23歲男性身高分布", fontsize = 16)


fig, ax = plt.subplots()
bar_container = ax.bar(age_list, pct_list, color ="turquoise", width = 0.6)
ax.set(ylabel="百分比", title = "該年齡層在全體男性占比")
ax.bar_label(bar_container)



plt.show

plt.savefig("該年齡層在全體男性占比.jpg", dpi =300, facecolor = "#EEEEEE")