my_dict = {'Kristina':2002, 'Irina':2000}
print(my_dict)
print(my_dict['Kristina'], my_dict.get('Andrey'))
my_dict.update({'Yana':2001, 'Andrey':1999})
del my_dict['Andrey']
print(my_dict.get('Andrey'))
print(my_dict)

my_set = {1, 1, 2, 3, 3, 3, 4, 5}
print(my_set)
my_set.update([6, 7])
my_set.remove(4)
print(my_set)

