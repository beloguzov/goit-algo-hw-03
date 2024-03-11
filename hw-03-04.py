from datetime import datetime, timedelta  

users = [  
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith1", "birthday": "1990.03.05"},
    {"name": "Jane Smith1", "birthday": "1990.03.07"},
    {"name": "Jane Smith1", "birthday": "1990.03.10"},
]

def prepare_users(users):
    prepared_users = []  
    for user in users: 
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  # Парсимо дату народження
            prepared_users.append({"name": user['name'], 'birthday': birthday})  # Додаємо користувача з підготовленою датою народження
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')  # Виводимо повідомлення про помилку
    return prepared_users
