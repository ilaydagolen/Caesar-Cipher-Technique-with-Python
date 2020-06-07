phrase=input('Enter sentence to encrypt:')
shift=input('Enter shift value:')
shift=int(shift)
encoded_phrase=''
for c in phrase:
    ascii_code=ord(c)
    if c.isupper():
        replaceChar=chr((ascii_code + shift-65)% 26+65)
    elif c.islower():
        replaceChar= chr((ascii_code+shift - 97)% 26+97)
    else:
        replaceChar= c
    encoded_phrase=encoded_phrase + replaceChar

print("The encoded phrase is {}\n".format(encoded_phrase))


