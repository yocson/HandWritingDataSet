
import os
import glob
import shutil


forms_for_parsing=open(r'forms_for_parsing.txt',mode='r')
d = {}
lines=forms_for_parsing.readlines()


for line in lines:
  key = line.split(' ')[0]
  writer = line.split(' ')[1]                   
  d[key] = writer
  if not os.path.exists(writer):
    os.makedirs(writer)


# print(d)

outputDir = os.getcwd()

for fpath in glob.glob('*.png'):  # this returns a list of the CURRENT contents. Therefore, there is no need to sanitize for the directories that we will later create
    filekey="-".join(fpath.split("-", 2)[:2])
    
    filewriter=d[filekey]
    
    

    
    print(filewriter)
    print(os.path.join(outputDir, filewriter))
    shutil.move(fpath, os.path.join(outputDir, filewriter))