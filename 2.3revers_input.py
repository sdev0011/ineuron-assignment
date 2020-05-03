''' Write a Python program to reverse a word after accepting the input from the user.
Sample Output:
Input word: AcadGild
Output: dilGdacA'''
#first solution
def revers_word(word):
    return word[::-1]

word = input("enter word:")
print(revers_word(word))


#second solution
def revers_word2(word):
    for i in word:
        word = word + i
    return word
    
word = input("enter word:")
print(revers_word(word))