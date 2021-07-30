'''
국어 kor, 영어 eng, 수학 math를 입력받아서
평균정수를 통해서 A-F 학점을 출력하시오
'''

class Grade(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    @staticmethod
    def main():
        kor = input('국어 점수를 입력하세요 : ')
        eng = input('영어 점수를 입력하세요 : ')
        math = input('수학 점수를 입력하세요 : ')
        grade = Grade(kor, eng, math)
        average = int((int(grade.kor) + int(grade.eng) + int(grade.math))/3)
        if int(average) >= int('90'):
            return print('A')
        elif int(average) >= int('80'):
            return print('B')
        elif int(average) >= int('70'):
            return print('C')
        elif int(average) >= int('60'):
            return print('D')
        elif int(average) >= int('50'):
            return print('E')
        elif int(average) >= int('40'):
            return print('F')
        else:
            return print('Fail')


Grade.main()



