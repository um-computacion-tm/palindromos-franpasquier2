'''''
import unittest 

def palindrome(palabra):
    palabra_1 = palabra.lower()
    lista = list(palabra_1)
    alreves = []
    total += 1    
    for i in lista:
        alreves += lista[-total]
        total += 1
'''''

import unittest


def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
    else:
        return False

print (palindrome("mendoza"), "= mendoza")
print (palindrome("aba"), "= aba") 
print (palindrome("neuquen"), "= neuquen")
print (palindrome("ala"), "= ala")
print (palindrome("rar"), "= rar") 



