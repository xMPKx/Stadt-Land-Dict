cities = ["Berlin", "Paris", "London", "Madrid", "Rome", "Oslo"]
countries = ["Germany", "France", "United Kingdom", "Spain", "Italy", "Denmark"]
d={}


def create_city_country_dict(cities, countries):
    
    
    

    for i in range(len(cities)):
        d[cities[i]] = countries[i]

    return d

   

result = create_city_country_dict(cities, countries)
print(result)


def new_combinations():

    d["Tokyo"] = "Japan"

    return d

result=new_combinations()
print(result)


def del_eintrag(city, country):

    if city in d and d[city] == country:
        del d[city]
        print(f"{city} - {country} wurde eben gelöscht")

    else:
        print(f" {city} - {country} Kombination ist nicht im dic vorhanden")

    return d


result= del_eintrag("Oslo", "Denmark")
print(result)

