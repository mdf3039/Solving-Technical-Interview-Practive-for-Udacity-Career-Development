###Question 1:Given two strings s and t, determine whether some anagram of t is a substring of s.
###For example: if s = "udacity" and t = "ad", then the function returns True.
###Your function definition should look like: question1(s, t) and return a boolean True or False.
def question1(s,t):
    return False if s.find(t) == -1 and s.find(t[::-1]) == -1 else True
print question1('This be a string','is')
print question1('This be a string','si')
print question1('This be a string','isi')

###Question 2:Given a string a, find the longest palindromic substring contained in a.
###Your function definition should look like question2(a), and return a string.
def question2(a):
    palindrome = []
    a = a.lower()
    for i in range(1,len(a))[::-1]:
        for j in range(0,len(a)-i):
            checker = a[j:j+i+1]
            if checker == checker[::-1]:
                palindrome.append(checker)
        if len(palindrome) != 0:
            break
    return "There is no palindrome!" if not palindrome else palindrome
print question2('AbraCaDaBra Alakazam')
print question2('qwertyuytrewq')
print question2('This has no palindromes!')
