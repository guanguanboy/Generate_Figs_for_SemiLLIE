from PIL import Image

from PIL import Image, ImageDraw,ImageOps
import os
"""
def draw_rectangle(image, output_path, bbox, color=(255, 0, 0), width=3):    
    # 创建ImageDraw对象
    draw = ImageDraw.Draw(image)
    
    # 绘制矩形框
    draw.rectangle(bbox, outline=color, width=width)
    
    # 保存图片
    image.save(output_path)

def save_images(image_floder_name, image_name,location1=[],location2=[]):

    output_father_foloder_path = os.path.join('images', image_floder_name + '_output')
    if not os.path.exists(output_father_foloder_path):
        os.mkdir(output_father_foloder_path)
    output_image_folder_name = os.path.join(image_floder_name + '_output', image_name)

    output_folder_path = os.path.join('images', output_image_folder_name)
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)

    # 打开图片
    origin_img_path = os.path.join('images', image_floder_name, image_name +'.jpg')
    origin_img = Image.open(origin_img_path)

    img = origin_img


    #绘制红色框并crop其中的内容 
    Image_height = 128
    Image_width = Image_height*2

    x1 = location1[0]
    x2 = x1+Image_width
    y1 = location1[1]
    y2 = y1+Image_height

    bbox = (x1, y1, x2, y2)

    # 截取矩形区域
    cropped_img_red = origin_img.crop(bbox)
    # 保存截取后的图片
    cropped_img_red.save(output_folder_path + '/'  + image_name + '_cropped_red.png')
    #cropped_img.save('images/2015_02485_cropped.jpg')


    #给截图后的图片上添加red边框并保存
    # 定义边框宽度和颜色
    border_width = 2
    border_color = (255, 0, 0)  # 红色 RGB 值

    # 添加边框
    cropped_img_red_with_border = ImageOps.expand(cropped_img_red, border=border_width, fill=border_color)
    cropped_img_red_with_border.save(output_folder_path + '/'  + image_name + '_cropped_red_with_border.png')

    #在原始图片上绘制红色矩形框并保存
    draw = ImageDraw.Draw(img)

    # 绘制矩形框
    color=(255, 0, 0)
    width=4
    draw.rectangle(bbox, outline=color, width=width)

    # 保存图片
    output_path = output_folder_path + '/'  + image_name +  '_red_rect.png'
    #output_path = 'images/2015_02485_red_rect.jpg'
    img.save(output_path)


    #继续绘制blue框并crop其中的内容 

    #定义矩形区域
    x1 = location2[0]
    x2 = x1+Image_width
    y1 = location2[1]
    y2 = y1+Image_height

    bbox = (x1, y1, x2, y2)
    # 截取矩形区域
    cropped_img_blue = origin_img.crop(bbox)


    # 保存截取后的图片
    cropped_img_blue.save(output_folder_path + '/'  + image_name + '_cropped_blue.png')
    #cropped_img.save('images/2015_02485_cropped.jpg')

    #给截图后的图片上添加red边框并保存
    # 定义边框宽度和颜色
    border_width = 2
    border_color = (0, 0, 255)  # 红色 RGB 值

    # 添加边框
    cropped_img_blue_with_border = ImageOps.expand(cropped_img_blue, border=border_width, fill=border_color)
    cropped_img_blue_with_border.save(output_folder_path + '/'  + image_name + '_cropped_blue_with_border.png')

    #在原始图片上绘制红色矩形框并保存
    draw = ImageDraw.Draw(img)

    # 绘制矩形框
    blue_color=(0, 0, 256)
    width=4
    draw.rectangle(bbox, outline=blue_color, width=width)

    # 保存图片
    output_path = output_folder_path + '/'  + image_name +  '_full_rect.png'
    #output_path = 'images/2015_02485_red_rect.jpg'
    img.save(output_path)

    # 获取原图和截取图像的尺寸
    img_width, img_height = img.size
    cropped_img1_width, cropped_img1_height = cropped_img_red_with_border.size
    cropped_img2_width, cropped_img2_height = cropped_img_blue_with_border.size

    # 计算截取图像的宽度和原图宽度的比例
    total_cropped_width = cropped_img1_width + cropped_img2_width
    scale_factor = img_width / total_cropped_width
    
    # 缩放截取图像
    new_cropped_img1_width = int(cropped_img1_width * scale_factor)
    new_cropped_img1_height = int(cropped_img1_height * scale_factor)
    new_cropped_img2_width = int(cropped_img2_width * scale_factor)
    new_cropped_img2_height = int(cropped_img2_height * scale_factor)
    
    resized_cropped_img1 = cropped_img_red_with_border.resize((new_cropped_img1_width, new_cropped_img1_height), Image.ANTIALIAS)
    resized_cropped_img2 = cropped_img_blue_with_border.resize((new_cropped_img2_width, new_cropped_img2_height), Image.ANTIALIAS)
    
    # 计算新图像的高度（原图高度 + 最大的截取图像高度）
    new_img_height = img_height + max(new_cropped_img1_height, new_cropped_img2_height)
    
    # 创建新的图像（宽度和原图相同，高度为新计算的高度）
    new_img = Image.new('RGB', (img_width, new_img_height))
    
    # 将原图粘贴到新图像的顶部
    new_img.paste(img, (0, 0))
    
    # 计算截取图像粘贴的位置
    box1_position = (0, img_height)
    box2_position = (new_cropped_img1_width, img_height)
    
    # 将缩放后的截取图像粘贴到新图像
    new_img.paste(resized_cropped_img1, box1_position)
    new_img.paste(resized_cropped_img2, box2_position)


    # 保存合并后的图片
    output_path = output_father_foloder_path + '/'  + image_name +  '_final.png'

    new_img.save(output_path)
"""

def draw_rectangle(image, bbox, color=(255, 0, 0), width=24):
    # 创建ImageDraw对象
    draw = ImageDraw.Draw(image)
    
    # 绘制矩形框
    for i in range(width):
        adjusted_bbox = (bbox[0] + i, bbox[1] + i, bbox[2] - i, bbox[3] - i)
        draw.rectangle(adjusted_bbox, outline=color)

def save_image(image_folder_name, image_name, location=[0, 0], color=(255, 0, 0), border_width=24):

    # 创建输出文件夹
    output_father_folder_path = os.path.join('images', image_folder_name + '_output')
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
    Image_height = 128
    Image_width = Image_height*2  # 将矩形宽度调整为源图像的宽度

    x1 = location[0]
    y1 = location[1]
    x2 = x1 + Image_width
    y2 = y1 + Image_height

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
    new_img_height = img_height + resized_cropped_img.size[1]
    new_img = Image.new('RGB', (img_width, new_img_height))

    # 粘贴源图像
    new_img.paste(origin_img, (0, 0))
    # 粘贴带边框的截取图像
    new_img.paste(resized_cropped_img, (0, img_height))

    # 保存最终合并后的图片
    final_output_path = os.path.join(output_father_folder_path, image_name + '_final.png')
    new_img.save(final_output_path)


# 示例
image_floder_name = 'ablation_try2'

image_floder_path = os.path.join('images', image_floder_name)
# 遍历文件夹中的所有文件名
file_names = []
for root, dirs, files in os.walk(image_floder_path):
    for file in files:
        file_names.append(file)

for image_name in file_names:
    #save_images(image_floder_name, image_name[:-4], location1 = [10,10], location2=[120,120])
    save_image(image_floder_name, image_name[:-4], location = [400,180])
    #save_images(image_floder_name, image_name[:-4], location1 = [10,10], location2=[160,50])

