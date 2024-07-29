import matplotlib.pyplot as plt
 
# 示例数据
x = range(10)
y1 = [i**2 for i in x]
y2 = [i**1.5 for i in x]
 
fig, ax1 = plt.subplots()
 
# 绘制第一个纵坐标
ax1.plot(x, y1, label='y = x^2')
ax1.set_xlabel('X axis')
ax1.set_ylabel('FID')
ax1.legend(loc='best')
 
# 创建第二个纵坐标
ax2 = ax1.twinx()
# 绘制第二个纵坐标
ax2.plot(x, y2, color='red', label='y = x^1.5')
ax2.set_ylabel('PSNR')
ax2.legend(loc='best')
 
plt.show()