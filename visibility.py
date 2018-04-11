import string
import random
def visibility(fog_flag,fog_patch_flag,fog_later_flag,has_fog):
    string_arr=["good","moderate","poor","very poor"]
    #generate visibility objects with no atmosphere can only have good/moderate. When fog happens visibility is set to very poor
    if has_fog==0:
      index_thing = random.randint(0,1)
      condition=string_arr[index_thing]
    else:
        index_thing = random.randint(0,2)
        if fog_flag==1:
            index_thing = 3
        condition=string_arr[index_thing]
    #add change to visibility
    if fog_patch_flag==0 and fog_later_flag==0:
        delta=random.randint(-1,1)
        if delta!=0 and (index_thing+delta)>-1 and (index_thing+delta)<4:        
            random_thing=random.randint(0,2)
            if random_thing==0:
                condition=condition+", occasionally "+string_arr[index_thing+delta]
            if random_thing==1:
                condition=condition+", "+string_arr[index_thing+delta]+" later" 
            if random_thing==2:
                condition=condition+", occasionally "+string_arr[index_thing+delta]+" later"
    if  fog_patch_flag==1:
        condition=condition+", occasionally "+string_arr[3]
    if  fog_later_flag==1:
        condition=condition+", "+string_arr[3]+" later"
    return condition
