employee = {'name': 'Scott', 'age': 24, 'level': 11, 'salary': 100000}
print(employee)
print(employee['name'])
print(employee['age'])
print(employee['salary'])

employee['date_joined'] = '10th August, 2018'
print(employee)
print(employee['date_joined'])

# starting with empty dictionary

items = {}
items['item1'] = 'book'
items['item2'] = 'pizza'
items['item3'] = 'chivita'
items['item4'] = 'japanese yen'
item = items
print(item)

item['item2'] = 'food'
print(item)

if item['item3'] == 'chivita':
    item['item3'] = 'drinks'

print(item)

# nested dictionaries

users = {
    'user1': {
            'first_name': 'John',
            'last_name': 'Cena',
            'occupation': 'Wrestler'
        },
    'user2': {
            'first_name': 'Katy',
            'last_name': 'Perry',
            'occupation': 'Singer'
        }
    }

print()

print(users['user1'])

for user in users:
    print(user)

print()

for user, user_info in users.items():
    print('User: ', user)
    first_name = user_info['first_name']
    last_name = user_info['last_name']

    print('First name:', first_name)
    print('Last name:', last_name)
    print()

    
    

