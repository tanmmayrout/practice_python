# Strings practice 26th November

# Strings initialisation

name = "My name is Tanmmay"  #With ""
print(name)

name_1 = 'My name is "Tanmmay"' #with ''
print(name_1)

long_name = '''  
My 
name 
is
Tanmmay
'''  #Print multiple lines
print(long_name)
print(type(long_name))

#Indexing practice

random_stuff= 'My name is Tanmmay' #string has indexes from 01234....
print(random_stuff)

print('Indexing the first value of the string')
print(random_stuff[0])  #Indexes start from 0
print('Indexing the last value of the string')
print(random_stuff[-1]) #Indexes  the last value of the string
#Negative value indexing only in Python
print(random_stuff[0:]) #Returns values till the end of the string
print(random_stuff[0:5]) #Returns values until 5 index excluding the index at 5
print(random_stuff[2:])  #Returns all values and excludes the values from 0 to 2
# '' is also a value in the string
print(random_stuff[:5])  #Starts at 0 and ends at 5 excludes 5
print(random_stuff[:]) # Prints the string in its entirety

