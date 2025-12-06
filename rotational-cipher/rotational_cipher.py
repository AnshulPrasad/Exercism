def rotate(text, key):
    ans = ""
    for i in text:
        if not i.isalpha():
            ans += i
            continue
        char = "a"
        if i.isupper():
            char = "A"
        ans += chr((ord(i) - ord(char) + key % 26) % 26 + ord(char))
    return ans
