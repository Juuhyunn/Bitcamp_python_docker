import matplotlib.pyplot as plt
import random
import csv

from modu.template import ChangedTemperaturesOnMyBirthday


def hist_show(ls: []):
    plt.hist(ls, bins=6, color='lightpink')
    plt.show()


def dice(n: int) -> []:
    ls = []
    [ls.append(random.randint(1, 6)) for i in range(n)]
    return ls


def highest_temperature(month: str) -> []:
    # month = (str('0'+month) if len(month) == 1 else month)
    birth = ChangedTemperaturesOnMyBirthday()
    birth.read_data()
    mon = []
    [mon.append(float(i[-1])) for i in birth.data if i[-1] != '' if month == i[0].split('-')[1]]
    return mon


def hist_show_many(ls):
    [plt.hist(i, bins=100) for i in ls]
    plt.show()


def show_hist_about(arr: [], month: str):
    plt.hist(arr, bins=100, color='pink', label=month)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    # hist_show(dice(int(input('How much?'))))
    # ls = []
    # while 1:
    #     menu = int(input('1. add else. show'))
    #     [ls.append(highest_temperature(input('Month?'))) if menu == 1 else hist_show_many(ls)]
    show_hist_about(highest_temperature('01'), '01')