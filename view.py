## the ability to see the file

def add_data(inform):
    with open("telephon.txt", "a", encoding="UTF-8") as f:
        f.write(inform)

def searching(search_str):
    with open("telephon.txt", "r", encoding="UTF-8") as f:
        lst_str = f.readlines()
        for inform in lst_str:
            if search_str in inform:
                print(inform)