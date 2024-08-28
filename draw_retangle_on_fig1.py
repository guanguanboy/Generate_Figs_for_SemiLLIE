from PIL import Image

from PIL import Image, ImageDraw,ImageOps
import os

def draw_rectangle(image, output_path, bbox, color=(255, 0, 0), width=3):    
    # 创建ImageDraw对象
    draw = ImageDraw.Draw(image)
    
    # 绘制矩形框
    draw.rectangle(bbox, outline=color, width=width)
    
    # 保存图片
    image.save(output_path)

def save_images(image_floder_name, image_name,location1=[]):

    output_father_foloder_path = os.path.join('images', image_floder_name + '_output')
    if not os.path.exists(output_father_foloder_path):
        os.mkdir(output_father_foloder_path)

    # 打开图片
    origin_img_path = os.path.join('images', image_floder_name, image_name +'.jpg')
    origin_img = Image.open(origin_img_path)

    img = origin_img


    #绘制红色框并crop其中的内容 
    Image_width = 32

    x1 = location1[0]
    x2 = x1+500
    y1 = location1[1]
    y2 = y1+270

    bbox = (x1, y1, x2, y2)

    #在原始图片上绘制红色矩形框并保存
    draw = ImageDraw.Draw(img)

    # 绘制矩形框
    color=(0, 255, 0)
    width=16
    draw.rectangle(bbox, outline=color, width=width)


    """
    x1 = location2[0]
    x2 = x1+140
    y1 = location2[1]
    y2 = y1+140

    color=(0, 255, 0)
    width=4
    bbox = (x1, y1, x2, y2)
    draw.rectangle(bbox, outline=color, width=width)
    """

    # 保存图片
    output_path = output_father_foloder_path + '/'  + image_name +  '.jpg'
    #output_path = 'images/2015_02485_red_rect.jpg'
    img.save(output_path)


# 示例
"""
image_path = "input.jpg"  # 输入图片路径
output_path = "output.jpg"  # 输出图片路径
bbox = (50, 50, 150, 150)  # 矩形框左上角和右下角坐标 (x1, y1, x2, y2)


draw_rectangle(image_path, output_path, bbox)
"""
image_floder_name = 'figure1'

image_floder_path = os.path.join('images', image_floder_name)
# 遍历文件夹中的所有文件名
file_names = []
for root, dirs, files in os.walk(image_floder_path):
    for file in files:
        file_names.append(file)

for image_name in file_names:
    save_images(image_floder_name, image_name[:-4], location1 = [1020,260])

