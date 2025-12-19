# Dictionary 
# A mutable data type that can be updated 
# In the context of other languages known as Hashmap and Object also.

cars = {
    'car1' : 'Toyota',
    'car2' : 'Honda',
    'car3' : 'Suzuki',
    'car4' : 'Hyundai',
    'car5' : 'Kia',
    'car6' : 'Ford',
    'car7' : 'BMW',
    'car8' : 'Audi',
    'car9' : 'Tesla',
    'car10': 'Nissan'
}
# print(cars, 'Original List of cars')

cars_detail = {
    'car1' : {'Brand' : 'Toyota',
    'model': 'Corolla',
    'year' : '2020'},

    'car2' : {'Brand' : 'Honda',
    'model' : 'Civic',
    'year' : '2019'},

   'car3' : {'Brand' : 'Suzuki',
    'model' : 'Swift',
    'year' : '2021'},

    'car4' : {'Brand' : 'Hyundai',
    'model' : 'Elantra',
    'year' : '2018'},

    'car5' : {'Brand' : 'Kia',
    'model' : 'Sportage',
    'year' : '2022'},

    'car6' : {'Brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '2017' },

    'car7' : {'Brand' : 'BMW',
    'model' : '3 Series',
    'year' : '2020'},

    'car8' : {'Brand' : 'Audi',
    'model' : 'A4',
    'year' : '2019'},

    'car9' : {'Brand' : 'Tesla',
    'model' : 'Model 3',
    'year' : '2023'},

    'car10' : {'Brand' : 'Nissan',
    'model' : 'Altima',
    'year' : '2016'}
}

# for car in cars_detail:
#     info = cars_detail[car]
#     print(f"{info['Brand']} {info['model']} - {info['year']}")

#Adding a new key-value:


for details in cars_detail.values():
    details['color'] = 'white'

# print(cars_detail)    

#Adding a same value to more than different dictionaries

selected_cars = ['car1', 'car5', 'car9']
for car_id in selected_cars:
    cars_detail[car_id]['color'] = 'Black'
print(cars_detail)


 