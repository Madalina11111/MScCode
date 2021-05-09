# -*- coding: utf-8 -*-
"""RemoveBlackRowsAndColumns all shadows of black.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fRYCPtl7GCRs9qQ1Kh5J1c5xHtjcevyi
"""

from PIL import Image
from numpy import asarray
import numpy as np
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

def removeBlackRows(image_array):
  height, width, _ = image_array.shape

  rows_to_delete = []
  for i in range(height):
    row_to_delete = True
    for j in range(width):
      if (image_array[i, j, 0] > 10):
        row_to_delete = False
      if (image_array[i, j, 1] > 10): 
          row_to_delete = False
      if (image_array[i, j, 2] > 10):
          row_to_delete = False
    if(row_to_delete == True):
        rows_to_delete.append(i)

  for row_to_del in reversed(rows_to_delete):
    image_array = np.delete(image_array, row_to_del, 0)
  return image_array

def removeBlackColumns(image_array):
  height, width, _ = image_array.shape

  columns_to_delete = []
  for i in range(width):
      column_to_delete = True
      for j in range(height):
        if (image_array[j, i, 0] > 10):
          column_to_delete = False
        if (image_array[j, i, 1] > 10): 
          column_to_delete = False
        if (image_array[j, i, 2] > 10):
              column_to_delete = False
      if(column_to_delete == True):
          columns_to_delete.append(i)
      
  for column_to_del in reversed(columns_to_delete):
      image_array = np.delete(image_array, column_to_del, 1)

  return image_array

print(len(os.listdir("/content/gdrive/My Drive/Kaggle/training preprocessed")))



#without resizing

for image_to_move in os.listdir("/content/gdrive/My Drive/Kaggle/randomly selected not preprocessed/class 0/"):
  if(image_to_move in os.listdir("/content/gdrive/My Drive/Kaggle/randomly selected preprocessed high resolution/class 0")):
    print("Image already here")
  else:
     print(image_to_move)
     image = Image.open("/content/gdrive/My Drive/Kaggle/randomly selected not preprocessed/class 0" + "/" + image_to_move)
                
     initial_shape = asarray(image).shape
     print(initial_shape)
     #reshaped_image = image.resize((int(initial_shape[1]/6), int(initial_shape[0]/6)))
     print(asarray(image).shape)
     image_as_array = asarray(image)
              
     image_as_array = removeBlackRows(image_as_array)
     image_as_array = removeBlackColumns(image_as_array)
            
     print(image_as_array.shape)
     print("-------------------")

     img_back = Image.fromarray(image_as_array, 'RGB')

     img_back.save('/content/gdrive/My Drive/Kaggle/randomly selected preprocessed high resolution/class 0' + "/" + image_to_move, 'JPEG')







for image_to_move in os.listdir("/content/gdrive/My Drive/Kaggle/randomly selected/class 2/"):
  if(image_to_move in os.listdir("/content/gdrive/My Drive/Kaggle/randomly selected/class 2 preprocessed")):
    print("Image already here")
  else:
     print(image_to_move)
     image = Image.open("/content/gdrive/My Drive/Kaggle/randomly selected/class 2" + "/" + image_to_move)
                
     initial_shape = asarray(image).shape
     print(initial_shape)
     reshaped_image = image.resize((int(initial_shape[1]/6), int(initial_shape[0]/6)))
     print(asarray(reshaped_image).shape)
     image_as_array = asarray(reshaped_image)
              
     image_as_array = removeBlackRows(image_as_array)
     image_as_array = removeBlackColumns(image_as_array)
            
     print(image_as_array.shape)
     print("-------------------")

     img_back = Image.fromarray(image_as_array, 'RGB')

     img_back.save('/content/gdrive/My Drive/Kaggle/randomly selected/class 2 preprocessed' + "/" + image_to_move, 'JPEG')

print(len(os.listdir("/content/gdrive/My Drive/Kaggle/training preprocessed")))