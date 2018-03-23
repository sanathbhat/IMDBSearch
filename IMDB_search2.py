import urllib3
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import numpy as np


class Top1000Search2:

    def __init__(self):
        http = urllib3.PoolManager()
        page = 'http://www.imdb.com/search/title?groups=top_1000&sort=user_rating&view=advanced&page='
        rows = []
        for i in range(1, 21):
            url = page + str(i)
            raw_html = http.request('GET', url).data.decode('utf-8')
            soup = BeautifulSoup(raw_html, 'lxml')

            movie_tags = soup.find_all('div', class_='lister-item-content')

            for movie_tag in movie_tags:
                movie = movie_tag.a.string
                directors_tag = movie_tag.contents[9]

                i = 0
                directors = []
                while directors_tag.contents[i].name != 'span':
                    if not isinstance(directors_tag.contents[i], bs4.element.NavigableString):
                        director = directors_tag.contents[i].string.lower()
                        directors.append(director)
                    i += 1

                rows.append([movie, ','.join(directors)])

        self.df_Movies = pd.DataFrame(rows, columns=['Movie', 'Directors'], dtype=np.str)


    def search(self, term):
        term = term.lower()
        df_filtered = self.df_Movies[self.df_Movies['Directors'].str.contains(term)]
        return list(df_filtered['Movie'])

