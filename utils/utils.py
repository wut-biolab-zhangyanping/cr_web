import os
from tqdm import tqdm
import skimage.io as skio


def get_file_list(source_path):
    files = os.listdir(source_path)
    file_list = []
    for f in tqdm(files):
        if f.endswith(".png") or f.endswith(".tif") or f.endswith(".jpg"):
            file_list.append(f)
    return file_list


def load_img(file_path):
    gray_img = skio.imread(file_path, as_gray=True)
    return gray_img