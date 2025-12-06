from collections import Counter


def find_anagrams(word, candidates):
    ans = []
    for i in candidates:
        if (
            Counter(list(i.lower())) == Counter(list(word.lower()))
            and i.lower() != word.lower()
        ):
            ans.append(i)
    return ans
