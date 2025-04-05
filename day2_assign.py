
"""
Question-3:
Given a directory, find out the file Name 
having max size recursively 
"""
import os
import glob
path=r"C:\Users\Geetha\Downloads\handson\handson\DAY1"

def max_file(directory,filename,maxsize):
    p=directory+r"\*"
    items=glob.glob(p)
    for item in items:
        if(os.path.isdir(item)):
            maxsize,filename=max_file(item,filename,maxsize)
        else:
            if(os.path.isfile(item)):
                size=os.path.getsize(item)
                if(size>maxsize):
                    maxsize=size;
                    filename=os.path.basename(item)
    return [maxsize,filename] 
            



print(max_file(path,"",0)[1])
    
    
    
    
    
