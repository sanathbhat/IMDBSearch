# IMDBSearch
A small web scraping project to search IMDB movie titles from the [Top 1000 movies list](http://www.imdb.com/search/title?groups=top_1000&sort=user_rating&view=simple) by various aspects of the movies using BeautifulSoup

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


# Update 2:
Added a new search class which searches movies using an inverted index with following features.
1. The search results are ranked based on the relationship between all the terms and the movie ranking. Highest priority results are those which are related to all the terms rather than a few.
2. Also there is a inherent priority based on which terms match. For eg a title match is better than actor match. (Priority can be changed in code)
3. For results of equal priority, ranking is based on movie rating

Examples
```python
from IMDB_search import Top1000Search3
ts3 = Top1000Search3()
print(ts3.search('spielberg'))           # movies with 'spielberg' ranked in order of rating
print(ts3.search('spielberg hanks'))     # movies with 'spielberg' and 'hanks' prioritized over only 'spielberg' or 'hanks'
print(ts3.search('scorsese leonardo'))   # movies with 'scorsese' and 'leonardo' prioritized over only 'spielberg' or 'hanks'
print(ts3.search('ryan'))                # movies with 'ryan' in title ranked higher than 'ryan' in actor
```

Results:
```
["Schindler's List", 'Saving Private Ryan', 'Raiders of the Lost Ark', 'Indiana Jones and the Last Crusade', 'Catch Me If You Can', 'Jurassic Park', 'Jaws', 'E.T. the Extra-Terrestrial', 'Empire of the Sun', 'The Color Purple', 'Minority Report', 'Close Encounters of the Third Kind', 'Bridge of Spies', 'Indiana Jones and the Temple of Doom', 'Munich']
['Saving Private Ryan', 'Catch Me If You Can', 'Bridge of Spies', 'Forrest Gump', 'The Green Mile', 'Toy Story', 'Toy Story 3', 'Toy Story 2', 'Cast Away', 'Captain Phillips', 'Road to Perdition', 'Philadelphia', 'Apollo 13', "Schindler's List", 'Raiders of the Lost Ark', 'Indiana Jones and the Last Crusade', 'Jurassic Park', 'Jaws', 'E.T. the Extra-Terrestrial', 'Empire of the Sun', 'The Color Purple', 'Minority Report', 'Close Encounters of the Third Kind', 'Indiana Jones and the Temple of Doom', 'Munich']
['The Departed', 'The Wolf of Wall Street', 'Shutter Island', 'Gangs of New York', 'Inception', 'Django Unchained', 'Catch Me If You Can', 'The Revenant', 'Blood Diamond', 'Titanic', "What's Eating Gilbert Grape", 'Sin Nombre', 'Goodfellas', 'Taxi Driver', 'Casino', 'Raging Bull', 'The King of Comedy', 'After Hours', 'The Last Temptation of Christ']
['Saving Private Ryan', 'Blade Runner 2049', 'La La Land', 'Barry Lyndon', 'Paper Moon', 'Deadpool', 'The Wild Bunch', 'The Notebook', 'The Big Short', 'Drive', 'Big Hero 6', 'Remember the Titans', 'Changeling', 'The Longest Day', 'Bridge of Spies', 'Lethal Weapon', 'When Harry Met Sally...', 'High Plains Drifter', 'Black Panther', 'Creed']
```