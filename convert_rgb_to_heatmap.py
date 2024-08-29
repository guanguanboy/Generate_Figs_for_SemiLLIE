import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取RGB图像
image_path = 'images/figure3/0000244_05900_d_0000013.jpg'  # 替换为图片的实际路径
image = cv2.imread(image_path)

# 确保图片读取成功
if image is None:
    print("Error: Unable to load image.")
else:
    # 将RGB图像转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 将灰度图像转换为热度图（使用Matplotlib colormap）
    heatmap_image = plt.get_cmap('hot')(gray_image / 255.0)  # 归一化并应用热度图色彩映射
    heatmap_image = (heatmap_image[:, :, :3] * 255).astype(np.uint8)  # 去掉alpha通道并转换为8位图像
    
    # 显示热度图
    plt.imshow(heatmap_image)
    plt.axis('off')  # 关闭坐标轴
    plt.show()
    
    # 保存热度图
    output_path = 'images/figure3/0000244_05900_d_0000013_heatmap.jpg'  # 替换为保存图片的路径
    cv2.imwrite(output_path, cv2.cvtColor(heatmap_image, cv2.COLOR_RGB2BGR))
