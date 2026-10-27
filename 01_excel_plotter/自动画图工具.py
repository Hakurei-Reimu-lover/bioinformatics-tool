import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#matplib的自带无中文。这个把中文加入
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
#把数据载入
road = input("请输入文件路径(excel)：")
df = pd.read_excel(road)
#要做数据的清洗
#绘制图像，kind是图像的类别，marker是数据点的标记
x1 = input("请输入x轴数据：")
y1 = input("请输入y轴数据：")
title1 = input("请输入标题：")
tu = df.plot(y=y1, x=x1, kind="line", marker="o", color="blue")
#处理图的各种数据
plt.xlabel(x1)
plt.ylabel(y1)
plt.title(title1)
#给图添加数据点的标记
for x, y in zip(df[x1], df[y1]):
    label = f'({x}, {y:.3f})'   # 日期格式化成字符串
    tu.annotate(label, xy=(x, y), xytext=(0, 8),
                textcoords='offset points', ha='center', fontsize=9)
#这个可以保存图片到指定路径，dpi是图片的分辨率
try:
   road_save = input("请输入保存图片名称：")
   folder = input("请输入保存图片文件夹：")
   plt.savefig(f"{folder}/{road_save}.png", dpi=300)
   print("保存成功")
except Exception as e:
   print("保存失败，请重新运行输入，错误为：", e)
plt.show()