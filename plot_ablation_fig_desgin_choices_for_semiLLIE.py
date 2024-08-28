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

region_psnr_lolv2_real =  [
20.66,
21.56,
22.05,
22.02#36.28 23.62
]


region_psnr_lolv2_synthetic = [
24.65,
24.99,
25.92,
25.80
#36.30
]


region_psnr_sid =  [
22.87,
23.08,
23.91,
23.76
#38.20
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

width_psnr_lolv2_real =  [
20.15,
21.18,
22.05,
#36.30,
21.94]


width_psnr_lolv2_synthetic = [
24.85,
25.29,
25.92,
#36.38,
25.29
]


width_psnr_sid =  [
22.07,
22.95,
23.91,
#38.50,
23.47]


mssg_sample_step = ['1', '2', '4','6']
#psnr_list = [38.1896, 38.2811, 38.2303, 38.7380, 38.3344, 38.2442]

mssg_fid_visdrone = [
52.05,
36.49,
38.97,
40.06
]

sam_psnr_lolv2_real =  [
21.48,
21.87,
22.05,
#36.30
]


sam_psnr_lolv2_synthetic = [
25.26,
25.59,
25.92
#36.38,
]


sam_psnr_sid =  [
23.40,
23.65,
23.91
#38.50
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



# 在第三个子图上绘制数据并设置标签
line31, = axs[1].plot(mssg_sample_step, mssg_fid_visdrone, marker = '*', color=custom_blue, label=r'Visdrone', linestyle=line_style)
#line32, = axs[1].plot(sam_sample_step, sam_psnr_lolv2_real, marker = 'o', color=custom_green, label=r"LSRW", linestyle=line_style)

#axs[2].set_title('子图3')
#axs[2].set_ylabel('PSNR (dB)', font2)  
axs[1].set_xlabel('Number of MSSGs', font2)


# 在第二个子图上绘制数据并设置标签
line21, = axs[2].plot(mssb_sample_step, mssb_fid_visdrone, marker = 'o', color=custom_blue, label=r'Visdrone', linestyle=line_style)
#line22, = axs[2].plot(region_sample_step, region_psnr_lolv2_real, marker = 'o', color=custom_green, label=r"LSRW", linestyle=line_style)

#axs[1].set_title('子图2')
#axs[1].set_ylabel('PSNR (dB)', font2)  
axs[2].set_xlabel('Number of MSSBs', font2)   

# 将刻度标签显示在所有子图中
for ax in axs.flat:
    ax.tick_params(axis='y', labelleft=True)
    
# 为整个图表生成统一的图例
fig.legend(handles=[line11], loc='upper center', ncol=4,fontsize=16)

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
plt.savefig('./images/ablation_design_final.png',bbox_inches='tight') #指定分辨率保存

# 显示图像
plt.show(block=True)