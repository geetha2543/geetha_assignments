"""
Question-13              
convert(x)          Converts like below 
                    input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
                    output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]
"""
def convert(lst):
    for item in lst:
        if type(item) is list:
            convert(item)
        else:
            lst[lst.index(item)] = [int(x) for x in (item[1:-1:2])]
    return lst
  
lst = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
print(convert(lst))
