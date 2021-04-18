from utils.utils import get_file_list, load_img
from utils.ParallerExcutor import ParallelExcutor
# from feature_extraction.extract_features import compute_pds
from config.config import image_source_path, pd_save_path
import matplotlib.pyplot as plt
from skimage import io as skio
from skimage.color import rgb2gray
from tqdm import tqdm
import numpy as np
import os


def controller(file_list, image_source_path, pd_save_path):
    for f in tqdm(file_list):
        f_name = f[0:-4]
        f_path = os.path.join(image_source_path, f)
        gray_img = load_img(f_path)
        # compute_pds(gray_img, f_name, pd_save_path)


if __name__ == "__main__":
#     file_list = get_file_list(image_source_path)
#     # excutor = ParallelExcutor(pool_size=20, func=controller, task_list=file_list, args=[image_source_path, pd_save_path])
#     # excutor.exec()
    img = skio.imread(r"D:\File\dataset\vein_draw\soybean_1024\mask_all\img001_1_2_t_b_mask.png")
    gray = rgb2gray(img)
    vein = (gray > 0).astype(np.uint8)
    plt.imshow(img)
    plt.show()