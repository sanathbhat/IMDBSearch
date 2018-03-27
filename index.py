import operator
class CustomInvertedIndex:

    def __init__(self):
        self.index = {}  # term : {topic : priority}

    def __update(self, term, topic, priority):
        if term not in  self.index:
            self.index[term] = {topic: priority}
        else:
            # check if topic is already present in entry for term,
            # if present increase priority
            curr_term_dict = self.index[term]
            if topic in curr_term_dict:
                curr_term_dict[topic] += priority
            else:
                curr_term_dict[topic] = priority


    def update(self, terms, topic, priority):
        '''
        Adds multiple terms with a given topic, all of same priority
        :param terms: List of terms to add
        :param topic: The topic for all the terms
        :param priority: The priority for all the terms
        :return: None
        '''
        for term in terms:
            self.__update(term, topic, priority)


    def __lookup(self, term):
        if term not in self.index:
            return {}
        return self.index[term]


    def lookup(self, terms):
        '''
        Look up all terms and combine the results
        :param term:
        :return:
        '''
        results = {}
        for term in terms:
            curr_term_res = self.__lookup(term)
            # for each result of each term, add to final results if not already present, else update priority
            for t, p in curr_term_res.items():
                if t not in results:
                    results[t] = p
                else:
                    results[t] += p
        return sorted(results.items(), key=operator.itemgetter(1), reverse=True)
