def remove_stop_words(words):
    stop_words = {'a', 'the', 'of', 'is', 'in', 'an', 'of', 'for', 'and', 'or'}
    return [word for word in words if word not in stop_words]