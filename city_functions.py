def get_name(city, country, population=''):
	if population:
		name = city.title() + ', ' + country.title() + ' - population ' + population
	else:
		name = city.title() + ', ' + country.title() 
	return name

