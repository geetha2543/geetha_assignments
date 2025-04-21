# Question-4:
# Recursively go below a dir and based on filter, dump those files in to  single file 
# (work with only text file)


import os
import glob
 

directory=r"C:\Users\Geetha\handson"

copypath=r"C:\Users\Geetha\copyfile.txt"
filter="txt"
def copyall(directory,copyfile):
    directory_path=directory+r"\*"
    filter_files=[items for items in glob.glob(f"{directory}//*.{filter}")]
    items=glob.glob(directory_path)
    for item in items:
        if(os.path.isdir(item)):
           copyall(item,copyfile)
        else:
            if item in filter_files:
                with open(item,"rt") as f1:
                    copyfile.write(f1.read())
    pass


with open(copypath,"at") as copyfile:
    copyall(directory,copyfile)
    
