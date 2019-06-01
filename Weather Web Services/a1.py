"""
Pragya Sethi
2018067
Section A Group 3
"""

from urllib.request import urlopen
from datetime import *

# function to get weather response
def weather_response(location, API_key):
	url='http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key
	Site = urlopen(url)
	json = Site.read()
	return json

# function to check for valid response 
# Returns False when location is correct and True when location is incorrect
def has_error(location,json):
	json_STR=str(json)

	if(json_STR.find(location)>0):
		return False
	else:
		return True

#Finding the present day date
today=date.today()



# function to get attributes on nth day and t th time

# function to get temperature
def get_temperature(json, n=0, t="03:00:00"):


	days=timedelta(n)
	date=str(today+days)				#finding the required date and converting it into a string
	ToFind=date+' '+t
	json_STR=str(json)
	i1=json_STR.index(ToFind)			#finding the index of required date and time in string
	slice1=json_STR[:i1]				#Omitting later dates and time from the string
	l=slice1.split('\"temp\":')			#Splitting the string at different temperatures
	temp=float(l[-1][:5])				#Last element in the list constitutes the required temperature. Slicing to get the temperature.
	return temp

# function to get humidity
def get_humidity(json, n=0, t="03:00:00"):
	days=timedelta(n)
	date=str(today+days)
	ToFind=date+' '+t
	json_STR=str(json)
	i1=json_STR.index(ToFind)
	slice1=json_STR[:i1]
	l=slice1.split('\"humidity\":')
	humidity=float(l[-1][:2])
	return humidity

# function to get pressure
def get_pressure(json, n=0, t="03:00:00"):
	days=timedelta(n)
	date=str(today+days)
	ToFind=date+' '+t
	json_STR=str(json)
	i1=json_STR.index(ToFind)
	slice1=json_STR[:i1]
	l=slice1.split('\"pressure\":')
	pressure=float(l[-1][:5])
	return pressure

# function to get wind speed
def get_wind(json, n=0, t="03:00:00"):
	days=timedelta(n)
	date=str(today+days)
	ToFind=date+' '+t
	json_STR=str(json)
	i1=json_STR.index(ToFind)
	slice1=json_STR[:i1]
	l=slice1.split('\"speed\":')
	wind_speed=float(l[-1][:3])
	return wind_speed 

# function to get sea level
def get_sealevel(json, n=0, t="03:00:00"):
	days=timedelta(n)
	date=str(today+days)
	ToFind=date+' '+t
	json_STR=str(json)
	i1=json_STR.index(ToFind)
	slice1=json_STR[:i1]
	l=slice1.split('\"sea_level\":')
	sea_level=float(l[-1][:6])
	return sea_level

