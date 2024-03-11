from datetime import datetime, timedelta  

users = [  
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith1", "birthday": "1990.03.05"},
    {"name": "Jane Smith1", "birthday": "1990.03.07"},
    {"name": "Jane Smith1", "birthday": "1990.03.10"},
]

def get_upcoming_birthdays(users):
    prepared_users = []  
    for user in users: 
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  
            prepared_users.append({"name": user['name'], 'birthday': birthday})  
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')  





    
    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
