sentece = "i love PYTHON"
capi = sentece.capitalize()
print(capi)

text1 = 'pYtHon'
conv = text1.casefold()
print(conv)

text2 = 'python programming'
c = text2.count('p')
print(c)
c2 = text2.count('r',9,17)
print(c2)

sentence = 'Python'
new_str = sentence.center(12,'*')
print(new_str)

message = 'python is python'
print(message.endswith('fun'))
print(message.endswith(('python','fun','is')))
