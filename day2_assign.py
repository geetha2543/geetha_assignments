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
            if(os.path.isfile(item)):
                size=os.path.getsize(item)
                if(size>maxsize):
                    maxsize=size;
                    filename=os.path.basename(item)
    return [maxsize,filename] 

print(max_file(directory,"no file is present in the directory",0)[1])



# Question-4:
# Recursively go below a dir and based on filter, dump those files in to  single file 
# (work with only text file)



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
                print(item)
                with open(item,"rt") as f1:
                    copyfile.write(f1.read())
    pass


with open(copypath,"at") as copyfile:
    copyall(directory,copyfile)
    
    

    
    
    
