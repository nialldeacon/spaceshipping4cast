import random
import time
import tweepy
from secrets import *
from area_forecast import area_forecast
from costal_report import costal_report
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
#list classes of costal stations
class costalstation_minimal_atmo:

    rain = ' '        
    fog = ' '
    has_fog=0
    has_rain=0
    has_atmo=1
    def __init__(self, name,pressure):
        self.name = name
        self.pressure=pressure

class costalstation_no_atmo:

    rain = ' '        
    fog = ' '
    has_fog=0
    has_rain=0
    has_atmo=0
    pressure=0.0
    def __init__(self, name):
        self.name = name
class costalstation_thick_atmo:
    has_fog=1
    has_rain=1
    has_atmo=1
    def __init__(self, name,pressure,fog,rain):
        self.name = name
        self.pressure=pressure
        self.fog=fog
        self.rain=rain
#list classes of areas
class Ldwarflike:

    rain = 'molten iron rain'        
    showers = 'molten iron showers'
    drizzle='silicate drizzle'
    fog = 'haze'
    has_fog=1
    has_rain=1
    fair = 'fair'
    def __init__(self, name):
        self.name = name
class neptunelike:
    rain = 'diamond rain'        
    showers = 'squally showers of diamonds'
    drizzle='diamond drizzle'
    fog = 'ammonium sulfide fog'
    has_fog=1
    has_rain=1
    fair = 'fair'
    def __init__(self, name):
        self.name = name
class superearth:
    
    rain = 'rain'      
    showers = 'showers'
    drizzle='drizzle'
    fog = 'haze'
    has_fog=1
    has_rain=1
    fair = 'fair'
    def __init__(self, name):
        self.name = name
class earthlike:
    
    rain = 'rain'      
    showers = 'showers'
    drizzle='drizzle'
    fog = 'fog'
    has_fog=1
    has_rain=1
    fair = 'fair'
    def __init__(self, name):
        self.name = name


class dead:
    
    rain = ' '      
    showers = ' '
    drizzle=' '
    fog = ' '
    has_fog=0
    has_rain=0
    fair = 'fair'
    def __init__(self, name):
        self.name = name


class blackhole:
    
    rain = 'flaring'      
    showers = 'spaghettification'
    drizzle='time running slower'
    fog = ''
    has_fog=0
    has_rain=1
    fair = 'fair'
    def __init__(self, name):
        self.name = name
class nebula:
    
    rain = ' '      
    showers = ' '
    drizzle=' '
    fog = 'nebulosity'
    has_fog=1
    has_rain=0
    fair = 'fair'
    def __init__(self, name):
        self.name = name
gap=' '
delay=3600        #setting time delay between forecasts
#define forecast areas
forecast_areas=[ ]
forecast_areas.append(dead('Proxima b'))
forecast_areas.append(earthlike('WISE0855')) #yes, not earthlike but maybe has water clouds
forecast_areas.append(Ldwarflike('Luhman 16B'))
forecast_areas.append(earthlike('Trappist 1f'))
forecast_areas.append(earthlike('Trappist 1g'))
forecast_areas.append(superearth('GJ 1214b'))
forecast_areas.append(Ldwarflike('PSO 318'))
forecast_areas.append(Ldwarflike('51 Peg b'))
forecast_areas.append(Ldwarflike('HR 8799c'))
forecast_areas.append(Ldwarflike('HD 209458b'))
forecast_areas.append(Ldwarflike('HD 189733b'))
forecast_areas.append(dead('Pleiades'))
forecast_areas.append(nebula('Taurus Molecular Cloud'))
forecast_areas.append(nebula('Chamaeleon Complex'))
forecast_areas.append(dead('Kepler 10b'))
forecast_areas.append(dead('Praesepe'))
forecast_areas.append(neptunelike('Kepler 20d'))
forecast_areas.append(nebula('Orion Nebula'))
forecast_areas.append(superearth('Kepler 36b'))
forecast_areas.append(neptunelike('Kepler 36c'))
forecast_areas.append(dead('Gemini Bight'))
forecast_areas.append(blackhole('Cygnus X-1'))
forecast_areas.append(neptunelike('OGLE-2005-169L b'))
forecast_areas.append(blackhole('V404 Cygni'))
forecast_areas.append(dead('Westerlund 1'))
forecast_areas.append(blackhole('Galactic Centre'))
forecast_areas.append(dead('Large Magellanic Cloud/Small Magellanic Cloud'))
forecast_areas.append(dead('Andromeda Galaxy'))
forecast_areas.append(dead('Southeast Triangulum'))
#define inshore areas
inshore_areas=[ ]
inshore_areas.append(dead('Sun to Mercury'))
inshore_areas.append(dead('Mercury to Venus'))
inshore_areas.append(dead('Venus to Earth including Orkney'))
inshore_areas.append(dead('Earth to Mars'))
inshore_areas.append(dead('Mars to Mull of Ganymede'))
inshore_areas.append(dead('Mull of Ganymede to Saturn'))
inshore_areas.append(dead('Saturn to Great Oberon Head'))
inshore_areas.append(dead('Great Oberon Head to Neptune'))
inshore_areas.append(dead('Neptune to Kuiper Belt'))
inshore_areas.append(dead('Kuiper Belt to Oort Cloud'))
#define costal stations
costal_stations=[ ]
costal_stations.append(costalstation_minimal_atmo('Caloris Basin',0.00000000001))
costal_stations.append(costalstation_thick_atmo('Maxwell Montes',93000,'sulphuric fog','sulphuric rain in upper atmosphere'))
costal_stations.append(costalstation_no_atmo('Mare Tranquillitatis'))
costal_stations.append(costalstation_no_atmo('Phobos'))
costal_stations.append(costalstation_no_atmo('Asteroid belt light vessel automatic'))
costal_stations.append(costalstation_minimal_atmo('Callisto',0.0000000075))
costal_stations.append(costalstation_thick_atmo('Titan automatic',1450,'hydrocarbon fog','methane rain'))
costal_stations.append(costalstation_minimal_atmo('Titania',0.0000000001))
costal_stations.append(costalstation_minimal_atmo('Triton',14))
costal_stations.append(costalstation_minimal_atmo('Charon',0.001))
costal_stations.append(costalstation_no_atmo('Quaoar'))

#generate area forecasts
forecast_start_string="And now the Spaceshipping Forecast, issued by the ExoMet Office on behalf of the Interplanetary and Spaceguard Agency at 0505 today."

api.update_status(forecast_start_string)
time.sleep(61)
n_areas=len(forecast_areas)
n_forecasts=10
use_vec1=random.sample(range(n_areas),n_forecasts)
use_vec=sorted(use_vec1)
#loop over objects in the forecast
for i0 in range(0,n_forecasts):
    forecast_len=10000.0
    while forecast_len>250:
        forecast_string=area_forecast(use_vec[i0],forecast_areas)
        forecast_len=len(forecast_string)
    api.update_status(forecast_string)
    time.sleep(delay)
#generate costal stations
forecast_start_string="Weather reports now for solar system stations for 0400"
api.update_status(forecast_start_string)
time.sleep(61)
n_areas=len(costal_stations)
n_forecasts=6
use_vec1=random.sample(range(n_areas),n_forecasts)
use_vec=sorted(use_vec1)
#loop over objects in the forecast
for i0 in range(0,n_forecasts):
    forecast_len=10000.0
    while forecast_len>250:
        forecast_string=costal_report(use_vec[i0],costal_stations)
        forecast_len=len(forecast_string)
    api.update_status(forecast_string)
    time.sleep(delay)
#generate inshore forecasts
forecast_start_string="And here is the forecast for the inshore waters of the solar system valid for the following 24 hours issued by the ExoMet Office at 0500 today"
api.update_status(forecast_start_string)
time.sleep(61)
n_areas=len(inshore_areas)
n_forecasts=4
use_vec1=random.sample(range(n_areas),n_forecasts)
use_vec=sorted(use_vec1)
#loop over objects in the forecast
for i0 in range(0,n_forecasts):
    forecast_len=10000.0
    while forecast_len>250:
        forecast_string=area_forecast(use_vec[i0],inshore_areas)
        forecast_len=len(forecast_string)
    api.update_status(forecast_string)
    time.sleep(delay)

