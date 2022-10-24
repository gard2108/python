import view,model

def start():
    choice = 1
    while choice != 7:
        choice = view.show_menu()
        match choice:
            case 0:
                phone_book = model.get_phone_book()
                view.show_phone_book(phone_book)
            case 1:
                path = view.input_path()
                model.set_path(path)
                model.open_file()
            case 2:
                 model.save_changes()
            case 3:
                contact = view.input_contact()
                model.new_contact(contact)
            case 4:
                contact = view.input_change()
                model.change_contact(*contact)
            case 5:
                id = view.input__delete()
                model.delete_contact(id)
            case 6:
                contact = view.input_find()
                model.find_contact(*contact)
            case 7:
                break