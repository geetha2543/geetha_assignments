import os,datetime,glob

class File:
    def __init__(self,directory):
        self.path = directory
        
    def getMaxSizeFile(self,n):
        res = get_max_files(self.path)
        print(res[-n::][::-1])
        
    def getLatestFiles(self,deadline):
        res = get_later_files(self.path)
        print([file for file in res if res[file] > deadline])
    
        
def get_max_files(path):
    def get_files(path, ed={}):
        files = glob.glob(os.path.join(path, "*"))
        for f in files:
            if os.path.isfile(f):
                ed[f] = os.path.getsize(f)
            elif os.path.isdir(f):
                get_files(f, ed)
        return ed  
        
    allfiles = get_files(path)
    size_sorted_files = sorted(allfiles, key=lambda k: allfiles[k])    
    return size_sorted_files
    
    
def get_later_files(path):
    def get_files(path, ed={}):
        files = glob.glob(os.path.join(path, "*"))
        for f in files:
            if os.path.isfile(f):
                ed[f] =datetime.date.fromtimestamp(os.path.getctime(f))
            elif os.path.isdir(f):
                get_files(f, ed)
        return ed   
        
    allfiles = get_files(path)   
    return allfiles
