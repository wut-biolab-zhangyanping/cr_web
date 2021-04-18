import numpy as np
import skimage.io as skio
from skimage.measure import find_contours

"""
    1. 在原始的高清二值图像的边沿采点
    2. 计算每个点到其他边缘点的距离和角度形成两个矩阵
    3. 分别计算这两个矩阵的PD然后来分类
"""


def get_contour_point(img):
    mask = img > 0
