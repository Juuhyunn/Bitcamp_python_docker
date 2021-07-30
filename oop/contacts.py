class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        return print(f'!name : {self.name}\tphone : {self.phone}\temail : {self.email}\taddress : {self.address}')


def set_contact() -> object:
    return Contacts(input('name : '), input('phone :'), input('email : '), input('address : '))


def get_contact(ls):
    for i in ls:
        Contacts(input('name : '), input('phone :'), input('email : '), input('address : ')). to_string()
        i.to_string()


def del_contact(contacts, n):
    for i, j in enumerate(contacts):
        if n == j.name:
            del contacts[i]
            print('!!Delete Complete!!')
    '''
    for i in contacts:
    if name == i.name:
        contacts.remove(i)
        print('!!Delete Complete!!')
    '''


def menu(ls) -> int:
    for i, j in enumerate(ls):
        print(f'{i}.  {j}')
    return int(input())
    '''
    lis = []
    for i in ls:
        print(f'{ls.index(i)}. {i}\t')
    '''


def main():
    ls = []
    #c = Contacts()
    while 1:
        m = menu(['Exit', 'Add', 'Print', 'Delete'])
        if m == 0:
            return
        elif m == 1:
            t = set_contact()
            ls.append(t)
            print()
        elif m == 2:
            get_contact(ls)
            print()
        elif m == 3:
            del_contact(ls, input('Del Name : '))
            print()
        else:
            print('Wrong Input')
            break

if __name__ == '__main__':
    main()