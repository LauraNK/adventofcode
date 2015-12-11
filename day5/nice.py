f = open('input.txt', 'r')
text = f.read()
f.close()

text = text.split('\n')
nice_count = 0
vowels = 'aeiou'

for i in text:
    if 'ab' in i or 'cd' in i or 'pq' in i or 'xy' in i:
        continue
    vowel_count = 0
    for char in i:
        if char in vowels:
            vowel_count += 1
    if vowel_count < 3:
        continue    
        
    for char in range(0, len(i)-1):
        if i[char] == i[char+1]:
            nice_count += 1
            break

print(nice_count)

