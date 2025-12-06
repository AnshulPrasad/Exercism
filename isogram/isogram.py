def is_isogram(string):
    string = [i for i in string.lower() if i.isalpha()]
    return len(set(string)) == len(string)
