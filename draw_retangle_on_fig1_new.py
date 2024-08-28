from PIL import Image

from PIL import Image, ImageDraw,ImageOps
import os

def draw_rectangle(image, bbox, color=(255, 0, 0), width=24):
    # 创建ImageDraw对象
    draw = ImageDraw.Draw(image)
    
    # 绘制矩形框
    for i in range(width):
        adjusted_bbox = (bbox[0] + i, bbox[1] + i, bbox[2] - i, bbox[3] - i)
        draw.rectangle(adjusted_bbox, outline=color)

def save_image(image_folder_name, image_name, location=[0, 0], color=(0, 255, 0), border_width=16):

    # 创建输出文件夹
    output_father_folder_path = os.path.join('images', image_folder_name + '_output_new2')
    if not os.path.exists(output_father_folder_path):
        os.mkdir(output_father_folder_path)
    output_folder_path = os.path.join(output_father_folder_path, image_name)
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)

    # 打开图片
    origin_img_path = os.path.join('images', image_folder_name, image_name + '.jpg')
    origin_img = Image.open(origin_img_path)

    # 获取源图像尺寸
    img_width, img_height = origin_img.size

    # 定义矩形区域
    Image_height = 150
    Image_width = 400  # 将矩形宽度调整为源图像的宽度

    x1 = location[0]
    x2 = x1+400
    y1 = location[1]
    y2 = y1+Image_height


    bbox = (x1, y1, x2, y2)

    # 截取矩形区域
    cropped_img = origin_img.crop(bbox)
    # 保存截取后的图片
    cropped_img.save(os.path.join(output_folder_path, image_name + '_cropped.png'))

    # 将截取的图像缩放到与原始图像相同的宽度
    scale_factor = img_width / Image_width
    new_cropped_img_width = img_width
    new_cropped_img_height = int(Image_height * scale_factor)
    resized_cropped_img = cropped_img.resize((new_cropped_img_width, new_cropped_img_height), Image.ANTIALIAS)

    # 给截图后的图片添加边框并保存
    #resized_cropped_img_with_border = ImageOps.expand(resized_cropped_img, border=border_width, fill=color)
    draw_rectangle(resized_cropped_img, bbox=(0, 0, new_cropped_img_width, new_cropped_img_height), color=color, width=border_width)
    resized_cropped_img.save(os.path.join(output_folder_path, image_name + '_cropped_with_border.png'))

    # 在原始图片上绘制矩形框并保存
    draw_rectangle(origin_img,  bbox, color=color, width=border_width)
    origin_img.save(os.path.join(output_folder_path, image_name + '_rect.png'))
    # 创建新的图像（将源图像与带边框的截取图像上下拼接）
    
    # 计算要截取的高度
    crop_height = int(0.8 * img_height)

    # 裁剪原图的上 70% 部分
    cropped_img = origin_img.crop((0, 0, img_width, crop_height))
    new_img_height = crop_height + resized_cropped_img.size[1]
    
    new_img = Image.new('RGB', (img_width, new_img_height))

    # 粘贴源图像
    new_img.paste(cropped_img, (0, 0))
    # 粘贴带边框的截取图像
    new_img.paste(resized_cropped_img, (0, crop_height))

    # 保存最终合并后的图片
    final_output_path = os.path.join(output_father_folder_path, image_name + '.jpg')
    new_img.save(final_output_path)

image_floder_name = 'figure1'

image_floder_path = os.path.join('images', image_floder_name)
# 遍历文件夹中的所有文件名
file_names = []
for root, dirs, files in os.walk(image_floder_path):
    for file in files:
        file_names.append(file)

for image_name in file_names:
    save_image(image_floder_name, image_name[:-4], location = [1120,330])

