I wrote the code in Google Colab. I noticed that files in .ipynb format cannot be read in github, they can only be downloaded, so I uploaded the code in format .py as well.

Description of code from every file:
- RemoveBlackRowsAndColumns all shadows of black.ipynb - It removes the rows and columns with black pixels (pixels with RGB intensities less than or equal to (10, 10, 10). This is part of the data preprocessing method.
- Good_make_npz.ipynb - normalizes every image so it has values between 0 and 255, and saves all the resulting images into a npz file. The npz file contains a numpy array. The npz file is used by the CNNs and GAN.
- Best_so_far_227x227_State_of_the_art_classifier_from_Npz_for_Kaggle,_(from_paper_A_lightweight_CNN_for_Diabetic_Retinopathy_classification_from_fundus_images).ipynb - This is my reimplementation of the state-of-the-art classifier for diabetic retinopathy.
- State_of_the_art_classifier_from_Npz_for_Kaggle,_data_preprocessing(from_paper_A_lightweight_CNN_for_Diabetic_Retinopathy_classification_from_fundus_images).ipynb - This is my reimplementation of the state-of-the-art classifier for diabetic retinopathy, modified to take as input images of resolution 128x128, where training is done on real images and testing is done on the test dataset.
- State_of_the_art_classifier_from_Npz_for_Kaggle,_real_+_fake_images,_data_preprocessing,_testing_on_test_dataset_(from_paper_A_lightweight_CNN_for_Diabetic_Retinopathy_classification_from_fundus_images).ipynb - This is my reimplementation of the state-of-the-art classifier for diabetic retinopathy, modified to take as input images of resolution 128x128, where training is done on real + synthetic images and testing is done on the test dataset.
- GOOD_Class_4_Kaggle_baseline_DCGAN_from_paper_Analysis_of_Adversarial_based_Augmentation_for_Diabetic_Retinopathy_Disease_Grading.ipynb - This is my reimplementation of the GAN.
- Classifier_from_paper_Analysis_of_Adversarial_based_Augmentation_for_Diabetic_Retinopathy_Disease_Grading.ipynb - This is my reimplementation of the CNN from paper “Analysis of Adversarial based Augmentation for Diabetic Retinopathy Disease Grading”
- real_+_fake_data_Classifier_from_paper_Analysis_of_Adversarial_based_Augmentation_for_Diabetic_Retinopathy_Disease_Grading.ipynb - This is my reimplementation of the CNN from paper “Analysis of Adversarial based Augmentation for Diabetic Retinopathy Disease Grading”, where training is done on real + synthetic images.
- Calculate_PSNR_between_fake_cass_4_and_real_class_4.ipynb, Calculate_PSNR_between_fake_cass_4_and_real_class_0.ipynb, Calculate_PSNR_between_fake_cass_4_and_real_class_2.ipynb, Calculate_PSNR_between_fake_cass_4_and_real_class_1.ipynb - These files calculate the average PSNR between images from different folders.
- Calculate_PSNR_between_every_fake_image_class_4_and_real_class_0.ipynb, Calculate_PSNR_between_every_fake_image_class_4_and_real_class_1.ipynb, Calculate_PSNR_between_every_fake_image_class_4_and_real_class_2.ipynb, Calculate_PSNR_between_every_fake_image_class_4_and_real_class_3.ipynb, Calculate_PSNR_between_every_fake_image_class_4_and_real_class_4.ipynb - These files calculate the average PSNR between every image from one folder and all the images from another folder. The minimum and maximum average PSNR are shown.
- Calculate_SSIM.ipynb - This file calculates the average SSIM between every image from one folder to every image from another folder.
- Select_random_images_of_every_class.ipynb - This file selects 100 images of every class from the Kaggle training dataset. The images are preprocessed.
- Calculate_average_cosine_distance.ipynb - This file calculates the average cosine distance between the images from 2 npz files

Link to the npz files used in the code: https://drive.google.com/drive/folders/1iVSlJB3GqIHLXeHkMT4y6lq68gxQd9TO?usp=sharing 

Links to the images:
- Kaggle: https://drive.google.com/drive/folders/130NY_M9UVEQ6gQgErzpcmAxMmAhTJgEg?usp=sharing 
- IDRiD: https://drive.google.com/drive/folders/1OLPjnRmsOmc-1tktkBHp-kpFOx4VxlVZ?usp=sharing 
