import swapi
pm = swapi.get_film(4)
jj = swapi.get_person(36)
for c in pm.get_characters().iter():
    if c.name == jj.name:
        print("Why George, why.")