'''
국어 kor, 영어 eng, 수학 math를 입력받아서
평균정수를 통해서 A-F 학점을 출력하시오
학생 이름, 평균 점수 ,학점을 출력하시오
'''

class Grade(object):
    def __init__(self, name):
        self.name = name
        self.scores = []

    def addScore(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)

    def result(self, avg):
        if int(avg) >= int('90'):
            return 'A'
        elif int(avg) >= int('80'):
            return 'B'
        elif int(avg) >= int('70'):
            return 'C'
        elif int(avg) >= int('60'):
            return 'D'
        elif int(avg) >= int('50'):
            return 'E'
        elif int(avg) >= int('40'):
            return 'F'
        else:
            return 'Fail'

    @staticmethod
    def main():
        people = []
        for j in [1, 2, 3]:
            grade = Grade(input('성명을 입력하세요 : '))
            for i in ['Korean', 'English', 'Math', 'Science']:
                grade.addScore(int(input(f'{i} 점수를 입력하세요 : ')))
            avg = grade.avg()
            people.append(f'[{grade.name}의 성적표] 평균 점수 : {grade.avg()}  학점 : {grade.result(grade.avg())}')

        for k in people:
            print(k)

Grade.main()