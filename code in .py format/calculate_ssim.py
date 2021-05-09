# -*- coding: utf-8 -*-
"""Calculate SSIM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m-QwlCA2DPOVDb-B44OsShnpiod7djRR
"""

from skimage.measure import compare_ssim as ssim
import cv2
import os

from google.colab import drive
drive.mount('/content/gdrive')

directory_real_class_4 = "/content/gdrive/My Drive/Kaggle/randomly selected preprocessed/class 3/"
directory_fake = "/content/gdrive/My Drive/Kaggle/randomly selected preprocessed/class 1/"
ssim_average = 0
i = 0
for real_image in os.listdir(directory_real_class_4):
  for fake_image in os.listdir(directory_fake):
    img_real = cv2.imread(directory_real_class_4 + real_image)
    img_real = cv2.cvtColor(img_real, cv2.COLOR_BGR2RGB)
    img_fake = cv2.imread(directory_fake + fake_image)
    img_fake = cv2.cvtColor(img_fake, cv2.COLOR_BGR2RGB)
    img_real = cv2.resize(img_real, (128, 128))
    img_fake = cv2.resize(img_fake, (128, 128))
    ssim_none = ssim(img_real, img_fake, multichannel=True)
    ssim_average += ssim_none
    i+=1
    print(i)
ssim_average = ssim_average/i
print("---------------")
print(ssim_average)

directory_IDRID = r"/content/gdrive/My Drive/Kaggle/fake 89"
directory_Kaggle = r"/content/gdrive/My Drive/Kaggle/preprocessing class 4"

ssim_sum = 0
iter = 0
for filename_IDRiD in os.listdir(directory_IDRID):
  img1 = cv2.imread(directory_IDRID + '/' + filename_IDRiD)
  img1 = cv2.resize(img1, (128, 128))
  for filename_Kaggle in os.listdir(directory_Kaggle):
    img2 = cv2.imread(directory_Kaggle + '/' + filename_Kaggle)
    try:
        img2 = cv2.resize(img2, (128, 128))
        ssim_none = ssim(img1, img2, multichannel=True)
        ssim_sum += ssim_none
        print(ssim_none)
        print(iter)
        iter += 1
        print("----------")
    except:
      print("filename_Kaggle")

print(ssim_sum/iter)