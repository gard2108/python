def show_menu():
    print("0 - Показать все контакты")
    print("1 - Открыть файл с контактами")
    print("2 - Записать файл с контактами")
    print("3 - Добавить контакт")
    print("4 - Изменить контакт")
    print("5 - Удалить контакт")
    print("6 - Поиск по контактам")
    print("7 - Закрыть меню")
    choice = int(input('Введите пункт меню: '))
    return choice

def show_phone_book(phone_book):
    if len(phone_book)<1:
        print("Книга пуста")
    else:
        for id,item in enumerate (phone_book):
            print(id, *item)

def input_path():
    path = input('Введите имя файла: ')
    return path

def input_contact():
    name_contact = input('Введите ФИО контакта: ')
    phone_contact = input('Введите номер контакта: ')
    comment_contact = input('Введите комментарий: ')
    return (name_contact, phone_contact, comment_contact)

def input_change():
    id = int(input('Введите номер контакта: '))
    print("Что изменить?")
    choice = input('0 - имя, 1 - телефон, 2 - комментарий, 3 - отмена')
    value = input('Введите изменения: ')
    return (id,choice, value)

def input__delete():
    id = int(input('Введите номер контакта: '))
    return(id)

def input_find():
    choice = int(input('Искать по: 0 - порядковый номер, 1 - Имя,номер,комментарий: '))
    need_find = input('Введите цифру(ы) или слова полностью или целиком: ')
    return (choice,need_find)













