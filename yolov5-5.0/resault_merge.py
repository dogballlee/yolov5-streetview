import pandas as pd
import os

img_path = r'D:/elephant/tianchi_streetview/mchar_test_a/'
label_path = r'D:/py_project/easy-rl-master/prjt_cv_2022/yolov5-streetview-master/yolov5-5.0/runs/detect/exp18/labels/'
res_merge_path = 'D:/elephant/tianchi_streetview/'
imgs = os.listdir(img_path)

res = {}
for i in imgs:
    if os.path.exists(label_path + i.replace('png', 'txt')):
        a = pd.read_csv(label_path + i.replace('png', 'txt'), sep=' ', header=None)
        b = a.sort_values(by=1)
        s = list(b.iloc[:][0])
        s = int(''.join(str(i) for i in s))
        res[i[:6]] = s
    else:
        res[i[:6]] = 0
# print(res)
with open(res_merge_path + 'res_merge.txt', 'w') as f:
    for k, v in res.items():
        f.write(k + ',' + str(v) + '\r')
f.close()

print('merge done!')
