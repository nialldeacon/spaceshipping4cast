# spaceshipping4cast
This code produces tweets containing randomly generated shipping forecasts for astrophysical locations. Some of the stuff in it is vaguely scientific, most of it is nonsense.

There are three parts to the shipping forecast; the area forecast, reports from costal stations and the inshore waters forecast. For the purposes of this twitter feed the inshore waters are the spaces in-between planet orbits in the solar system and the costal stations are mostly on moons in the solar system. The area forecasts are all astronomical objects outside the solar system.

Area forecast:
An area forecast has four parts; wind, sea conditions, weather, visibility. The weather is generated inside area_forecast.py as is the force for the wind (higher wind forces are less likely to be generated). The wind force is then passed to wind.py and seastate.py which generate wind and sea conditions based on the wind force. These parts are randomly generated and have no astrophysical meaning. The weather depends on the class of object an area forecast is for. There are
  Hot Jupiters & L dwarfs
  Super-earths
  "earth-like" planets
  "dead" locations: either empty space or planets with little or no atmosphere
  nebulae
  black holes
Some of these classes have some astrophysical things for fog, rain, drizzle and showers, some have no weather at all so always report "fair"
Visibilty is generated in visibility.py. Visibility can only be "very poor" in the presence of fog.

Inshore waters forecast:
Same as area forecasts but with all locations set to class dead

Costal stations:
Costal stations have wind, weather, visibility distance, pressure
Wind is generated in costal_wind.py . Weather and pressure are generated based on classes
  thick atmosphere
  tenuous atmosphere
  no atmosphere
Thick atmosphere stations can have rain or fog (I kind of made up the fog) and have pressure, tenuous atmospheres have pressure and no weather, no atmosphere stations have no weather and no pressure. The pressure readings are in millibars and should be +/-3% of the rough atmospheric pressure I found for each object from a quick google.
Visibilty distance is generated in costal_forecast.py based on presence of fog and/or a thick atmosphere
