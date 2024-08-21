import matplotlib.pyplot as plt

#設定字體:微軟正黑
plt.rcParams["font.family"] = "Microsoft JhengHei"

acde_degree_list = ["高中以上","大專以上","大學以上",
               "碩士以上","博士以上"]
pct_list = [87.1, 50.89, 40.38, 9.91, 0.61]

# plt.bar(hei_list, pct_list)
# plt.title("台灣23歲男性身高分布", fontsize = 16)


fig, ax = plt.subplots()
bar_container = ax.bar(acde_degree_list, pct_list, color ="lightsalmon", width = 0.6)
ax.set(ylabel="百分比", title = "該學歷以上在全體男性占比")
ax.bar_label(bar_container)



plt.show

plt.savefig("該學歷以上在全體男性占比.jpg", dpi =300, facecolor = "#EEEEEE")