from bs4 import BeautifulSoup
import requests
import pandas as pd

class Bugsmusic(object):

    url = 'https://music.bugs.co.kr/chart/track/realtime/total?'
    class_name = []  # 파이썬에서 복수의 값을 담는 리스트
    title_list = []
    artist_list = []
    dict = {}   # 딕셔너리 (key, value)
    df = None   # data framework 줄임말로 df 많이씀 / None -> 비어있는 객체

    def set_url(self, detail):
        # detail 은 chartdate=20210605&charthour=11 부분으로 바뀌는 값
        self.url = requests.get(f'{self.url}{detail}').text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        t_list = soup.find_all(name='p', attrs={"class":self.class_name[0]})
        for idx, title in enumerate(t_list):
            # print(f'{idx+1}위 {title.find("a").text}')
            self.title_list.append(title.find("a").text)

        print('='*100)
        a_list = soup.find_all(name='p', attrs={"class": self.class_name[1]})
        for artist in a_list:
            # print(f'{artist.find("a").text}')
            self.artist_list.append(artist.find("a").text)
    def make_dict(self):
        for idx, title in enumerate(self.title_list):
            self.dict[title] = self.artist_list[idx]
        print(self.dict)

    def dict_to_dataframe(self):
        dt = self.dict
        self.df = pd.DataFrame.from_dict(dt, orient='index')

    def df_to_csv(self):
        path = './data/bugs.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')    # na:값이 없는것 / NaN : not a number

    @staticmethod
    def main():
        bugs = Bugsmusic()
        bugs.set_url('chartdate=20210605&charthour=11')
        bugs.class_name = ["title", "artist"]
        bugs.get_ranking()
        bugs.make_dict()
        bugs.dict_to_dataframe()
        bugs.df_to_csv()

Bugsmusic.main()
