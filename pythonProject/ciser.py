def ciser(text,key):
    result = ""
    for i in text:
        if(i.isupper()):
            result += chr((ord(i)+4-64)%26+65)
        else:
            result += chr((ord(i)+4-96)%26+97)
    return result
text =  "CEASER CIPHER EXAMPLE"
s = 4

print("Plain text: "+text)
print("shift pattern: "+str(s))
print("cipher: "+ciser(text,s))

sequence = {"Python","Pass","Statement",}

for value in sequence:
    if value == "Pass":
        pass
    else:
        print("Not Reachable Pass",value)

