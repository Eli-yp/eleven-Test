import unittest
from city_functions import get_name

class NameTestCase(unittest.TestCase):
	def test_city_country(self):
		formated_name = get_name('santiago', 'chile')
		self.assertEqual(formated_name, 'Santiago, Chile')

	def test_city_country_population(self):
		formated_name = get_name('santiago', 'chile', '500000')
		self.assertEqual(formated_name, 'Santiago, Chile - population 500000')

unittest.main()
