###Question 1:Given two strings s and t, determine whether some anagram of t is a substring of s.
###For example: if s = "udacity" and t = "ad", then the function returns True.
###Your function definition should look like: question1(s, t) and return a boolean True or False.
def question1(s,t):
    return False if s.find(t) == -1 and s.find(t[::-1]) == -1 else True
print question1('This be a string','is')
print question1('This be a string','si')
print question1('This be a string','isi')
