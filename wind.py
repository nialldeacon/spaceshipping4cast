import string
import random
def wind(force_thing):
    string_arr=["variable","cylconic","N","NE","E","SE","S","SW","W","NW"]
    string_arr1=["1","2","3","4","5","6","7","gale 8","severe gale 9","storm 10","violent storm 11","hurricane force 12"]
    #generate wind direction, need to be careful as direction 0 and 1 don't give compass directions
    x=0
    while x<1:
        direction_thing = random.randint(0,9)
        if direction_thing>1 or force_thing<6:
            x=1
    direction=string_arr[direction_thing]
    force=string_arr1[force_thing]
    down_flag=0
    up_flag=0
    #add wind direction variability
    redo_thing=random.randint(0,5)
    if redo_thing>4 and direction_thing>1:
        if direction_thing!=9:
            direction=string_arr[direction_thing]+" or "+string_arr[direction_thing+1]
        else:
            direction=string_arr[2]+" or "+string_arr[direction_thing]
    if redo_thing==2 and direction_thing>1:
        if direction_thing!=9:
            direction=string_arr[direction_thing]+" veering "+string_arr[direction_thing+1]
        else:
            direction=string_arr[2]+" or "+string_arr[direction_thing]
            
    if redo_thing==3 and direction_thing>1 :
        if direction_thing!=2:
            direction=string_arr[direction_thing]+" backing "+string_arr[direction_thing-1]
        else:
            direction=string_arr[direction_thing]+" backing "+string_arr[9]
    redo_thing=random.randint(0,6)
    #add short term change in wind and use up_flag and down_flag to keep a record of it
    if redo_thing==3:
        redo_thing1=random.randint(0,1)
        if redo_thing1==1 and force_thing<11:
            force = string_arr1[force_thing]+" occasionally "+string_arr1[force_thing+1]
            up_flag=1
        if redo_thing1==0 and force_thing>0:
            force = string_arr1[force_thing]+" occasionally "+string_arr1[force_thing-1]
            down_flag=1
    if redo_thing>3 and force_thing<6:
            force = string_arr1[force_thing]+" or "+string_arr1[force_thing+1]
            up_flag=1
    if redo_thing>3 and force>5 and force_thing<11:
            force = string_arr1[force_thing]+" to "+string_arr1[force_thing+1]
            up_flag=1
    condition=direction+" "+force
#add wind direction/force change
    delta_direction=random.randint(-1,1)
    delta_force=random.randint(-1,1)
    #changing only the wind force. If win speed had previous short-term up or down change then a movement later in the same direction is by 2 on the wind scale, 1 otherwise 
    if delta_direction==0 and delta_force==-1:
        if down_flag==0 and force_thing>0:
            condition=condition+", decreasing "+string_arr1[force_thing-1]
        if down_flag==1 and force_thing>1:
            condition=condition+", decreasing "+string_arr1[force_thing-2]
    if delta_direction==0 and delta_force==1:        
        if up_flag==0 and force_thing<11:
            condition=condition+", increasing "+string_arr1[force_thing+1]
        if up_flag==1 and force_thing<10:
            condition=condition+", increasing "+string_arr1[force_thing+2]
    #changing both wind direction and force
    if delta_direction!=0 and delta_force!=0:
        if force_thing>0 and force_thing<11:
            if direction_thing>2 and (direction_thing)<9:
                condition=condition+", becoming "+string_arr[direction_thing+delta_direction]+" "+string_arr1[force_thing+delta_force]
            if direction_thing==2:
                if(delta_direction==-1):
                    condition=condition+", becoming "+string_arr[9]+" "+string_arr1[force_thing]
                else:
                    condition=condition+", becoming "+string_arr[direction_thing+delta_direction]+" "+string_arr1[force_thing+delta_force]
                        
            if direction_thing==9:
                if(delta_direction==1):
                    condition=condition+", becoming "+string_arr[2]+" "+string_arr1[force_thing+delta_force]
                else:
                    condition=condition+", becoming "+string_arr[direction_thing+delta_direction]+" "+string_arr1[force_thing+delta_force]
    #When direction changes but force doesn't change to variable or cyclonic
    if delta_direction!=0 and delta_force==0:
        redo_thing1=random.randint(0,1)
        if redo_thing1==0:
            condition=condition+", becoming variable "+string_arr1[force_thing]
        if redo_thing1==1:
            condition=condition+", becoming cyclonic "+string_arr1[force_thing]
    if delta_direction!=0 or delta_force!=0:
        redo_thing1=random.randint(0,1)
        if redo_thing1==1:
            condition=condition+" at times"
        if redo_thing1==1:
            condition=condition+" later"
            
            
    return condition
    
