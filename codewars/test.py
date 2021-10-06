import unittest
from pagination import PaginationHelper

# Luccas
# Rafa
# Anderson
# Natasha

# -- Round 2 --

# Luccas
# Anderson
# Rafa
# Natasha

# -- Round 3 --

# Luccas
# Anderson
# Rafa
# Natasha

class pagination_helper_tests(unittest.TestCase):

	def test_item_count_two_expected_two(self):
		#Arrange
		expected = 2
		collection = range(1,3)
		helper = PaginationHelper(collection, 10)
		#Act
		result = helper.item_count()
		self.assertEqual(result, expected)

	def test_item_count_five_expected_five(self):
		#Arrange
		expected = 5
		collection = range(1,6)
		helper = PaginationHelper(collection, 10)
		#Act
		result = helper.item_count()
		self.assertEqual(result, expected)

	def test_count_pages_two_expected_two(self):
		#Arrange
		expected = 2
		collection = range(1,7)
		helper = PaginationHelper(collection, 3)
		#Act
		result = helper.page_count()
		self.assertEqual(result, expected)
	
	def test_count_pages_five_expected_five(self):
		#Arrange
		expected = 5
		collection = range(1,11)
		helper = PaginationHelper(collection, 2)
		#Act
		result = helper.page_count()
		self.assertEqual(result, expected)

	def test_count_pages_ten_expected_ten(self):
		#Arrange
		expected = 10
		collection = range(1,11)
		helper = PaginationHelper(collection, 1)
		#Act
		result = helper.page_count()
		self.assertEqual(result, expected)

	def test_count_pages_three_expected_three(self):
		#Arrange
		expected = 3
		collection = range(1,13)
		helper = PaginationHelper(collection, 5)
		#Act
		result = helper.page_count()
		self.assertEqual(result, expected)

	def test_page_count_one_expected_one(self):
		#Arrange
		expected = 1
		collection = range(1)
		helper = PaginationHelper(collection, 6)
		#Act
		result = helper.page_count()
		self.assertEqual(result, expected)

	def test_2_itens_page_1(self):
		#Arrange
		expected = 2
		collection = range(1, 3)
		helper = PaginationHelper(collection, 2)
		#Act
		result = helper.page_item_count(0)
		self.assertEqual(result, expected)
	
	def test_5_itens_page_1(self):
		#Arrange
		expected = 5
		collection = range(1, 11)
		helper = PaginationHelper(collection, 5)
		#Act
		result = helper.page_item_count(0)
		self.assertEqual(result, expected)

	def test_5_itens_page_1_list_with_nine_items(self):
		#Arrange
		expected = 5
		collection = range(1, 10)
		helper = PaginationHelper(collection, 5)
		#Act
		result = helper.page_item_count(0)
		self.assertEqual(result, expected)

	def test_4_itens_page_2_list_with_nine_items(self):
		#Arrange
		expected = 4
		collection = range(1, 10)
		helper = PaginationHelper(collection, 5)
		#Act
		result = helper.page_item_count(1)
		self.assertEqual(result, expected)

	def test_3_itens_page_4_list_with_nine_items(self):
		#Arrange
		expected = 3
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_item_count(3)
		self.assertEqual(result, expected)

	def test_page_item_count_index_maior_que_range(self):	
		#Arrange
		expected = -1
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_item_count(7)
		self.assertEqual(result, expected)

	def test_page_item_count_index_menor_que_zero(self):	
		#Arrange
		expected = -1
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_item_count(-5)
		self.assertEqual(result, expected)

	def test_page_item_index_0(self):	
		#Arrange
		expected = 0
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_index(0)
		self.assertEqual(result, expected)

	def test_page_item_index_7_expect_1(self):	
		#Arrange
		expected = 1
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_index(7)
		self.assertEqual(result, expected)
		
	def test_page_item_index_14_expect_2(self):	
		#Arrange
		expected = 2
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_index(14)
		self.assertEqual(result, expected)

	def test_page_item_index_15_expect_2(self):	
		#Arrange
		expected = 2
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_index(15)
		self.assertEqual(result, expected)

	def test_page_item_index_0_expect_0(self):	
		#Arrange
		expected = 0
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_index(0)
		self.assertEqual(result, expected)

	def test_page_item_index_24_expect_minus1(self):	
		#Arrange
		expected = -1
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_index(24)
		self.assertEqual(result, expected)

	def test_page_item_index_28_expect_minus1(self):	
		#Arrange
		expected = -1
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_index(28)
		self.assertEqual(result, expected)
	
	def test_page_item_index_minus1_expect_minus1(self):	
		#Arrange
		expected = -1
		collection = range(1, 25)
		helper = PaginationHelper(collection, 7)
		#Act
		result = helper.page_index(-1)
		self.assertEqual(result, expected)


# python -m unittest discover . test.py
