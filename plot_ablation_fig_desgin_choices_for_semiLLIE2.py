import matplotlib

import matplotlib.pyplot as plt

# 准备数据
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
matplotlib.rcParams['text.usetex'] = True

mssb_sample_step = ['1', '2', '3','4']
#psnr_list = [38.1896, 38.2811, 38.2303, 38.7380, 38.3344, 38.2442]

mssb_fid_visdrone = [
49.36,
36.49,
37.79,
39.87#32.00
]

mssb_fid_LSRW = [
18.65,
19.73,
19.58,
19.54
#36.30
]



width_sample_step = ['16', '32', '64','96']
#psnr_list = [38.1896, 38.2811, 38.2303, 38.7380, 38.3344, 38.2442]

width_fid_visdrone = [
56.66,
48.84,
36.49,
#32.06,
40.06
]

#2.32
width_psnr_LSRW =  [
17.83,
18.86,
19.73, ##22.05,
#36.30,
19.62]



mssg_sample_step = ['1', '2', '4','6']
#psnr_list = [38.1896, 38.2811, 38.2303, 38.7380, 38.3344, 38.2442]

mssg_fid_visdrone = [
52.05,
36.49,
38.97,
40.06
]

#2.14
mssg_psnr_LSRW =  [
19.34,
19.73,
19.48,
19.46
]


# 设置虚线样式
line_style = '--'

custom_green = '#2B9F2B'
custom_red = '#D62728'
custom_blue = '#1571B1'
custom_orange = '#FF7E0D'

custom_light_blue = '#E6E6FF'


# 设置题目与坐标轴名称  
font2 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}

# 创建包含一行三列的图表
fig, axs = plt.subplots(1, 3, figsize=(12, 4), sharey=True)

# 在第一个子图上绘制数据并设置标签
line11, = axs[0].plot(width_sample_step, width_fid_visdrone, marker = 'o', color=custom_blue, label=r'Visdrone', linestyle=line_style)
#line12, = axs[0].plot(width_sample_step, width_psnr_lolv2_real, marker = 'o', color=custom_green, label=r"LSRW", linestyle=line_style)

#axs[0].set_title('子图1')
axs[0].set_ylabel('FID', font2)  
axs[0].set_xlabel('Feature Width', font2)  


# 创建一个共享x轴但独立y轴的第二个坐标轴
axs0_twin = axs[0].twinx()  # 注意这里使用了twinx()
line12, = axs0_twin.plot(width_sample_step, width_psnr_LSRW, marker = 'o', color=custom_green, label=r"LSRW", linestyle=line_style)

# 在第三个子图上绘制数据并设置标签
line31, = axs[1].plot(mssg_sample_step, mssg_fid_visdrone, marker = 'o', color=custom_blue, label=r'Visdrone', linestyle=line_style)


axs1_twin = axs[1].twinx()  # 注意这里使用了twinx()
line32, = axs1_twin.plot(mssg_sample_step, mssg_psnr_LSRW, marker = 'o', color=custom_green, label=r"LSRW", linestyle=line_style)

#axs[2].set_title('子图3')
#axs[2].set_ylabel('PSNR (dB)', font2)  
axs[1].set_xlabel('Number of MSSGs', font2)


# 在第二个子图上绘制数据并设置标签
line21, = axs[2].plot(mssb_sample_step, mssb_fid_visdrone, marker = 'o', color=custom_blue, label=r'Visdrone', linestyle=line_style)
#line22, = axs[2].plot(region_sample_step, region_psnr_lolv2_real, marker = 'o', color=custom_green, label=r"LSRW", linestyle=line_style)

axs2_twin = axs[2].twinx() 
line22, = axs2_twin.plot(mssb_sample_step, mssb_fid_LSRW, marker = 'o', color=custom_green, label=r"LSRW", linestyle=line_style)


axs2_twin.set_ylabel('PSNR (dB)', font2)  # 设置第二个y轴的标签

#axs[1].set_title('子图2')
#axs[1].set_ylabel('PSNR (dB)', font2)  
axs[2].set_xlabel('Number of MSSBs', font2)   
#axs[2].set_ylabel('PSNR (dB)', font2)  


# 将刻度标签显示在所有子图中
for ax in axs.flat:
    ax.tick_params(axis='y', labelleft=True)
    
# 为整个图表生成统一的图例
fig.legend(handles=[line11,line12], loc='upper center', ncol=4,fontsize=16)

# 调整子图之间的间距
plt.tight_layout()

# 调整子图与上边界的距离
plt.subplots_adjust(top=0.85)

#plt.ylabel('PSNR (dB)', font2)  
#plt.xlabel('Sampling Steps', font2) 
#plt.legend(loc = "best", fontsize=16)#图例

#plt.gcf().set_facecolor(np.ones(3)* 255 / 255)   # 生成画布的大小
#plt.grid()  # 生成网格
#plt.xticks(size=13)
#plt.yticks(size=13)
plt.savefig('./images/ablation_design_final2.png',bbox_inches='tight') #指定分辨率保存

# 显示图像
plt.show(block=True)