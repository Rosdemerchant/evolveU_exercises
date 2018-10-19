import foundation
import unittest

class Testt_logic(unittest.TestCase):

	def test_large(self):
		self.assertEqual(8,foundation.large_num(2,8))
		self.assertEqual(6,foundation.large_num(6,2))
		self.assertEqual(5,foundation.large_num(4,5))
		self.assertEqual(8,foundation.large_num(8,8))

	def test_plus_num(self):
		self.assertEqual(True,foundation.plus_num(4,6,10))
		self.assertEqual(True,foundation.plus_num(4,5,9))
		self.assertEqual(False,foundation.plus_num(8,5,3))

	def test_dress_for_temp(self):
		
		self.assertEqual('shorts',foundation.dress_for_temp(30))
		self.assertEqual('shorts',foundation.dress_for_temp(25))
		self.assertEqual('shorts',foundation.dress_for_temp(20))
		self.assertEqual('tshirt',foundation.dress_for_temp(19))
		self.assertEqual('tshirt',foundation.dress_for_temp(16))
		self.assertEqual('tshirt',foundation.dress_for_temp(15))
		self.assertEqual('coat',foundation.dress_for_temp(10))
		self.assertEqual('coat',foundation.dress_for_temp(5))
		self.assertEqual('coat',foundation.dress_for_temp(-5))
		self.assertEqual('parka',foundation.dress_for_temp(-10))
		self.assertEqual('parka',foundation.dress_for_temp(-15))
		
	def test_dress_for_summer(self):
		self.assertEqual('summer weather',foundation.dress_for_summer(30))
		self.assertEqual('summer weather',foundation.dress_for_summer(20))
		self.assertEqual('long sleeves',foundation.dress_for_summer(19))
		self.assertEqual('long sleeves',foundation.dress_for_summer(15))

	def test_check_temp(self):
		self.assertEqual([12,13,10],foundation.check_temp())
		self.assertEqual(,foundation.check_temp()
		self.assertEqual(,foundation.check_temp(10,14))
		self.assertEqual(,foundation.check_temp(5,9))















	# def test_w_loop(self):
	# 	self.assertEqual(4,found.w_loop(4))
	# 	self.assertEqual(3,found.w_loop(2))

		
	# def test_pet_list(self):
	# 	self.assertEqual("cat",found.pets("turtle"))
	# 	self.assertEqual("cat",found.pets("cat"))

	# def test_pet_list(self):
	# 	self.assertIn(newlist,found.new_l(["Mary"]))
	# 		