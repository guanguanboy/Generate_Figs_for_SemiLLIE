import os
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio as psnr

# 输入文件夹路径和输出文件夹路径
input_folder = r'E:\科研项目\无监督的低光增强\对比方法实验结果\MambaIR\ValSet_MambaIR\LRSW\ValSet_LRSW\ValSet'   # 替换为包含 PNG 图像的文件夹路径
output_folder = r'E:\科研项目\无监督的低光增强\对比方法实验结果\MambaIR\ValSet_MambaIR\LRSW\ValSet_LRSW\ValSet_LRSW_jpg' # 替换为保存 JPG 图像的文件夹路径

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    if filename.endswith('.png'):
        # 构建完整的文件路径
        if filename.endswith('_gt.png'):
            continue
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')

        # 打开 PNG 图像并转换为 RGB 模式（JPEG 不支持透明度）
        with Image.open(input_path) as img:
            rgb_img = img.convert('RGB')
            # 保存为 JPG 格式
            rgb_img.save(output_path, 'JPEG')

        print(f'已将 {filename} 转换为 JPG 并保存到 {output_path}')
