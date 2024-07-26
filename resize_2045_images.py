import os
from PIL import Image

# 设置源文件夹和目标文件夹路径
source_folder = 'images/LSRW2045'
target_folder = 'images/LSRW2045_Resized'

# 定义支持的图像格式
supported_formats = ('.png', '.jpg', '.jpeg')

# 如果目标文件夹不存在，创建目标文件夹
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 遍历源文件夹下的所有文件
for filename in os.listdir(source_folder):
    # 检查文件是否为PNG图像
    if filename.endswith(supported_formats):
        # 构建图像的完整路径
        img_path = os.path.join(source_folder, filename)
        # 打开图像
        img = Image.open(img_path)
        
        # 获取图像的宽度和高度
        width, _ = img.size
        
        # 设置新的高度
        new_height = 534
        
        # 调整图像大小
        resized_img = img.resize((width, new_height), Image.ANTIALIAS)
        
        # 保存调整大小后的图像到目标文件夹
        resized_img.save(os.path.join(target_folder, filename))

print("Image resizing completed.")
