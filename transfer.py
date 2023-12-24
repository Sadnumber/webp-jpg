import os
from PIL import Image

def convert_webp_to_jpg(source_folder, destination_folder):
    # 获取源文件夹中所有文件的路径
    files = os.listdir(source_folder)

    for file in files:
        # 检查文件是否是webp格式
        if file.endswith('.webp'):
            # 构建源文件的完整路径
            source_path = os.path.join(source_folder, file)

            # 构建目标文件的完整路径，将后缀改为jpg
            destination_path = os.path.join(destination_folder, file.replace('.webp', '.jpg'))

            # 打开并转换图片格式
            image = Image.open(source_path)
            image.convert('RGB').save(destination_path, 'JPEG')

# 调用函数进行转换
convert_webp_to_jpg('test', 'test1')