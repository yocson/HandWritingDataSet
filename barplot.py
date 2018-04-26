import os
import matplotlib.pyplot as plt
import numpy as np
writers=[name for name in os.listdir(".") if os.path.isdir(name)]
num_pic=[]
# print(writers)
for w in writers:
    l=len(os.listdir('./'+w))
    # print(l)
    num_pic.append(l)

objects=[]
for i in range(1,51):
    objects.append(i)
# objects = writers
y_pos = np.arange(len(objects))
performance = num_pic
 
plt.bar(y_pos, performance, align='center', alpha=0.9)
plt.xticks(y_pos, objects)
plt.ylabel('Number of images')
plt.title('Writer contribution')
 
plt.show()