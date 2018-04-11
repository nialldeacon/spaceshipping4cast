import string
import random
def seastate(force_thing):
    string_arr = ["smooth","slight","moderate","rough","very rough","high","very high","phenomenal"]
    #convert wind force to seastate adding a small random variation
    x=0
    while x<1:
        index_thing = int(force_thing/1.7)
        delta=random.randint(-1,1)
        if (index_thing+delta)>-1 and  (index_thing+delta)<8:
            index_thing=index_thing+delta
        condition = string_arr[index_thing]
        if index_thing>4:
            redo_thing=random.randint(0,5)
            if redo_thing>4:
                x=1
        else:
            x=1
    if index_thing < 7:
        redo_thing=random.randint(0,1)
        if redo_thing>0:
            condition=string_arr[index_thing]+" or "+string_arr[index_thing+1]
    #add change to the seastate
    delta=random.randint(-1,1)
    if delta !=0 and (delta+index_thing)>-1 and (delta+index_thing)<8:
        redo_thing=random.randint(0,4)
        if redo_thing==2:
            condition=condition+", occasionally "+string_arr[index_thing+delta]
            redo_thing1=random.randint(0,4)
            if redo_thing1==0:
                condition=condition+' later'
            if redo_thing1==1:
                condition=condition+' at first'
        if redo_thing>3:
            condition=condition+", becoming "+string_arr[index_thing+delta]
            redo_thing1=random.randint(0,1)
            if redo_thing1==1 and (index_thing+delta)<7:
                condition=condition+' or '+string_arr[index_thing+delta+1]
            redo_thing1=random.randint(0,1)
            if redo_thing1==1:
                condition=condition+' later'
    return condition
