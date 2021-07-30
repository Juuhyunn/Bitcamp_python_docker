import csv
import matplotlib.pyplot as plt
import numpy


class Population(object):
    data: [] = list()

    def read_data(self):
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간.csv', encoding='utf-8'))
        next(data)
        self.data = data

    def pop_per_dong(self, dong: str) -> []:
        self.read_data()
        for i in self.data:
            if dong in i[0]:
                print('a')
                arr = numpy.array(i[3:], dtype=int) / int(i[2].replace(',', ''))
        # for i in self.data:
        #     arr2 = numpy.array(i[3:], dtype=int) / int(i[2].replace(',', ''))
        #     print('aaa')
        #     print(arr1 - arr2)
        return arr

    def show_plot(self, arr: []):
        plt.rc('font', family='Malgun Gothic')
        plt.title('인구구조')
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()


if __name__ == '__main__':
    pop = Population()
    # pop.pop_per_dong('방이1동')
    pop.show_plot(pop.pop_per_dong('방이1동'))

