import urllib3
from bs4 import BeautifulSoup
import bs4
from index import CustomInvertedIndex
from enum import Enum
from utils import remove_stop_words


class Priority(Enum):
    Title = 10
    Actor = 9
    Director = 8
    Genre = 2


class Top1000Search3:

    def __init__(self):
        self.index = CustomInvertedIndex()
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
                title_terms = remove_stop_words(movie.lower().split(' '))
                directors_actors_tag = movie_tag.contents[9]

                directors = []
                actors = []
                currently_filling = directors
                for tag in directors_actors_tag.contents:
                    if tag.name == 'span':
                        currently_filling = actors
                        continue
                    if not isinstance(tag, bs4.element.NavigableString):
                        person = tag.string.lower()
                        currently_filling.append(person)

                genre_tag = movie_tag.contents[3].find(class_='genre')
                genres = genre_tag.string.lstrip('\n').rstrip().lower().split(', ')

                # time to update the index with the parsed values
                self.index.update(title_terms, movie, Priority.Title.value)
                for actor in actors:
                    self.index.update(actor.split(' '), movie, Priority.Actor.value)

                for director in directors:
                    self.index.update(director.split(' '), movie, Priority.Director.value)

                self.index.update(genres, movie, Priority.Genre.value)


    def search(self, terms):
        results = self.index.lookup(terms.split(' '))
        if len(results)>0:
            return [r[0] for r in results]
        return 'No results found'
