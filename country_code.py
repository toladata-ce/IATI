import pycountry


def country_code(str):
    mapping = {country.name: country.alpha_2 for country in pycountry.countries}
    return mapping.get(str)
