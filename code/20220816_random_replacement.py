import re

def is_medial(str_to_search, str_to_find):
    """
    Finds the first match of str_to_find inside str_to_search, but not at the beginning of str_to_search, and not at the end of str_to_search.
    """
    if str_to_find in str_to_search[1:] and str_to_find in str_to_search[:-1]:
        return True
    return False

def is_begin(str_to_search, str_to_find):
    """
    finds the match at the beginning of str_to_search. using regex
    """
    pattern = re.complie("^" + str_to_find)
    if pattern.match(str_to_search):
        return True
    return False

def is_end(str_to_search, str_to_find):
    """
    finds the match at the end of str_to_search. using regex
    """
    pattern = re.complie(str_to_find + "$")
    if pattern.match(str_to_search):
        return True
    return False