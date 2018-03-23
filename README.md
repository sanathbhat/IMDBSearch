# IMDBSearch
A small web scraping project to search IMDB movie titles by various aspects of the movies using BeautifulSoup

You can use the API by simply importing the Top1000Search class, instantiating it and calling the search() method for searching through all aspects of the movies. There are other search methods for individual aspects that return sets instead of lists of movies, however some of them may not be implemented yet.

Usage:

```python
from IMDB_search import Top1000Search
ts = Top1000Search()
print(ts.search('steven'))    
```

This returns ['Raiders of the Lost Ark', 'Jurassic Park', 'The Color Purple', 'Bridge of Spies', 'Indiana Jones and the Last Crusade', 'Jaws', 'Close Encounters of the Third Kind', 'Indiana Jones and the Temple of Doom', "Schindler's List", 'Munich', 'E.T. the Extra-Terrestrial', 'Minority Report', 'Empire of the Sun', 'Saving Private Ryan', 'Traffic', "Ocean's Eleven", 'Catch Me If You Can']

```python
print(ts.search('frank'))
```

Returns ["It's a Wonderful Life", 'Batman: Mask of the Phantasm', 'It Happened One Night', 'Sin City', 'The Green Mile', 'The Shawshank Redemption', 'Arsenic and Old Lace', 'Mr. Smith Goes to Washington']
(movies directed by directors with 'frank' in their name, for eg. frank darabont, frank capra)

# Update:
Added a new class Top1000Search2 that uses Pandas and performs better searches including partial name matches. Eg 'steven' matches 'steven', 'stevens', 'stevenson' etc

The new search has the exact same syntax and a sample is shown in test.py

Performance takes a hit compared to the Top1000Search (takes upto a second for search results compared to a microsecond in Top1000Search). But this search is flexible, scales better for including search over other aspects and is much more simplified and easy to understand without a complicated data structure to create and update.
