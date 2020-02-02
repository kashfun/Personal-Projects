def palindrome(word): 
    revword = word[::-1]
    if (word.lower() == revword.lower()): 
        return True
    return False

word = input('Enter word/number: ')
check = palindrome(word) 

if (check): 
    print(word+" is a palindrome") 
else: 
    print(word+" is a not palindrome")
