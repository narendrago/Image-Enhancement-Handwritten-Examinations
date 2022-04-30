import cv2
import os
import numpy as np
from tqdm import tqdm
os.makedirs('/Users/narendraomprakash/Desktop/Narendra/Semester-VI-WINTER2021/Image Processing/JCOM/Datasets/HK_dataset/Deblurring-3/gaussian_blurred', exist_ok=True)
src_dir = '/Users/narendraomprakash/Desktop/Narendra/Semester-VI-WINTER2021/Image Processing/JCOM/Datasets/HK_dataset/img'
images = os.listdir(src_dir)
dst_dir = '/Users/narendraomprakash/Desktop/Narendra/Semester-VI-WINTER2021/Image Processing/JCOM/Datasets/HK_dataset/Deblurring-3/gaussian_blurred'

for i, img in tqdm(enumerate(images), total=len(images)):
    img = cv2.imread(f"{src_dir}/{images[i]}", cv2.IMREAD_COLOR)
    blur = cv2.GaussianBlur(img, (31, 31), 0)
    cv2.imwrite(f"{dst_dir}/{images[i]}", blur)
print('DONE')