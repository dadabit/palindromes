word_File = open('words.txt', 'r') #open the file

def check_palindrome(p_word): #function that check the word if it is a palindrome

    last = len(p_word) - 1
    first = 0
    is_palindrome_times = 0

    count = len(p_word) / 2

    while first <= count:
    
        if p_word[last] == p_word[first]:
            is_palindrome_times += 1
        else:
            print("this word is not a palindrome")
            first = count + 1
    
        first += 1
        last -= 1
    
        if is_palindrome_times >= count:
            print("this word is a palindromes")
            
for word in word_File:
    words = list(word.strip())
    check_palindrome(words)
    
    


word_File.close()
