# import numpy as np
# import matplotlib.pyplot as plt
# import os
# import homcloud.interface as hc
# import cv2
# from skimage.morphology import remove_small_objects, remove_small_holes
# from feature_extraction.texture_feature import compute_texture_pd
# from skimage.color import rgb2gray
# from config.config import pht_threshold_texture
# # pd transform
#
#
# class PHT:
#     def __init__(self, v):
#         self.b_1 = np.reshape(np.array([1, 1]) / np.sqrt(2), [1, 2])
#         self.b_2 = np.reshape(np.array([-1, 1]) / np.sqrt(2), [1, 2])
#         self.v = v
#
#     def __call__(self, pds):
#         x = pds * np.repeat(self.b_1, pds.shape[0], axis=0)
#         x = np.sum(x, axis=1)
#         y = pds * np.repeat(self.b_2, pds.shape[0], axis=0)
#         y = np.sum(y, axis=1)
#         i = [y <= self.v]
#         y[i] = np.log(y[i] / self.v) + self.v
#         ret = np.stack([x, y], axis=1)
#         return ret
#
# pht = {}
# pht['texture'] = PHT(pht_threshold_texture)
#
#
# def get_persistence(pd, N):
#     persistence = pd[:, 1] - pd[:, 0]
#     index = np.argsort(persistence)[::-1]
#     if len(index) > N:
#         return index[0:N]
#     else:
#         temp = np.repeat(index[-1], N-len(index))
#         index = np.concatenate([index, temp])
#         return index
#
#
# def compute_pds(gray, name, pd_save_path):
#     texture_pd = None
#     mask = gray > 0
#     mask = remove_small_holes(mask, 1000)
#     mask = remove_small_objects(mask, 1000)
#     gray = mask.astype(int) * gray
#     texture_pd_path = os.path.join(pd_save_path)
#     if not os.path.exists(texture_pd_path):
#         os.mkdir(texture_pd_path)
#     try:
#         texture_pd = compute_texture_pd(gray, name=name, save_path=texture_pd_path)
#     except Exception as e:
#         print(e)
#     return texture_pd
#
#
#
#
