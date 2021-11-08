import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import pandas as pd


class Naver_test():
    query = ''
    url = ''
    html = ''
    headers = {'User-Agent': 'Mozilla/5.0'}

    titles = []
    links = []
    shorts = []
    dict = {}
    df = {}


    def set_html(self):
        self.query = '오늘 일기'
        self.url = 'https://search.naver.com/search.naver?query=' + quote(self.query) + '&nso=&where=blog&sm=tab_opt'
        # print(self.url)
        self.html = requests.get(self.url, headers=self.headers).text
        # print(self.html)

    def get_search(self):
        soup = BeautifulSoup(self.html, 'lxml')
        ls1 = soup.find_all(name='div', attrs={'class': 'total_area'})
        for i in ls1:
            self.titles.append(i.find('a', attrs={'class':'api_txt_lines total_tit'}).text)
            self.links.append(i.find('a', attrs={'class':'api_txt_lines total_tit'})['href'])
            self.shorts.append(i.find('a', attrs={'class':'total_dsc'}).text)
        # [print(i) for i in self.titles]
        # [print(i) for i in self.links]
        # [print(i+'\n') for i in self.shorts]


    def get_blog(self):
        # for i in self.links:
        soup = BeautifulSoup(self.links[3], 'lxml')
        ls = soup.find_all(name='p', attrs={'class': 'se-text-paragragh se-text-paragraph-align-center'})
        for i in ls:
            self.blogs.append(i.find('span').text)
        # [print(i) for i in self.blogs]


    def insert_dict(self):
        for i, j in zip(self.titles, self.shorts):
            self.dict[i] = j
        # print(self.dict)

    def dic_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)


    def df_to_csv(self):
        path = f'./naver_test.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN', encoding="utf-8-sig")



if __name__ == '__main__':
    this = Naver_test()
    this.set_html()
    this.get_search()
    # this.get_blog()
    this.insert_dict()
    this.dic_to_dataframe()
    this.df_to_csv()