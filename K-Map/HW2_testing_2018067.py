#Name: Pragya Sethi
#Roll_N0 : 2018067
#Section: A
#Group: 3
#Date: 15-10-18

import unittest
from HW2_2018067 import *



class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(4,'(4,8,10,11,12,15)d(9,14)'),"""wx'+wy+xy'z' OR wy+wz'+xy'z'""")
		self.assertEqual(minFunc(4,'(4,8,10,11)d(9,14)'),"""w'xy'z'+wx'""")
		self.assertEqual(minFunc(3,'(0,1,2,5,6,7)d-'),"""w'x'+wy+xy' OR w'y'+wx+x'y""")
		self.assertEqual(minFunc(2,'(0,1,2)d(3)'),'1')
		self.assertEqual(minFunc(2,'(0)d(3)'),"""w'x'""")
		self.assertEqual(minFunc(3,'(1,2,5,6)d(0,4,3,7)'),'1')
		self.assertEqual(minFunc(3,'(1)d-'),"""w'x'y""")
		self.assertEqual(minFunc(4,'(0,1,2,4,5,6,8,9,12,13,14)d-'),"""w'z'+xz'+y'""")
		self.assertEqual(minFunc(4,'(1,3,7,11,15)d(0,2,5)'),"""w'x'+yz OR w'z+yz""")

		
                
if __name__=='__main__':
	unittest.main()
