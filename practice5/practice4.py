with open('decoded.txt', 'r') as data: 
    for line in data:
        s = line
print(s)
def encode (s):
    count = 1
    prev = ''
    s1 = ''
    for i in s:
        if i != prev:
            if prev:
                s1 += str(count) + prev
            count = 1
            prev = i
        else:
            count += 1
    s1 += str(count) +s[len(s)-1]
    return s1
s1 = encode(s)
print(s1)

with open('encoded.txt', 'w') as data:
    data.write(s1)

with open('encoded.txt', 'r') as data: 
    for line in data:
        e = line
print(e)

def decode(e):
    d = ''
    count = ''
    for i in e:
        if i.isdigit():
            count += i
        else:
            d += i * int(count)
            count = ''
    return d

d = decode(e)
print(d)
with open('decoded.txt', 'r') as data: 
    for line in data:
        d = line