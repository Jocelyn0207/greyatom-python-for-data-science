# --------------
class_1 = ['Geoffery Hinnton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = ['Hilary Mason', 'Carla Gentry', 'Corinna Cortes']
new_class = class_1 + class_2
print(new_class)
a = new_class.append('Peter Warden')
print(new_class)
b = new_class.remove('Carla Gentry')
print(new_class)

# Geoffrey Hinton grades

courses = {'Math': 65, 'English': 70, 'History': 80, 'French': 70, 'Science': 60}
print(courses)
total = 65+70+80+70+60
print(total)
percentage = (total/500)*100
print(percentage)

# highest marks in math

mathematics = {'Geoffery Hinnton': 78, 'Andrew Ng': 95, 'Sebastian Raschka':65, 'Yoshua Bengio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}
print(mathematics)
topper = max(mathematics, key = mathematics.get)
print("The topper is ", topper)

# certificate name 

first_name = 'Andrew'
last_name = 'Ng'
full_name =  'Ng' + ' ' + 'Andrew'
certificate_name = full_name.upper()
print(certificate_name)




