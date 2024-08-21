import matplotlib.pyplot as plt

#設定字體:微軟正黑
plt.rcParams["font.family"] = "Microsoft JhengHei"

hei_list = ["164","166","167","168","169","170","171","172",
            "173","174","175","176","177","178","179","181"]
pct_list = [95,90,85,80,
        75,70,62.5,55,47.5,
        40,32.5,25,20,15,
        10,5]

# plt.bar(hei_list, pct_list)
# plt.title("台灣23歲男性身高分布", fontsize = 16)


fig, ax = plt.subplots()
bar_container = ax.bar(hei_list, pct_list)
ax.set(ylabel="百分比", title = "該身高以上之男性占比")
ax.bar_label(bar_container)


plt.show

plt.savefig("台灣男性身高分布.jpg", dpi =300, facecolor = "#EEEEEE")