import os
from PIL import Image

# 输入文件夹路径和输出文件夹路径
input_folder = r'E:\科研项目\无监督的低光增强\对比方法实验结果\RetinexNet\visdrone_unlabeld_test_RetinexNet\visdrone_unlabeld_test'   # 替换为包含以 fake_B.png 结尾的图像的文件夹路径
output_folder = r'E:\科研项目\无监督的低光增强\对比方法实验结果\RetinexNet\visdrone_unlabeld_test_RetinexNet\visdrone_unlabeld_test_jpg'  # 替换为保存 JPG 图像的文件夹路径

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('_S.jpg'):
        # 构建完整的文件路径
        input_path = os.path.join(input_folder, filename)
        
        # 去掉文件名中的 'fake_B' 并转换为 jpg 格式
        new_filename = filename.replace('_S.jpg', '') + '.jpg'
        output_path = os.path.join(output_folder, new_filename)

        # 打开 PNG 图像并转换为 RGB 模式（JPEG 不支持透明度）
        with Image.open(input_path) as img:
            rgb_img = img.convert('RGB')
            # 保存为 JPG 格式
            rgb_img.save(output_path, 'JPEG')

        print(f'已将 {filename} 转换为 {new_filename} 并保存到 {output_path}')
