import matplotlib.pyplot as plt
import numpy as np

# 创建一些数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)  # 第一组数据
y2 = np.cos(x)  # 第二组数据

# 创建一个图形和坐标轴
fig, ax1 = plt.subplots()

# 绘制第一组数据
color = 'tab:red'
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)', color=color)
ax1.plot(x, y1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# 创建一个共享x轴但独立y轴的第二个坐标轴
ax2 = ax1.twinx()  # 注意这里使用了twinx()

# 绘制第二组数据
color = 'tab:blue'
ax2.set_ylabel('cos(x)', color=color)  # 设置第二个y轴的标签
ax2.plot(x, y2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# 显示图形
fig.tight_layout()  # 自动调整子图参数, 使之填充整个图像区域
plt.show()