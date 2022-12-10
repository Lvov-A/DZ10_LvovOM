from collections import UserDict

class Field():
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record():

    def __init__(self, name, phone_number):
        self.name = Name(name)
        self.phone_number = Phone([phone_number])
    
    def add_phone_number(self, number):
        self.phone_number.value.append(number)
    
    def delete_phone_number(self, number):
        for i in self.phone_number.value:
            if i == number:
                self.phone_number.value.remove(number)

    def change_phone_number(self, old_number, new_number):
        self.delete_phone_number(old_number)
        self.add_phone_number(new_number)

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as exception:
            return exception.args[0]
    return wrapper


def parser(msg):
    msg = msg.replace("show all", "show_all")
    msg = msg.replace("good bye", "good_bye")
    msg = msg.split(' ')
    command = msg[0].lower()
    name = None
    phone = None
    if len(msg) >= 2:
        name = msg[1]
    if len(msg) == 3:
        phone = msg[2]

    return command, name, phone

def show_all():
    list_contacts = ""
    for key, value in list_user.items():
        list_contacts += f'{key} : {value.phone_number.value} \n'
    return list_contacts[:-2]

@input_error
def show_phone(name):
    res_phone = list_user.get(name)
    if res_phone == None:
        raise ValueError(f"Contact {name} not found")
    else:
        return res_phone.phone_number.value

@input_error
def add_contact(name, phone):
    if not name or not phone:
        raise ValueError("More arguments needed")
    else:
        user = Record(name, phone)
        list_user.add_record(user)
        return "Number saved"


OPERATIONS = {
    "show all": show_all,
    "phone": show_phone,
    "add": add_contact,
    "change": add_contact
}

list_user = AddressBook()

def handler(user_msg):
    list_msg = parser(user_msg)
    if list_msg[0] == "hello":
        return "How can I help you?"   
    elif list_msg[0] == "add":
        return(OPERATIONS["add"](list_msg[1], list_msg[2]))
    elif list_msg[0] == "change":
        return(OPERATIONS["change"](list_msg[1], list_msg[2]))        
    elif list_msg[0] == "phone":
        return(OPERATIONS["phone"](list_msg[1]))  
    elif list_msg[0] == "show_all":
        return(OPERATIONS["show all"]())    
    elif list_msg[0] == "good_bye" or list_msg[0] == "close" or list_msg[0] == "exit":
        return "Good bye!"
    else:
        return "Error command"

def main():
    while True:
        user_msg = input("Enter command:")
        result = handler(user_msg)
        print(result)
        if result == "Good bye!":
            break

if __name__ == "__main__":
    main()