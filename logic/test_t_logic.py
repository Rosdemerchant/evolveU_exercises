import t_logic
import unittest

class Testt_logic(unittest.TestCase):

	def test_math_operators(self):
		t_logic.math_operators(24, 2)
		t_logic.math_operators(2, 8)
		t_logic.math_operators(8, 4)

	def test_mod(self):
		self.assertEqual(6,t_logic.mod(27, 7))
		self.assertEqual(1,t_logic.mod(5, 2))
		
		
	def test_floor_division(self):
		self.assertEqual(2,t_logic.floor_division(5, 2))
		self.assertEqual(0,t_logic.floor_division(5, 7))

	def test_exponent(self):
		self.assertEqual(8,t_logic.exponent(2, 3))
			

	def test_largest(self):
		self.assertEqual(4,t_logic.large_n(4, 2, 1))
		self.assertEqual(8,t_logic.large_n(2, 4, 8))
		self.assertEqual(10,t_logic.large_n(5, 9, 10))

	# def test_largest(self):
		#self.assertEqual(6,t_logic.num_range,(6,7,8))

	# def test_odd_num(self):
	# 	self.assertEqual(8,t_logic.odd_num,(6,7,8))

	def test_p_list(self):
		t_logic.p_list(1)
		
	def test_biglist(self):
		self.assertEqual(8,t_logic.l_list([7, -7, 8, 2, 1]))
		self.assertEqual(31,t_logic.l_list([2, 3, -2, 31, -31]))
		self.assertEqual(8,t_logic.l_list([7, -7, 8, 2, 1]))

	# def long_str(self):
	# 	t_logic.l_list([7, -7, 8, 2, 1])
	# 	t_logic.l_list([2, 3, -2, 31, -31])
	# 	8,t_logic.l_list([7, -7, 8, 2, 1])
