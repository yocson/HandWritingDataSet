import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import shutil
writers=[name for name in os.listdir("./Train/") if os.path.isdir("./Train/"+name)]
print(writers)
num_pic=[]
# print(writers)
for w in writers:
    l=len(os.listdir('./Train/'+w))
    # print(l)
    num_pic.append(l)

# print(num_pic)

test_size=[int(1*x/6) for x in num_pic]
print(test_size)

train_dir="./Train/"
for i in range(len(test_size)):
# for i in range(2):
    for j in range(test_size[i]):
        path=train_dir+writers[i]
        src=path+"/"+os.listdir(path)[j]
        dest='./Validation/'+writers[i]
        # print(src)
        if not os.path.exists(dest):
            os.makedirs(dest)
        shutil.move(src,dest)


