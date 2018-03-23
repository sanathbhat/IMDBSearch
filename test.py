import time
from IMDB_search import Top1000Search
from IMDB_search2 import Top1000Search2

t1 = time.time()
ts = Top1000Search()
print(time.time()-t1)
print(ts.search('steven'))
print(ts.search('frank'))       # multiple matches: frank darabont, frank capra
print(ts.search('lilly'))       # second director


t1 = time.time()
ts2 = Top1000Search2()
print(time.time()-t1)
print(ts2.search('steven'))      # multiple matches: steven, stevens
print(ts2.search('frank'))       # multiple matches: frank darabont, frank capra, 'franklin'
print(ts2.search('lilly'))       # second director
