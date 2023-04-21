users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]
# TODO найдите пользователя с именем "Olga"
# suitable_users = None
for suitable_users in users:
    if suitable_users['name'] == 'Olga':
        print(suitable_users)
