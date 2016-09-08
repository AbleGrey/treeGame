import random

#for reference, see
#http://sciencelearn.org.nz/Contexts/Soil-Farming-and-Science/Science-Ideas-and-Concepts/Soil-properties

##Weather
#cloud cover
    #fog, rainclouds, shadeclouds, stormclouds
#precipitation
    #rain, snow, sleet, hail
#sun
    #factor in cloud effects
#windspeed
#atmospheric ionization
#temperature
    #factor in wind chill, sunlight intensity mitigated by cloud cover
#humidity


##Soil
#water levels
#air levels
#chemistry
    #acidity
#mineral/organic balance
#organisms
    #microfauna,invertibrates,bigger burrowers? (need oxygen btw)
#texture (loam particle size of sand>silt>clay)
    #fluid retention, root impedance, affects hardness as f(water level)
    #nutrient retention (P,N)
#structure
    #(clay, organic matter, and organism excretions increase binding)
    #friable (crumbly/fine aggregate) vs coarse or firm clods vs super loose
#porosity
    #compacted vs visible pores/cracks/holes (affects drainage)

class NeighborModel:
    def __init__(self,style='default',seed=113090):
        self.initialSeed = seed
        self.rGenerator = random.Random(initialSeed)
        self.style = style
    def resetSeed(self, newSeed):
        self.rGenerator.seed(newSeed)
    #def getEvent(self,style):


class WeatherModel:
    def __init__(self,style='default',seed=113090):
        self.initialSeed = seed
        self.rGenerator = random.Random(initialSeed)
        self.style = style
    def resetSeed(self, newSeed):
        self.rGenerator.seed(newSeed)
    #def getEvent(self,style):
        
class SoilModel:
    def __init__(self,style='default',seed=113090):
        self.initialSeed = seed
        self.rGenerator = random.Random(initialSeed)
        self.style = style
    def resetSeed(self, newSeed):
        self.rGenerator.seed(newSeed)
