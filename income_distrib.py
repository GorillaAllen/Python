import matplotlib.pyplot as plt

#設定字體:微軟正黑
plt.rcParams["font.family"] = "Microsoft JhengHei"

income_list = ["31.9萬","37.1萬","42.8萬",
               "48.3萬","55.7萬","64.8萬",
               "78.5萬","100.7萬","136.8萬"]
pct_list = [90,80,70,60,50,
            40,30,20,10]

fig, ax = plt.subplots()
bar_container = ax.bar(income_list, pct_list, color ="#73ced0")
ax.set(ylabel="百分比", title = "該收入以上之男性占比")
ax.bar_label(bar_container)

plt.show

plt.savefig("台灣男性收入分布.jpg", dpi =300, facecolor = "#EEEEEE")