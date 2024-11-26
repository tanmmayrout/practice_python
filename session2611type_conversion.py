# Type conversion practice 26th November
print('What is your birth year')
birth_year = input ('Birth year: ')
print(type(birth_year)) # to print the type

print('Your birth year is ' + birth_year)

#Basic age calculation

age = 2024 - int(birth_year)#Type conversion to convert string to int
print(type(age))

print('Your age is', age )

