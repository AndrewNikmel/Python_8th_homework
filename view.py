## the ability to change the file
import input

def add_data(inform):
    with open("telephon.txt", "a", encoding="UTF-8") as f:
        f.write(inform)

def read_data():
# reads the whole info in the database
    with open("telephon.txt", "r", encoding="utf8") as file:
        content = file.readlines()
        return content

def find_person(persons, name):
# looks for a person based on the name and surname
    simillar_person = list()
    for person in persons:
        if name.lower() in person.lower():
            simillar_person.append(person)
    for i in range(len(simillar_person)):
        print(f"{i + 1} {simillar_person[i]}")
    print("--------------------------")
    while True:
        request = input.change_menu()
        if request == 1:
            if len(simillar_person) > 1:
                choice = int(input("Введите позицию, которую необходимо заменить - "))
            else:
                choice = 1
            print("Введите новые данные")
            new_person = input.get_info()
            change_person(new_person, simillar_person[choice - 1])
            print("--------------------------")
            print("Данные обновлены")
            print(f"Добавлен: {new_person}")
            print("--------------------------")
        elif request == 2:
            if len(simillar_person) > 1:
                choice = int(input("Введите позицию, которую необходимо удалить - "))
            else:
                choice = 1
            delete_person(simillar_person[choice - 1])
            print("--------------------------")
            print("Пользователь удален")
            print("--------------------------")
        else:
            break

def delete_person(name):
# terminates data
    persons = read_data()
    with open("telephon.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
# changes data
    persons = read_data()
    with open("telephon.txt", "w", encoding="utf8" ) as file:
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")