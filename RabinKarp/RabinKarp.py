def RabinKarp(text, pattern):
    if len(pattern) > len(text):
        print("length of pattern is more than length of text")
        return -1
    thash = 0
    phash = 0
    isMatch = 0
    for i in range(len(pattern)):
        phash += ord(pattern[i])
        thash += ord(text[i])
    for i in range(len(text) - len(pattern) + 1):
        if thash == phash:
            for j in range(len(pattern)):
                if text[i+j] == pattern[j]:
                    isMatch += 1
                else:
                    break
        if isMatch == len(pattern):
            print("Found pattern %s in string %s, index %d" %(pattern, text, i))
            return 0
        elif i <= len(text) - len(pattern) - 1:
            isMatch = 0
            thash = thash - ord(text[i]) + ord(text[i+len(pattern)])
        if i == len(text) - len(pattern):
            print("Pattern %s not found in string %s" %(pattern, text))
            return 0
print("Write text:")
a = str(input())
print("Write pattern:")
b = str(input())

RabinKarp(a, b) 