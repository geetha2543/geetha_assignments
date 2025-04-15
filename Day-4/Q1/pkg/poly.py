class Poly:
    def __init__(self,*args):
        self.co_effs=list(args)
        
    def __add__(self,b_class):
        a_len=len(self.co_effs)
        b_len=len(b_class.co_effs)
        if a_len>b_len:
            res= add(self.co_effs,b_class.co_effs,b_len)
        else:
            res= add(b_class.co_effs,self.co_effs,a_len)
        return tuple(res)
           
    
        
def add(max_list,min_list,length):
        max_list=max_list[::-1]
        min_list=min_list[::-1]
        for i in range(0,length):
            max_list[i]+=min_list[i]
        return max_list[::-1] 
