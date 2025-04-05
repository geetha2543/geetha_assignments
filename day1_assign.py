d1 = {'ok': 1, 'nok': 2}
d2 = {'ok': 2, 'new':3 }


#union

union=d1.copy()
for keys in d2:
    union[keys]=d2[keys]        
print(union)
                #or
#print(d1|d2)


#--------------------------------------------------------------------------------------


#intersection

intersection={}
for key1 in d1:
    if key1 in d2:
        intersection[key1]=d1[key1]  
print(intersection)
                #or
intersection={keys:values for keys,values in d1.items() if keys in d2}
#print(intersection)


#--------------------------------------------------------------------------------------


#d1-d2

only_d1={}
for keys in d1:
    if keys not in d2:
        only_d1[keys]=d1[keys]
print(only_d1)
                #or
only_d1={keys:values for keys,values in d1.items() if keys not in d2}
print(only_d1)


#--------------------------------------------------------------------------------------


#merge

merge=d1.copy()
for keys in d2:
    if keys not in merge:
        merge[keys]=d2[keys] 
    else:
        merge[keys]+=d2[keys]
        
print(merge)

