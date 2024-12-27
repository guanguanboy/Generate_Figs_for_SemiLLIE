import os
from PIL import Image, ImageDraw

def draw_ellipse_on_images(input_folder, output_folder, ellipse_box, ellipse_color, ellipse_width):
    """
    Draws an ellipse on all images in the input folder and saves them to the output folder.

    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder to save images with ellipses.
        ellipse_box (tuple): A tuple of four integers (x0, y0, x1, y1) defining the bounding box of the ellipse.
        ellipse_color (tuple): Color of the ellipse in (R, G, B) format.
        ellipse_width (int): Width of the ellipse border.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                draw = ImageDraw.Draw(img)
                draw.ellipse(ellipse_box, outline=ellipse_color, width=ellipse_width)
                img.save(output_path)
                print(f"Processed and saved: {output_path}")
        except Exception as e:
            print(f"Error processing {input_path}: {e}")

# Example usage
input_folder = "E:\科研项目\无监督的低光增强\低光下检测的实验\实验结果\Dectection_Show_Results"
output_folder = "E:\科研项目\无监督的低光增强\低光下检测的实验\实验结果\Dectection_Show_Results_with_Eclips"
ellipse_box = (125, 125, 400, 450)  # (x0, y0, x1, y1)
ellipse_color = (255, 255, 255)  # Red
ellipse_width = 8

draw_ellipse_on_images(input_folder, output_folder, ellipse_box, ellipse_color, ellipse_width)