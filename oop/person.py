'''
이름, 나이, 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오.
안녕하세요, 제 이름은 Tom이고, 나이는 28세이고, 서울에서 거주합니다.
이때, 여러 사람이면 전부 입력 받아서 전체가 일괄 출력되는 시스템
'''
class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.people = []

    def to_string(self, param):
        return str(f'안녕하세요, 제 이름은 {param.name}이고, 나이는 {param.age}세 이고, {param.address}에서 거주합니다.')

    def addPerson(self, param):
        return self.people.append(param)

    @staticmethod
    def main():
        count = int(input("몇 명입니까?"))
        result = []
        for i in range(count):
            person = Person(input("이름은?"), input('나이는?'), input('주소는?'))
            result.append(person.to_string(person))
        for i in result:
            print(i)

Person.main()