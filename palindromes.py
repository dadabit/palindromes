
word = ['r', 'a', 'c', 'e', '3', 'a', 'r']

last = len(word) - 1
first = 0
is_palindrome = True
is_palindrome_times = 0

count = len(word) / 2

while first <= count and is_palindrome:
    
    if word[last] == word[first]:
        is_palindrome_times += 1
    else:
        print("this word is not a palindrome")
        is_palindrome = False
    
    first += 1
    last -= 1
    
    if is_palindrome_times >= count:
        print("this word is a palindromes")
    
    


