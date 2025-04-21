"""
flatten(lst)        Flattens the list 
                    ie input = [1,2,3, [1,2,3,[3,4],2]]
                    output = [1,2,3,1,2,3,3,4,2]
                    """
flattened_list = []
def flatten(lst):
    for item in lst:
        if type(item) is list:
            flatten(item)
        else:
            flattened_list.append(item)
    return flattened_list

lst = [1,2,3, [1,2,3,[3,4],2]]
print(flatten(lst))
