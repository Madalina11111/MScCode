# -*- coding: utf-8 -*-
"""Good make npz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aAaDwV2n2IWsO3NkhMZSXzlRs63KDNkJ
"""

from keras.layers import AveragePooling2D
from keras.layers import LeakyReLU
from keras.layers import Layer
from keras.layers import Add
from keras.constraints import max_norm
from keras.initializers import RandomNormal
from keras import backend
from matplotlib import pyplot
import numpy as np
from os import listdir
from numpy import savez_compressed
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import asarray

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

def load_images(directory):
    resized_images = list()
    f = open("preprocessed_IDRID_real_class_1.txt", "w")
    i = 0
    for filename in listdir(directory):
          img2 = cv2.imread(directory + filename)
          img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
          resized = cv2.resize(img3, (128,128))
          ratio = (255.0/np.amax(resized))
          int_ratio = int(ratio)        
          new_pixels = resized*int_ratio
          i += 1
          print(i)
          resized_images.append(new_pixels)
          f.write("\"" + filename + "\", ")
    f.close()
    return asarray(resized_images)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected training preprocessed/"

all_faces = load_images(directory)
savez_compressed('training_preprocessed_real_plus_fake_selected_708_each_class.npz', all_faces)



directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 2/class 0/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_0_2nd_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 2/class 1/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_1_2nd_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 2/class 2/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_2_2nd_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 2/class 3/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_3_2nd_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 2/class 4/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_4_2nd_time.npz', all_faces)



directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 3/class 0/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_0_3nd_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 3/class 1/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_1_3rd_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 3/class 2/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_2_3rd_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 3/class 3/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_3_3rd_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 3/class 4/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_4_3rd_time.npz', all_faces)



directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 4/class 0/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_0_4th_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 4/class 1/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_1_4th_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 4/class 2/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_2_4th_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 4/class 3/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_3_4th_time.npz', all_faces)

directory = r"/content/gdrive/My Drive/Kaggle/randomly selected preprocessed 4/class 4/"

all_faces = load_images(directory)
savez_compressed('random_selected_preprocessed_real_class_4_4th_time.npz', all_faces)