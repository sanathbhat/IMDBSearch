import urllib3
from bs4 import BeautifulSoup
import bs4


class Top1000Search:
    dir_name_parts = {}
    dir_movies = {}

    def __init__(self):
        http = urllib3.PoolManager()
        page = 'http://www.imdb.com/search/title?groups=top_1000&sort=user_rating&view=advanced&page='
        for i in range(1, 51):
            url = page + str(i)
            raw_html = http.request('GET', url).data.decode('utf-8')
            soup = BeautifulSoup(raw_html, 'lxml')
            # # parse 50 movies and the director names
            movie_tags = soup.find_all('div', class_='lister-item-content')

            for movie_tag in movie_tags:
                movie = movie_tag.a.string
                directors_tag = movie_tag.contents[9]

                i = 0
                while directors_tag.contents[i].name != 'span':     # contents after <span> are actors, not directors
                    if not isinstance(directors_tag.contents[i], bs4.element.NavigableString):
                        director = directors_tag.contents[i].string.lower()
                        # update the dictionaries
                        if director in self.dir_movies:
                            self.dir_movies[director].append(movie)
                        else:
                            self.dir_movies[director] = [movie]
                            # new director, update the director name parts dictionary
                            name_parts = director.split(' ') + [director]
                            for np in name_parts:
                                if np in self.dir_name_parts:
                                    self.dir_name_parts[np].add(director)
                                else:
                                    self.dir_name_parts[np] = set([director])

                    i += 1


    def search_director(self, name_part):
        if name_part not in self.dir_name_parts:
            return set()
        directors = self.dir_name_parts[name_part]
        movies = set()
        for d in directors:
            movies.update(self.dir_movies[d])
        return movies


    def search_actor(self, name_part):
        # Not yet implemented
        return set()

    def search_genre(self, genre):
        # Not yet implemented
        return set()


    def search(self, term):
        term = term.lower()
        return list(self.search_director(term) | self.search_actor(term) | self.search_genre(term))
