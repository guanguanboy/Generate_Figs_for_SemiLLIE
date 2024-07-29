from PIL import Image, ImageEnhance

# 打开图像
image_path = 'images/ablation_try2/0000073_05999_d_0000007_Input.jpg'  # 替换为你的图像路径
image = Image.open(image_path)

# 创建一个图像增强对象
enhancer = ImageEnhance.Brightness(image)

# 调整亮度，factor<1会变暗
factor = 0.8  # 设置为0.5，图像会变得暗一些，可以根据需要调整
darker_image = enhancer.enhance(factor)

# 保存变暗后的图像
darker_image.save('images/ablation_try2/0000073_05999_d_0000007_Input_darker.jpg')  # 替换为你想保存的路径

# 显示变暗后的图像
darker_image.show()
