def is_pangram(sentence):
    sentence = [i for i in sentence.lower() if i.isalpha()]
    return len(set(sentence)) == 26
