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

def save_images(image_floder_name, image_name,location1=[],location2=[]):

    output_father_foloder_path = os.path.join('images', image_floder_name + '_output')
    if not os.path.exists(output_father_foloder_path):
        os.mkdir(output_father_foloder_path)
    #final_output_image_folder_name = os.path.join(image_floder_name + '_output')
    output_image_folder_name = os.path.join(image_floder_name + '_output', image_name)

    output_folder_path = os.path.join('images', output_image_folder_name)
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)

    # 打开图片
    origin_img_path = os.path.join('images', image_floder_name, image_name +'.jpg')
    origin_img = Image.open(origin_img_path)

    img = origin_img


    #绘制红色框并crop其中的内容 
    Image_height = 256
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

    # 获取原图和截取图像的尺寸
    img_width, img_height = img.size
    cropped_img1_width, cropped_img1_height = cropped_img_red_with_border.size

    # 计算截取图像的宽度和原图宽度的比例
    total_cropped_width = cropped_img1_width
    scale_factor = img_width / total_cropped_width
    
    # 缩放截取图像
    new_cropped_img1_width = int(cropped_img1_width * scale_factor)
    new_cropped_img1_height = int(cropped_img1_height * scale_factor)

    
    resized_cropped_img1 = cropped_img_red_with_border.resize((new_cropped_img1_width, new_cropped_img1_height), Image.ANTIALIAS)

    
    # 计算新图像的高度（原图高度 + 最大的截取图像高度）
    new_img_height = img_height + new_cropped_img1_height
    
    # 创建新的图像（宽度和原图相同，高度为新计算的高度）
    new_img = Image.new('RGB', (img_width, new_img_height))
    
    # 将原图粘贴到新图像的顶部
    new_img.paste(img, (0, 0))
    
    # 将放大后的图像粘贴到新图像的底部
    new_img.paste(resized_cropped_img1, (0, img_height))

    """
    scale_value = 3
    cropped_img_red_with_border_resized = cropped_img_red_with_border.resize((cropped_img_red_with_border.width*scale_value, cropped_img_red_with_border.height*scale_value))
    cropped_img_red_with_border_width = cropped_img_red_with_border_resized.width
    cropped_img_red_with_border_height = cropped_img_red_with_border_resized.height

    cropped_img_blue_with_border_resized = cropped_img_blue_with_border.resize((cropped_img_blue_with_border.width*scale_value, cropped_img_blue_with_border.height*scale_value))
    cropped_img_blue_with_border_width = cropped_img_blue_with_border_resized.width
    cropped_img_blue_with_border_height = cropped_img_blue_with_border_resized.height

    big_img_width = img.width
    big_img_height = img.height

    # 将小图1粘贴到大图的左下角
    img.paste(cropped_img_red_with_border_resized, (0, big_img_height - cropped_img_red_with_border_height))

    # 将小图2粘贴到大图的右下角
    img.paste(cropped_img_blue_with_border_resized, (big_img_width - cropped_img_blue_with_border_width, big_img_height - cropped_img_blue_with_border_height))
    """


    # 保存合并后的图片
    output_path = output_father_foloder_path + '/'  + image_name +  '_final.png'

    new_img.save(output_path)




# 示例
"""
image_path = "input.jpg"  # 输入图片路径
output_path = "output.jpg"  # 输出图片路径
bbox = (50, 50, 150, 150)  # 矩形框左上角和右下角坐标 (x1, y1, x2, y2)


draw_rectangle(image_path, output_path, bbox)
"""
image_floder_name = 'quali_comp'

image_floder_path = os.path.join('images', image_floder_name)
# 遍历文件夹中的所有文件名
file_names = []
for root, dirs, files in os.walk(image_floder_path):
    for file in files:
        file_names.append(file)

for image_name in file_names:
    #save_images(image_floder_name, image_name[:-4], location1 = [10,10], location2=[120,120])
    save_images(image_floder_name, image_name[:-4], location1 = [250,30])
    #save_images(image_floder_name, image_name[:-4], location1 = [10,10], location2=[160,50])

