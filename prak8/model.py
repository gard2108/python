import control

phone_book = []
path = 'prak8/'

def get_phone_book():
    global phone_book
    return phone_book

def set_path(file):
    global path
    path += file

def open_file():
    global path
    global phone_book
    with open(path,'r',encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)

def save_changes():
    with open (path,'w',encoding='UTF-8') as file:
        for i in range(len(phone_book)):
            for j in range(len(phone_book[i])):
                phone_book[i][j] = f'{phone_book[i][j]};'
            temp = ''.join(phone_book[i]) + '\n'
            print(temp)
            file.write(temp)
        
def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))

def change_contact(id,choice,value):
    global phone_book
    phone_book [int(id)][int(choice)] = value

def delete_contact(id):
    global phone_book
    phone_book.pop(id)

def find_contact(choice,need_find):
    global phone_book
    if choice == 0:
        need_find = int(need_find)
        print(*phone_book[need_find])
    elif choice != 0:
        for i in range(len(phone_book)):
            for j in range(len(phone_book[i])):
                if need_find.lower() in phone_book[i][j].lower():
                    print(phone_book[i])

            

















