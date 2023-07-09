# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)

user_data = {
    0: {'name': 'Pavel', 'surname': 'Pupkin', 'tel': 123456, 'e-mail': 'aaaa@kdkj.com'},
    1: {'name': 'Vasya', 'surname': 'Mutin', 'tel': 123459, 'e-mail': 'bbb@kdkj.com'},
    2: {'name': 'Masha', 'surname': 'Gutina', 'tel': 123458, 'e-mail': 'vvv@kdkj.com'},
    3: {'name': 'Vlad', 'surname': 'Sutin', 'tel': 123457},
    4: {'name': 'Vika', 'surname': 'Vutina', 'tel': 123456, 'e-mail': ''},
    5: {'name': 'Milka', 'surname': 'Rutina', 'tel': 123455, 'e-mail': 'ccc@kdkj.com'},
    6: {'name': 'Tom', 'surname': 'Nutin', 'tel': 123454, 'e-mail': 'ooo@kdkj.com'}
}


def no_imail(user_data):
    for i, j in user_data.items():
        if 'e-mail' not in j.keys() or j.get('e-mail') == '':
            print(j.get('name'))


no_imail(user_data)
