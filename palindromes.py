
word = ['r', 'a', 'c', 'e', '3', 'a', 'r']

last = len(word) - 1
first = 0
is_palindrome = True

count = len(word) / 2

while first <= count and is_palindrome:
    
    if word[last] == word[first]:
        print(word[last] + " and " + word[first] + " is the same!")
    else:
        is_palindrome = False
    
    first += 1
    last -= 1
    
    


