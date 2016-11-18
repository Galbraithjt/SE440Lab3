#barometer class
class Barometer(object):
    __air_pressure = 0.0

    def set_air_pressure(self, air_pressure):
        __air_pressure = air_pressure #used to get air pressure from instrument

    def get_air_pressure(self):
        return self.__air_pressure


#temp class
class Temp(object):
    __air_temp = 0.0

    def set_air_temp(self, air_temp):
        __air_temp = air_temp #used to get air temp from instrument

    def get_air_temp(self):
        return self.__air_temp


#precip class
class Precipitation(object):
    __precipitation_chance = 0.0

    def set_precipitation_chance(self, precipitation_chance):
        __precipitation_chance = precipitation_chance #used to get precipitation chance from instrument

    def get_precipitation_chance(self):
        return self.__precipitation_chance


#weather report class
class WeatherReport(object):
    __air_pressure = Barometer.get_air_pressure #gets air pressure from baromete
    __air_temp = Temp.get_air_temp #gets air temp from temp
    __precipitation_chance = Precipitation.get_precipitation_chance #get precipitation chance from precip class

    def request_air_pressure(self): #prints air pressure
        print("current air pressure is {}".format(self.__air_pressure) )

    def request_air_temp(self): #prints air temp
        print("current air temp is {}".format(self.__air_temp))

    def request_precipitation_chance(self): #prints precip chance
        print("current precipitation chance is {}".format(self.__precipitation_chance))

    def generate_weather_report(self): #prints air pressure temp and precip chance
        print("{}, {}, {}".format(self.request_air_pressure, self.request_air_temp, self.request_precipitation_chance))


class WeatherStation(object):
    __weather_report = WeatherReport

    def request_weather_report(self):
        print(self.weather_report.generate_weather_report())

#main

print(WeatherReport.generate_weather_report)