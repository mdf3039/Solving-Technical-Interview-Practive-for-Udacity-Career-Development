###Question 1:Given two strings s and t, determine whether some anagram
###of t is a substring of s. For example: if s = "udacity" and t = "ad",
###then the function returns True. Your function definition should look
###like: question1(s, t) and return a boolean True or False.
def question1(s,t):
    #delete all spaces and lowercase all letters
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()
    if len(s) == 0:
        print "There is not a string s"
        return None
    if len(t) == 0:
        print "There is not a string t"
        return None
    if len(t) > len(s):
        print "There can't be an anagram; t is bigger than s"
        return None
    #create a empty dictionary for t
    tdict = {}
    #fill the dictionary with the count and letters of t
    for i in range(len(t)):
        tdict[t[i]] = t.count(t[i])
    #for each substring in s of length t, create empty dictionary
    for i in range(len(s)-len(t)+1):
        sub_str_s = s[i:i+len(t)]
        sss_dict = {}
    #fill empty dictionary with count and letters of substring of s
        for j in range(len(t)):
            sss_dict[sub_str_s[j]] = sub_str_s.count(sub_str_s[j])
    #if dictionaries are equal, return true
        if sss_dict == tdict:
            return True            
    return False
#Test function
print "Test Question 1"
print question1('     ','is')
#Should print 'There is not a string s' and return None
print question1('This be a string','     ')
#Should print 'There is not a string s' and return None
print question1('This be a string','isi')
#False
print question1('This be a string','rst')
#True
print " "

###Question 2:Given a string a, find the longest palindromic substring
###contained in a. Your function definition should look like
###question2(a), and return a string.
def question2(a):
    palindrome = None
    a = a.replace(" ", "").lower()
    if len(a) == 0:
        print "There is not a string a"
        return None
    for i in range(0,len(a))[::-1]:
        for j in range(0,len(a)-i):
            checker = a[j:j+i+1]
            if checker == checker[::-1]:
                palindrome = checker
                return palindrome
#Test function
print "Test Question 2"
print question2('           ')
#Should print 'There is not a string a' and return None
print question2('mnbvcxzlkjhgfdsapoiuytrewqwertyuiopasdfghjklzxcvbnm')
#mnbvcxzlkjhgfdsapoiuytrewqwertyuiopasdfghjklzxcvbnm
print question2('This has no palindromes over two chars!')
#t
print question2('This has three character palindrome!')
#tht
print " "

###Question 3:Given an undirected graph G, find the minimum spanning
###tree within G. A minimum spanning tree connects all vertices in a
###graph with the smallest possible total weight of edges. Your function
###should take in and return an adjacency list structured like this:
###{'A':[('B',2)], 'B':[('A',2),('C',5)], 'C':[('B',5)]}
###Vertices are represented as unique strings. The function definition
###should be question3(G)
import numpy as np
import pandas as pd
import math
import random
import class_graph as cg
def question3(G):
    #Create empty Graph
    G_G = cg.Graph(nodes = [], edges = [])
    #For every item in every key, make an edge
    for key in G.keys():
        for item in range(len(G[key])):
            G_G.insert_edge(G[key][item][1], key, G[key][item][0])
    #get edge list, create an empty dictionary and a set with the first
    #index, in the set. Convert edge list to dataframe
    L = G_G.get_edge_list()
    df = pd.DataFrame(L).pivot(index=1,columns=2, values=0)
    a_list = {}
    in_dict = set([df.index[0]])
    #make sure all of my diagonals are zero
    np.fill_diagonal(df.values, 'NaN')
    #find the vertex with the lowest edge that connects to first index
    try:
        sec_vertex = df[df.index[0]].idxmin()
    except:
        print "Graph is disconnected at first vertex or only one vertex!"
        return None
    #created a function that adds the connection to the dictionary. The
    #function also makes the corresponding rows of the vertices equal
    #to 'NaN' and adds the vertices to the set.
    def addtodict(i,j):
        for m,n in [(i,j),(j,i)]:
            try:
                a_list[str(m)].append((str(n),df.get_value(m,n) if not
                                       math.isnan(df.get_value(m,n))
                                       else df.get_value(n,m)))
            except:
                a_list[str(m)] = [(str(n),df.get_value(m,n) if not
                                   math.isnan(df.get_value(m,n))
                                   else df.get_value(n,m))]
        for p in [i,j]:
            df[p:p] = float('nan')
            in_dict.add(p)
    #add the first index/vertex and the second vertex
    addtodict(df.index[0],sec_vertex)
    #loop that runs until all of the vertices are in the dictionary.
    while len(a_list) != len(G):
        #columns of the dataframe correspond to the vertices in the set.
        df_in_dict = df[list(in_dict)]
        #finds the smallest value not equal to zero
        min_val = np.nanmin(list(df_in_dict.min()))
        if math.isnan(min_val):
            print "Graph is disconnected!"
            return None
        #finds the first point equal to minimum value
        def what_to_addtodict(d):
            for row in list(d.index):
                for column in list(d.columns):
                    if d.get_value(row,column) == min_val:
                        addtodict(row,column)
                        return
        what_to_addtodict(df_in_dict)
    return a_list
#Test function
print "Test Question 3"
print question3({'1': [('4', 102), ('2', 100), ('3', 101)],
                 '0': [('4', 100)], '3': [('1', 101)],
                 '2': [('1', 100)], '4': [('0', 100), ('1', 102)]})
#{'1': [('4', 102.0), ('2', 100.0), ('3', 101.0)], '0': [('4', 100.0)],
#'3': [('1', 101.0)], '2': [('1', 100.0)], '4': [('0', 100.0),
#('1', 102.0)]}
print question3({'1': [], '0': [],
                 '3': [('4', 3)], '2': [('1', 8)],
                 '4': [('0', 1), ('3', 3), ('1', 4)]})
#Should print 'Graph is disconnected at first vertex or only one
#vertex!' and return None
print question3({'0': [('1', 14), ('2', 10), ('3', 81), ('4', 55),
                       ('5', 31), ('6', 76), ('7', 81)],
                 '1': [('0', 14), ('2', 1), ('3', 22), ('4', 97),
                       ('5', 82), ('6', 19), ('7', 68)],
                 '2': [('0', 10), ('1', 1), ('3', 25), ('4', 69),
                       ('5', 42), ('6', 7), ('7', 20)],
                 '3': [('0', 81), ('1', 22), ('2', 25), ('4', 54),
                       ('5', 61), ('6', 3), ('7', 22)],
                 '4': [('0', 55), ('1', 97), ('2', 69), ('3', 54),
                       ('5', 15), ('6', 85), ('7', 77)],
                 '5': [('0', 31), ('1', 82), ('2', 42), ('3', 61),
                       ('4', 15), ('6', 39), ('7', 1)],
                 '6': [('0', 76), ('1', 19), ('2', 7), ('3', 3),
                       ('4', 85), ('5', 39), ('7', 13)],
                 '7': [('0', 81), ('1', 68), ('2', 20), ('3', 22),
                       ('4', 77), ('5', 1), ('6', 13)]})
#{'1': [('2', 1.0)], '0': [('2', 10.0)], '3': [('6', 3.0)],
#'2': [('0', 10.0), ('1', 1.0), ('6', 7.0)], '5': [('7', 1.0),
#('4', 15.0)], '4': [('5', 15.0)], '7': [('6', 13.0), ('5', 1.0)],
#'6': [('2', 7.0), ('3', 3.0), ('7', 13.0)]}
print " "

###Question 4:Find the least common ancestor between two nodes on a
###binary search tree. The least common ancestor is the farthest node
###from the root that is an ancestor of both nodes. For example, the
###root is a common ancestor of all nodes on the tree, but if both nodes
###are descendents of the root's left child, then that left child might
###be the lowest common ancestor. You can assume that both nodes are in
###the tree, and the tree itself adheres to all BST properties. The
###function definition should look like question4(T, r, n1, n2), where
###T is the tree represented as a matrix, where the index of the list is
###equal to the integer stored in that node and a 1 represents a child
###node, r is a non-negative integer representing the root, and n1 and
###n2 are non-negative integers representing the two nodes in no
###particular order. For example, one test case might be
###question4([[0, 1, 0, 0, 0],
###           [0, 0, 0, 0, 0],
###           [0, 0, 0, 0, 0],
###           [1, 0, 0, 0, 1],
###           [0, 0, 0, 0, 0]],
###          3,
###          1,
###          4)
###and the answer would be 3.
import numpy as np
def question4(T, r, n1, n2):
    #Create two sets, one for each node. Put the node in its set.
    set1 = set([n1])
    set2 = set([n2])
    #Create veriables that maintains the lowest level of both sets.
    level1 = n1
    level2 = n2
    #Make T a numpy array matrix
    T = np.array(T)
    #Create a loop that does not stop until the intersection of the two
    #sets is not empty. For each set, the loop finds the parent of the
    #lowest level node and puts the parent in the set.
    while len(set.intersection(set1,set2)) == 0:
        level1 = np.where(T[:,level1] == 1)[0].tolist()
        None if not level1 else set1.add(level1[0])
        level2 = np.where(T[:,level2] == 1)[0].tolist()
        None if not level2 else set2.add(level2[0])
        if not level1+level2:
            print "Tree is disconnected"
            return None
    #return the least common ancestor
    return list(set.intersection(set1,set2))[0]
#Test function
print "Test Question 4"
print question4([[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1],[0, 0, 0, 0, 0]],3,1,4)
#3
print question4([[0, 1, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],[0, 0, 0, 1, 0]],0,1,3)
#Should print 'Tree is disconnected' and return None
print question4([[0, 1, 1, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0],[0, 0, 0, 0, 0, 0, 0, 1,],
                 [0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0,]],
                0,6,7)
#0
print " "

###Question 5:Find the element in a singly linked list that's m elements
###from the end. For example, if a linked list has 5 elements, the 3rd
###element from the end is the 3rd element. The function definition
###should look like question5(ll, m), where ll is the first node of a
###linked list and m is the "mth number from the end". You should
###copy/paste the Node class below to use as a representation of a node
###in the linked list. Return the value of the node at that position.
###class Node(object):
###  def __init__(self, data):
###    self.data = data
###    self.next = None
import linked_list as LL
def question5(ll, m):
    #make sure the value of m is more than 0
    if m <=0:
        print "m can't be zero or negative"
        return None
    #set a counter at 1 and find the head of the list
    counter = 1
    if ll.head:
        current = ll.head
    else:
        print "There is no head to this linked list"
        return None
    #Create a while loop to scroll through the linked list until it
    #reaches the end. The loop also adds one to the counter every time
    #it reaches a new node.
    while current.next:
        current = current.next
        counter += 1
    #make sure m is not larger than the counter, or number of nodes in
    #the linked list
    if m > counter:
        print "Only {} nodes. Can't find {}.".format(counter,m)
        return None
    else:
        return ll.get_position(counter-m+1).data
#Test function
print "Test Question 5"
n1 = LL.Node(1)
n2 = LL.Node(2)
n3 = LL.Node(3)
n4 = LL.Node(4)
ll = LL.LinkedList(n1)
ll.append(n2)
ll.append(n3)
ll.append(n4)
print question5(ll,3)
#2
print question5(ll,1)
#4
print question5(ll,8)
#Prints 'Only 4 nodes. Can't find 8' and returns None
print question5(ll,2)
#3
print question5(ll,0)
#m can't be zero or negative
