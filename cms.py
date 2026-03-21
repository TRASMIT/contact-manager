contacts = {}
print("contact manager started")

def add_contact():
    name = input("name:")
    phone = input("phone:")
    email = input("email:")
    contacts[name] = {"phone": phone, "email": email}
    print(name + ' is added')

    print('1. enter 1 add another contact')
    print('2. enter any key to exit')
    choice = input("enter your choice:")

    match choice:
        case '1':
            add_contact()
        case _:
            return


def view_contacts():
    for name, info in contacts.items():
        print(name, info['phone'], info['email'])


def search_contact():
    print("enter 1 to search by name:")
    print("enter 2 to search by phone number")
    print("enter 3 to search by email")

    choice = input('enter choice:')

    match choice:
        case '1':
            name = input("enter name:")
            f = 0
            for n, info in contacts.items():
                if name in n:
                    f += 1
                    print(n, info['phone'], info['email'])
            if f == 0:
                print("no contact found")

        case '2':
            num = input("enter phone number:")
            f = 0
            for name, info in contacts.items():
                if num in str(info['phone']):
                    f += 1
                    print(name, info['phone'], info['email'])
            if f == 0:
                print("no contact found")

        case '3':
            e = input('enter email:')
            f = 0
            for name, info in contacts.items():
                if e in info['email']:
                    f += 1
                    print(name, info['phone'], info['email'])
            if f == 0:
                print("no contact found")

        case _:
            print('error')


def delete_or_edit():
    print('enter 1 to delete a contact')
    print('enter 2 to edit a contact')
    choice = input('enter your choice:')

    match choice:
        case '1':
            print("enter 1 to search by name:")
            print("enter 2 to search by phone number")
            print("enter 3 to search by email")
            c = input('enter choice:')

            match c:
                case '1':
                    name = input("enter name:")
                    f = 0
                    for n, info in list(contacts.items()):
                        if name in n:
                            f += 1
                            print("do you want to delete", n, info['phone'], info['email'])
                            print("enter 1 to delete")
                            print("enter any key to exit")
                            d = input("enter your choice:")

                            match d:
                                case '1':
                                    list(contacts.pop(n))
                                case _:
                                    pass
                    if f == 0:
                        print("no contact found")

                case '2':
                    num = input("enter phone number:")
                    f = 0
                    for name, info in list(contacts.items()):
                        if num in str(info['phone']):
                            f += 1
                            print("do you want to delete", name, info['phone'], info['email'])
                            print("enter 1 to delete")
                            print("enter any key to exit")
                            d = input("enter your choice:")

                            match d:
                                case '1':
                                    list(contacts.pop(name))
                                case _:
                                    pass
                    if f == 0:
                        print("no contact found")

                case '3':
                    e = input('enter email:')
                    f = 0
                    for name, info in list(contacts.items()):
                        if e in info['email']:
                            f += 1
                            print("do you want to delete", name, info['phone'], info['email'])
                            print("enter 1 to delete")
                            print("enter any key to exit")
                            d = input("enter your choice:")

                            match d:
                                case '1':
                                    list(contacts.pop(name))
                                case _:
                                    pass
                    if f == 0:
                        print("no contact found")

                case _:
                    print('error')

        case '2':
            print("enter 1 to search by name:")
            print("enter 2 to search by phone number")
            print("enter 3 to search by email")

            choice = input('enter choice:')

            match choice:
                case '1':
                    name = input("enter name:")
                    f = 0
                    for n, info in list(contacts.items()):
                        if name in n:
                            f += 1
                            print("do you want to edit", n, info['phone'], info['email'])
                            print("enter 1 to edit")
                            print("enter any key to exit")
                            d = input("enter your choice:")

                            match d:
                                case '1':
                                    print("enter 1 to edit the name")
                                    print('enter 2 to edit phone number')
                                    print('enter 3 to edit email')
                                    e = input("enter your choice:")

                                    match e:
                                        case '1':
                                            newn = input("enter the new name:")
                                            contacts[newn] = contacts[n]
                                            list(contacts.pop(n))
                                        case '2':
                                            newp = input("enter new phone number:")
                                            info['phone'] = newp
                                        case '3':
                                            newe = input("enter new email:")
                                            info['email'] = newe
                                        case _:
                                            pass
                                case _:
                                    pass

                    if f == 0:
                        print("no contact found")

                case '2':
                    num = input("enter phone number:")
                    f = 0
                    for name, info in list(contacts.items()):
                        if num in str(info['phone']):
                            f += 1
                            print("do you want to edit", n, info['phone'], info['email'])
                            print("enter 1 to edit")
                            print("enter any key to exit")
                            d = input("enter your choice:")

                            match d:
                                case '1':
                                    print("enter 1 to edit the name")
                                    print('enter 2 to edit phone number')
                                    print('enter 3 to edit email')
                                    e = input("enter your choice:")

                                    match e:
                                        case '1':
                                            newn = input("enter the new name:")
                                            contacts[newn] = contacts[n]
                                            list(contacts.pop(n))
                                        case '2':
                                            newp = input("enter new phone number:")
                                            info['phone'] = newp
                                        case '3':
                                            newe = input("enter new email:")
                                            info['email'] = newe
                                        case _:
                                            pass
                                case _:
                                    pass

                    if f == 0:
                        print("no contact found")

                case '3':
                    e = input('enter email:')
                    f = 0
                    for name, info in list(contacts.items()):
                        if e in info['email']:
                            f += 1
                            print("do you want to edit", name, info['phone'], info['email'])
                            print("enter 1 to edit")
                            print("enter any key to exit")
                            d = input("enter your choice:")

                            match d:
                                case '1':
                                    print("enter 1 to edit the name")
                                    print('enter 2 to edit phone number')
                                    print('enter 3 to edit email')
                                    e = input("enter your choice:")

                                    match e:
                                        case '1':
                                            newn = input("enter the new name:")
                                            contacts[newn] = contacts[name]
                                            list(contacts.pop(name))
                                        case '2':
                                            newp = input("enter new phone number:")
                                            info['phone'] = newp
                                        case '3':
                                            newe = input("enter new email:")
                                            info['email'] = newe
                                        case _:
                                            pass
                                case _:
                                    pass

                    if f == 0:
                        print("no contact found")

                case _:
                    print('error')


add_contact()
view_contacts()
search_contact()
delete_or_edit()
view_contacts()