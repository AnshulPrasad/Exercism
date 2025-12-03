def convert(number):
    ans = 'Pling'*(not bool(number%3)) + 'Plang'*(not bool(number%5)) + 'Plong'*(not bool(number%7)) + ""
    if ans == "":
        ans += str(number)
    return ans
    