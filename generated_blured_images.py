import cv2

# 读取图片
image_path = 'images/ablation_try2/0000073_05999_d_0000007_Input_darker.jpg'  # 替换为图片的实际路径
image = cv2.imread(image_path)

# 确保图片读取成功
if image is None:
    print("Error: Unable to load image.")
else:
    # 进行轻微的模糊处理
    # 使用高斯模糊函数，ksize参数控制模糊程度
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    
    # 显示处理后的图片
    cv2.imshow('Blurred Image', blurred_image)
    cv2.waitKey(0)  # 等待按键以关闭窗口
    cv2.destroyAllWindows()
    
    # 保存模糊化后的图片
    output_path = 'images/ablation_try2/0000073_05999_d_0000007_Input_darker_blurred.jpg'  # 替换为保存图片的路径
    cv2.imwrite(output_path, blurred_image)
