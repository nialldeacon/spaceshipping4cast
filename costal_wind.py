import string
import random
def costal_wind():
    string_arr=["N","NE","E","SE","S","SW","W","NW"]
    string_arr1=["1","2","3","4","5","6","7","gale 8","severe gale 9","storm 10","violent storm 11","hurricane force 12"]
    direction_thing = random.randint(0,7)
    x=0
    #generate force with 8 or higher 3 times less likely to be generated
    while x<1:
        force_thing = random.randint(0,11)
        if force_thing>8:
            redo_thing=random.randint(0,5)
            if redo_thing>4:
                x=1
        else:
            x=1
    coin_toss = random.randint(0,1)
    #Generate slight difference in direction
    if coin_toss==1:
        if direction_thing!=7:
           condition=string_arr[direction_thing]+" by "+string_arr[direction_thing+1]+" "+string_arr1[force_thing]
        else:
            condition=string_arr[direction_thing]+" by "+string_arr[0]+" "+string_arr1[force_thing]  
    else:
        condition=string_arr[direction_thing]+" "+string_arr1[force_thing]
    return condition
