import unittest
from city_functions import get_name

class NameTestCase(unittest.TestCase):
	def test_city_country(self):
		formated_name = get_name('santiago', 'chile')
		self.assertEqual(formated_name, 'Santiago, Chile')

unittest.main()
