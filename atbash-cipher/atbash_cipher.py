def encode(plain_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    for i in plain_text:
        if i.isalpha():
            ans += plain[25 - (ord(i.lower()) - ord("a"))]
        elif i.isdigit():
            ans += i
    ans = " ".join([ans[i : i + 5] for i in range(0, len(ans), 5)])
    return ans


def decode(ciphered_text):
    return encode(ciphered_text).replace(" ", "")
