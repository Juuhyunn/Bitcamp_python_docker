'''
이름, 나이, 주소를 입력받아서 자기 소개하는 프로그램을 작성하시오.
안녕하세요, 제 이름은 Tom이고, 나이는 28세이고, 서울에서 거주합니다.
이때, 여러 사람이면 전부 입력 받아서 전체가 일괄 출력되는 시스템
'''
class Person(object):
    def __init__(self, num):
        self.num = num
        self.people = []
        self.introduce = []

    def addPerson(self, info):
        return self.people.append(info)

    def addHi(self):
        return self.introduce.append(f'안녕하세요, 제 이름은 {self.people[-3]}이고, 나이는 {self.people[-2]}이고, {self.people[-1]}에 거주합니다.')

    def sayHi(self):
        for i in self.introduce:
            print(i)

    @staticmethod
    def main():
        person = Person(int(input("사람은 몇 명입니까?")))
        for j in range(person.num):
            for i in ['이름이 어떻게 됩니까?', '나이가 어떻게 됩니까?', '어디에 삽니까?']:
                person.addPerson(input(f'{i}'))
            person.addHi()
        person.sayHi()

Person.main()