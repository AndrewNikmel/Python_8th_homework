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
        if choice == 2:
            searcher = input.search()
            view.searching(searcher)
        if choice == 3:
            break


if __name__=="__main__":
    main()
