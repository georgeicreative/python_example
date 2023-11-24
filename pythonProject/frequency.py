def wordfreq(string,n):
    from collections import OrderedDict
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in string:
        if i in punc:
            new_string = string.replace(i,"")
    new_string2 = new_string.lower()
    wordlist = list(new_string2.split(" "))
    freq = {}
    for i in wordlist:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    sorted_dt = {key: value for key, value in sorted(freq.items(), key=lambda item: item[1],reverse=False)}
    for i in range(n):
        print(sorted_dt.popitem())
string ="Sample is sample that so good@ good"
wordfreq(string,3)



