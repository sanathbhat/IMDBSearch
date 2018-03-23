import time
from IMDB_search import Top1000Search

t1 = time.time()
ts = Top1000Search()
print(time.time()-t1)
print(ts.search('steven'))
print(ts.search('frank'))       # multiple matches: frank darabont, frank capra
print(ts.search('lilly'))       # second director
