import os
import shutil

# 图像路径
train_image_path = 'D:/py_project/easy-rl-master/prjt_cv_2022/yolov5-streetview-master/data/images/mchar_train_origin/'
val_image_path = 'D:/py_project/easy-rl-master/prjt_cv_2022/yolov5-streetview-master/data/images/mchar_val/'
dst_image_path = 'D:/py_project/easy-rl-master/prjt_cv_2022/yolov5-streetview-master/data/images/mchar_train/'
train_image_list = os.listdir(train_image_path)
val_image_list = os.listdir(val_image_path)

for img in train_image_list:
    shutil.copy(train_image_path+img, dst_image_path+img)
for img in val_image_list:
    shutil.copy(val_image_path+img, dst_image_path+'val_'+img)

# 标签路径
train_label_path = 'D:/py_project/easy-rl-master/prjt_cv_2022/yolov5-streetview-master/data/labels/mchar_train_origin/'
val_label_path = 'D:/py_project/easy-rl-master/prjt_cv_2022/yolov5-streetview-master/data/labels/mchar_val/'
dst_label_path = 'D:/py_project/easy-rl-master/prjt_cv_2022/yolov5-streetview-master/data/labels/mchar_train/'
train_label_list = os.listdir(train_label_path)
val_label_list = os.listdir(val_label_path)

for txt in train_label_list:
    shutil.copy(train_label_path + txt, dst_label_path + txt)
for txt in val_label_list:
    shutil.copy(val_label_path + txt, dst_label_path+'val_'+txt)
