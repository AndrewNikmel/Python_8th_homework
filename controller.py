## the ability of connection to the file
import input
import view

print("Hello! Nice to meet you! Let's work!")

def main():
    while True:
        choice = input.chase_the_action()
        if choice == 1:
            inform = input.get_info()
            view.add_data(inform)
        elif choice == 2:
            users = view.read_data()
            # print(users)
            name = input.ask_person()
            view.find_person(users, name )
        elif choice == 3 or choice not in range(1,3):
            break


if __name__=="__main__":
    main()
