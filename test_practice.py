
import practice
import unittest

class Test_practice(unittest.TestCase):

	def test_bigger(self):
		self.assertEqual(7,practice.bigger(3,7))
		self.assertEqual(20,practice.bigger(20,19))
		self.assertEqual(37,practice.bigger(37,6))
		self.assertEqual(-7,practice.bigger(-7, -13))
		self.assertEqual(1,practice.bigger(-1, 1))

	def test_biglist(self):
		self.assertEqual(8,practice.biglist([7, -7, 8, 2, 1]))
		self.assertEqual(31,practice.biglist([2, 3, -2, 31, -31]))
		self.assertEqual(8,practice.biglist([7, -7, 8, 2, 1]))

	def test_occur(self):
		self.assertEqual({3:2, 5:1, 7:1, 4:1, 51:1},practice.count_occ([4, 3, 51, 3, 5, 7]))		
		self.assertEqual({3:2, 5:1, 7:1, 4:1, 51:1},practice.count_occ([4, 3, 51, 3, 5, 7]))	
		self.assertEqual({3:2, 5:1, 7:1, 4:1, 51:1},practice.count_occ([4, 3, 51, 3, 5, 7]))	