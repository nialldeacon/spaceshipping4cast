import random
from seastate import seastate
from wind import wind
from visibility import visibility
def area_forecast(obj_num,forecast_areas):
    #Generate weather and visibility
    fog_flag=0                            #flags to pass to visibility so fog -> very poor
    fog_patch_flag=0  
    fog_later_flag=0
    x=0
    #while loop to generate weather, while loop needed as some objects don't have all types of weather
    while x<1:
        weather_index=random.randint(0,3)
        if weather_index==0 and forecast_areas[obj_num].has_rain==1:
            weather_sub_index=random.randint(0,2)
            if weather_sub_index==0:            
                weather_condition=forecast_areas[obj_num].rain
            if weather_sub_index==1:            
                weather_condition="occasional "+forecast_areas[obj_num].rain
            if weather_sub_index==2:            
                weather_condition=forecast_areas[obj_num].showers
            x=1
        if weather_index==1 and forecast_areas[obj_num].has_rain==1:
            weather_condition=forecast_areas[obj_num].drizzle
            x=1
        if weather_index==2 and forecast_areas[obj_num].has_fog==1:
            weather_sub_index=random.randint(0,2)
            if weather_sub_index==0:
                weather_condition=forecast_areas[obj_num].fog+" patches"
                fog_patch_flag=1
            else:
                weather_condition=forecast_areas[obj_num].fog
                fog_flag=1
            x=1
        if weather_index==3:
            weather_condition=forecast_areas[obj_num].fair
            x=1
#add change to weather
    random_thing=random.randint(0,2)
    if random_thing>0 and (forecast_areas[obj_num].has_fog==1 or forecast_areas[obj_num].has_rain==1):
        weather_condition1=weather_condition
        x=0
        while x<1:
            weather_index1=random.randint(0,3)
            if weather_index1!=weather_index:
                if weather_index1==0 and forecast_areas[obj_num].has_rain==1:
                    weather_sub_index=random.randint(0,2)
                    if weather_sub_index==0:            
                        weather_condition=weather_condition1+", "+forecast_areas[obj_num].rain+" later"
                    if weather_sub_index==1:            
                        weather_condition=weather_condition1+", "+"occasional "+forecast_areas[obj_num].rain+" later"
                    if weather_sub_index==2:            
                        weather_condition=weather_condition1+", "+forecast_areas[obj_num].showers+" later"
                    x=1
                if weather_index1==1 and forecast_areas[obj_num].has_rain==1:
                    weather_condition=weather_condition1+", "+forecast_areas[obj_num].drizzle+" later"
                    x=1
                if weather_index1==2 and forecast_areas[obj_num].has_fog==1:
                    weather_condition=weather_condition1+", "+forecast_areas[obj_num].fog+" later"
                    fog_later_flag=1
                    x=1
                if weather_index1==3:
                    weather_condition=weather_condition1+", "+forecast_areas[obj_num].fair+" later"
                    x=1

    
#Generate wind, seastate & visibility
    x=0
    while x<1:
        force_thing = random.randint(0,11)
        if force_thing>8:
            redo_thing=random.randint(0,5)
            if redo_thing>4:
                x=1
        else:
            x=1


    wind_condition=wind(force_thing)
    sea_condition=seastate(force_thing)
    visibility_condition=visibility(fog_flag,fog_patch_flag,fog_later_flag,forecast_areas[obj_num].has_fog)
    forecast_string=forecast_areas[obj_num].name+": "+wind_condition+"; "+sea_condition+"; "+weather_condition+"; "+visibility_condition
    return forecast_string
