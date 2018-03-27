import time
from IMDB_search import Top1000Search
from IMDB_search2 import Top1000Search2
from IMDB_search3 import Top1000Search3

# t1 = time.time()
# ts = Top1000Search()
# print(time.time()-t1)
# print(ts.search('steven'))
# print(ts.search('frank'))       # multiple matches: frank darabont, frank capra
# print(ts.search('lilly'))       # second director


# t1 = time.time()
# ts2 = Top1000Search2()
# print(time.time()-t1)
# print(ts2.search('steven'))      # multiple matches: steven, stevens
# print(ts2.search('frank'))       # multiple matches: frank darabont, frank capra, 'franklin'
# print(ts2.search('lilly'))       # second director


t1 = time.time()
ts3 = Top1000Search3()
print(time.time()-t1)
t2 = time.time()
print(ts3.search('spielberg'))
print(ts3.search('spielberg hanks'))     # movies with 'spielberg and 'hanks' prioritized over only 'spielberg' or 'hanks'
print(ts3.search('scorsese leonardo'))
print(ts3.search('ryan'))                # movies with 'ryan' in title ranked higher than 'ryan' in actor
print(time.time()-t2)