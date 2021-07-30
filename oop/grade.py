'''
국어 kor, 영어 eng, 수학 math를 입력받아서
평균정수를 통해서 A-F 학점을 출력하시오
'''

class Grade(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum()/3

    def score(self):
        if int(self.average()) >= int('90'):
            return 'A'
        elif int(self.average()) >= int('80'):
            return 'B'
        elif int(self.average()) >= int('70'):
            return 'C'
        elif int(self.average()) >= int('60'):
            return 'D'
        elif int(self.average()) >= int('50'):
            return 'E'
        elif int(self.average()) >= int('40'):
            return 'F'
        else:
            return 'Fail'

    @staticmethod
    def main():
        kor = input('국어 점수를 입력하세요 : ')
        eng = input('영어 점수를 입력하세요 : ')
        math = input('수학 점수를 입력하세요 : ')
        grade = Grade(kor, eng, math)

        print(f'당신의 점수는 {int(grade.score(grade))}입니다. ')

Grade.main()



