
word = ['r', 'a', 'c', 'e', 'c', 'a', 'r']

last = len(word) - 1
first = 0

count = len(word) / 2

while first <= count:
    
    if word[last] == word[first]:
        print(word[last] + " and " + word[first] + " is the same!")
    
    first += 2
    last -= 1
    
    


