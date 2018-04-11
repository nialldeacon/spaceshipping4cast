import string
import random
import math
from costal_wind import costal_wind

def costal_report(obj_num,costal_stations):
    #set up flags ton indicate if fog and weather are generated. Costal stations don't always report weather
    fog_flag=0
    weather_flag=0
    if costal_stations[obj_num].has_atmo==1:
        #generate pressure as a +/-3% variation on the pressure value each object has
        new_pressure=random.uniform(0.97,1.03)*costal_stations[obj_num].pressure
        order=math.log10(new_pressure)
        if order<0:
            temp_str1="%%%d.%df"%(int(math.ceil(abs(order))+4),int(math.ceil(abs(order))+2))
            pressure_str=temp_str1%new_pressure
        if order>0 and order<3:
            temp_str1="%3.1f"
            pressure_str=temp_str1%new_pressure
        if order>3 and order<4:
            temp_str1="%d"
            pressure_str=temp_str1%int(int(new_pressure/10)*10)
        if order>4:
            temp_str1="%d"
            pressure_str=temp_str1%int(int(new_pressure/100)*100)
        str_arr1=["rising","falling"]
        str_arr2=[" more slowly"," slowly",""," quickly"," very rapidly"]
        change_thing1=random.randint(0,1)
        change_thing2=random.randint(0,4)
        pressure_str=pressure_str+" "+str_arr1[change_thing1]+str_arr2[change_thing2]
    else:
       pressure_str="zero"
    #set weather
    if costal_stations[obj_num].has_rain==1:
        weather_thing=random.randint(0,8)
        if weather_thing<2:
            weather_flag=0
        if weather_thing>1 and weather_thing<4:
            weather_flag=1
            fog_flag=1
            weather_condition=costal_stations[obj_num].fog
        if weather_thing==4:
            weather_flag=1
            weather_condition="recent "+costal_stations[obj_num].rain
        if weather_thing==5:
            weather_flag=1
            weather_condition=costal_stations[obj_num].rain
        if weather_thing==6:
            weather_flag=1
            weather_condition="heavy "+costal_stations[obj_num].rain
        if weather_thing==7:
            weather_flag=1
            fog_flag=1
            weather_condition=costal_stations[obj_num].rain+", "+costal_stations[obj_num].fog
    #set visibility units, AU for no or little atmo, miles for thick atmo, 00m for thick atmos with fog
    visibility_unit=" AU"
    if costal_stations[obj_num].has_fog==1:
        visibility_unit=" miles"
        if fog_flag!=0:
            visibility_unit="00 metres"
    visibility=random.randint(1,5)
    if costal_stations[obj_num].has_rain==0 or weather_flag==0:
        report=costal_stations[obj_num].name+": "+costal_wind()+"; "+str(visibility)+visibility_unit+": "+pressure_str
    if costal_stations[obj_num].has_rain==1 and weather_flag==1:
        report=costal_stations[obj_num].name+": "+costal_wind()+"; "+weather_condition+"; "+str(visibility)+visibility_unit+": "+pressure_str
    return report

