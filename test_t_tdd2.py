
#begin tdd
import t_tdd2
import unittest
from datetime import datetime


class Testt_tdd2(unittest.TestCase):

	#write a function / method to add 5 to a number. 
	def testplus_five(self):
		self.assertEqual(8,t_tdd2.plus_five(3)) 
	
	#without the max function find the largest number in an array with tdd

	def testmax_function(self):
		self.assertEqual(4,t_tdd2.highestNumber([1,2,3,4,]))

	#without the min function find the smallest number in an array with tdd

	def testmin_function(self):
		self.assertEqual(1,t_tdd2.lowestNumber([1,2,3,4,5]))

	#return all the entries from a list that have the string within it

	def test_string(self):
		self.assertEqual(["Mary had"],
						t_tdd2.has_string(
							["Mary had",
							 "a little lamb",
							 "little lamb",
							 "Whose fleece",
							],"Mary"))


		#isinstance returns a Boolean stating whether the object is an instance or subclass of another object.
		# check whether an object is of type datetime.date
	
	def test_to_date(self):
		dt = t_tdd2.to_date("2010-08-02")
		self.assertIsInstance(dt, datetime.date)
		self.assertEqual(2010,dt.year)
		self.assertEqual(8,dt.month)
		self.assertEqual(2,dt.day)


		#find the number of days between two dates

	def test_date_diff(self):
		self.assertEqual(1, t_tdd2.date_diff("2018-09-02", "2018-09-01"))

		#find the number of days between Sept 1st this year and the mayan end of the world 

	def test_datemayan(self):
		self.assertEqual("2012-12-21",t_tdd2.datemayan,'2018-09-01')

		#check if a value is contained in a list
	
	def test_contains(self):	
		self.assertTrue("c",t_tdd2.contains(['a','b','d']))

		# add the contents of a list
	def listcontents(self):
		self.assertEqual(6, t_tdd2.add_contents([1,2,3]))

			
	def key_mine(self):
		self.assertEqual('one mine', t_tdd2.lookup({1:'one', 2:'two', 3:'three'}, 1))