f = open('input.txt', 'r')
text = f.read()
f.close()

text = text.split('\n')
niceCount = 0

for i in text:
    
    # It contains at least one letter which repeats with exactly one letter between them
    for char in range(0, len(i)-2):
        if i[char] == i[char+2]:
            break
    else:
        continue
            
    # Contains a pair of any two letters that appears at least twice in the string without overlapping   
    for char in range(0, len(i)-1):
        if i.count(i[char] + i[char+1]) > 1:
            niceCount +=1
            break
            
print(niceCount)
