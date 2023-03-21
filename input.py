## the file about connection with user

def chase_the_action():
    choice = int(input("Выберите функцию программы: \n 1 - ввод \n 2 - вывод \n 3 - выход \n"))
    return choice

def get_info():
    name = input("фамилия: ")
    surname = input("имя: ")
    phone = input("номер телефона: ")
    inform_str = name + " " + surname + " " + phone + " " + "\n"
    return inform_str

def ask_person():
    search_str = input("что Вы хотите найти? ")
    return search_str

def change_menu():
    choice = int(input("Введите категорию\n1 - изменить данные\n2 - удалить данные\n3 - выход\n"))
    return choice