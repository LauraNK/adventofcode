f = open('input.txt', 'r')
text = f.read()
f.close()

text = text.split('\n')
niceCount = 0
vowels = 'aeiou'

for i in text:
    if 'ab' in i or 'cd' in i or 'pq' in i or 'xy' in i:
        continue
    vowelCount = 0
    for char in i:
        if char in vowels:
            vowelCount += 1
    if vowelCount < 3:
        continue    
        
    for char in range(0, len(i)-1):
        if i[char] == i[char+1]:
            niceCount += 1
            break

print(niceCount)

