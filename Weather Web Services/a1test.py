"""
Pragya Sethi
2018067
Section A Group 3
"""
import unittest
from a1 import weather_response
from a1 import has_error
from a1 import get_temperature 
from a1 import get_humidity
from a1 import get_pressure
from a1 import get_wind
from a1 import get_sealevel


class testpoint(unittest.TestCase):

	
	# Testing the error function

	def test_has_error(self):
		self.assertFalse(has_error("Delhi",weather_response("DeLHi","c21be3f5656ccff4a5fb262f334b1867")))
		self.assertFalse(has_error("New York",weather_response("New%20York","c21be3f5656ccff4a5fb262f334b1867")))
		self.assertFalse(has_error("New York",weather_response("New York","c21be3f5656ccff4a5fb262f334b1867")))
		self.assertTrue(has_error("Kolkata",weather_response("Mumbai","c21be3f5656ccff4a5fb262f334b1867")))
		self.assertTrue(has_error("KOLKATA",weather_response("KOLKATA","c21be3f5656ccff4a5fb262f334b1867")))
		self.assertTrue(has_error("KOLKATA",weather_response("Kolkata","c21be3f5656ccff4a5fb262f334b1867")))


	# Testing the temperature function with appropriate absolute errors

	def test_get_temperature(self):
		self.assertAlmostEqual(get_temperature(weather_response("DeLHi","c21be3f5656ccff4a5fb262f334b1867"), n=3, t="06:00:00"),299.96,delta=7)
		self.assertAlmostEqual(get_temperature(weather_response("Kolkata","c21be3f5656ccff4a5fb262f334b1867"), n=0, t="12:00:00"),302.9,delta=7)
		self.assertAlmostEqual(get_temperature(weather_response("London","c21be3f5656ccff4a5fb262f334b1867"), n=1, t="00:00:00"),285.5,delta=10)
		self.assertAlmostEqual(get_temperature(weather_response("Mumbai","c21be3f5656ccff4a5fb262f334b1867"), n=2, t="21:00:00"),298.8,delta=7)
		self.assertAlmostEqual(get_temperature(weather_response("New York","c21be3f5656ccff4a5fb262f334b1867"), n=4, t="03:00:00"),294.3,delta=10)


	# Testing the humidity function with an absolute error of 15
	
	def test_get_humidity(self):
		self.assertAlmostEqual(get_humidity(weather_response("DeLHi","c21be3f5656ccff4a5fb262f334b1867"),n=1,t="09:00:00"), 80.0,delta=15)
		self.assertAlmostEqual(get_humidity(weather_response("Kolkata","c21be3f5656ccff4a5fb262f334b1867"),n=2,t="18:00:00"),83.0,delta=15)
		self.assertAlmostEqual(get_humidity(weather_response("London","c21be3f5656ccff4a5fb262f334b1867"),n=3,t="09:00:00"), 72.0,delta=15)
		self.assertAlmostEqual(get_humidity(weather_response("New York","c21be3f5656ccff4a5fb262f334b1867"),n=0,t="21:00:00"),81.0,delta=15)
		self.assertAlmostEqual(get_humidity(weather_response("Mumbai","c21be3f5656ccff4a5fb262f334b1867"),n=4,t="00:00:00"),99.0,delta=15)


	# Testing the pressure function with an absolute error of 7

	def test_get_pressure(self):
		self.assertAlmostEqual(get_pressure(weather_response("DeLHi","c21be3f5656ccff4a5fb262f334b1867"),n=1,t="09:00:00"),992.2,delta=7)
		self.assertAlmostEqual(get_pressure(weather_response("Kolkata","c21be3f5656ccff4a5fb262f334b1867"),n=2,t="18:00:00"),1020.0,delta=7)
		self.assertAlmostEqual(get_pressure(weather_response("London","c21be3f5656ccff4a5fb262f334b1867"),n=3,t="09:00:00"),1027.0,delta=7)
		self.assertAlmostEqual(get_pressure(weather_response("New York","c21be3f5656ccff4a5fb262f334b1867"),n=0,t="21:00:00"),1030.0,delta=7)
		self.assertAlmostEqual(get_pressure(weather_response("Mumbai","c21be3f5656ccff4a5fb262f334b1867"),n=4,t="00:00:00"),1022.0,delta=7)
	
	# Testing the wind function with an absolute error of 5

	def test_get_wind(self):
		self.assertAlmostEqual(get_wind(weather_response("DeLHi","c21be3f5656ccff4a5fb262f334b1867"),n=1,t="09:00:00"),5.8,delta=5)
		self.assertAlmostEqual(get_wind(weather_response("Kolkata","c21be3f5656ccff4a5fb262f334b1867"),n=2,t="18:00:00"),3.7,delta=5)
		self.assertAlmostEqual(get_wind(weather_response("London","c21be3f5656ccff4a5fb262f334b1867"),n=3,t="09:00:00"),5.2,delta=5)
		self.assertAlmostEqual(get_wind(weather_response("New York","c21be3f5656ccff4a5fb262f334b1867"),n=0,t="21:00:00"),3.9,delta=5)
		self.assertAlmostEqual(get_wind(weather_response("Mumbai","c21be3f5656ccff4a5fb262f334b1867"),n=4,t="00:00:00"),2.8,delta=5)

	# Testing the sealevel function with an absolute error of 5

	def test_get_sealevel(self):
		self.assertAlmostEqual(get_sealevel(weather_response("DeLHi","c21be3f5656ccff4a5fb262f334b1867"),n=1,t="09:00:00"),1016.4,delta=5)
		self.assertAlmostEqual(get_sealevel(weather_response("Kolkata","c21be3f5656ccff4a5fb262f334b1867"),n=2,t="18:00:00"),1022.1,delta=5)
		self.assertAlmostEqual(get_sealevel(weather_response("London","c21be3f5656ccff4a5fb262f334b1867"),n=3,t="09:00:00"),1035.3,delta=5)
		self.assertAlmostEqual(get_sealevel(weather_response("New York","c21be3f5656ccff4a5fb262f334b1867"),n=0,t="21:00:00"),1033.5,delta=5)
		self.assertAlmostEqual(get_sealevel(weather_response("Mumbai","c21be3f5656ccff4a5fb262f334b1867"),n=4,t="00:00:00"),1023.6,delta=5)

if __name__=='__main__':
	unittest.main()
