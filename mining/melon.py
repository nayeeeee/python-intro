from bs4 import BeautifulSoup
import requests

class Melon(object):
    url = 'https://www.melon.com/chart/index.htm?'
    headers = {'User-Agent':'Mozilla/5.0'}  # 벅스와 달리 멜론에서 설정해야 하는 헤더값
    class_name = []

    def set_url(self, detail):
        # headers 는 멜론에서 스크래핑을 할 때 필요한 속성값
        self.url = requests.get(f'{self.url}{detail}', headers=self.headers).text

    def get_ranking(self):
        soup = BeautifulSoup(self.url, 'lxml')
        ls1 = soup.find_all(name='div', attrs={"class":"ellipsis rank01"})
        for idx, title in enumerate(ls1):
            print(f'{idx+1}위 {title.find("a").text}')   # idx는 0부터 시작함


    @staticmethod
    def main():
        melon = Melon()
        melon.set_url('dayTime=2021060515')
        melon.get_ranking()

Melon.main()