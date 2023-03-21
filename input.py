## the file about connection with user

def chase_the_action():
    choice = int(input("Выберите функцию программы: \n 1 - ввод \n 2 - вывод \n 3 - выход"))
    return choice

def get_info():
    name = input("фамилия: ")
    surname = input("имя: ")
    phone = input("номер телефона: ")
    inform_str = name + " " + surname + " " + phone + " " + "\n"
    return inform_str

def search():
    search_str = input("что Вы хотите найти? ")
    return search_str