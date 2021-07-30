class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def to_string(self):
        print(f'name : {self.name} age : {self.age} address : {self.address}')
def main():
    people = []
    while 1:
        menu = input('0 1 2 ')
        if menu == '0':
            return
        elif menu == '1':
            people.append(Person(input('name : '), input('age : '), input('address :')))
        elif menu == '2':
            for i in people:
                i.to_string()
if __name__ == '__main__':
    main()