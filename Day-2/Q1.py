import os
import glob

#Question-3:
#Given a directory, find out the file Name 
#having max size recursively 

directory=r"C:\Users\Geetha\handson"

def max_file(directory,filename,maxsize):
    p=directory+r"\*"
    items=glob.glob(p)
    for item in items:
        if(os.path.isdir(item)):
            maxsize,filename=max_file(item,filename,maxsize)
        else:
            size=os.path.getsize(item)
            if(size>maxsize):
                maxsize=size;
                filename=os.path.basename(item)
    return [maxsize,filename] 

print(max_file(directory,"no file is present in the directory",0)[1])
