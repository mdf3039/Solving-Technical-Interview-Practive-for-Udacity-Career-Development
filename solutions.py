###Question 1:Given two strings s and t, determine whether some anagram of t is a substring of s.
###For example: if s = "udacity" and t = "ad", then the function returns True.
###Your function definition should look like: question1(s, t) and return a boolean True or False.
def question1(s,t):
    return False if s.find(t) == -1 and s.find(t[::-1]) == -1 else True
#Test function
print "Test Question 1"
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
#Test function
print "Test Question 2"
print question2('AbraCaDaBra Alakazam')
print question2('qwertyuytrewq')
print question2('This has no palindromes!')

###Question 3:Given an undirected graph G, find the minimum spanning tree within G. A minimum
###spanning tree connects all vertices in a graph with the smallest possible total weight of edges.
###Your function should take in and return an adjacency list structured like this:
###{'A':[('B',2)], 'B':[('A',2),('C',5)], 'C':[('B',5)]}
###Vertices are represented as unique strings. The function definition should be question3(G)
import numpy as np
import random
import class_graph as cg
def question3(G):
    #create an empty dictionary and a set with 0, the first index, in the set.
    a_list = {}
    in_dict = set([0])
    #get the adjacency matrix from the graph and convert it to a numpy array matrix
    matrix = np.array(G.get_adjacency_matrix())
    #make sure all of my diagonals are zero
    for i in range(len(matrix)):
        matrix[i][i] = 0
    #find the vertex with the lowest edge that connects to vertex 0
    try:
        sec_vertex = random.choice(list(np.where(matrix[0]==np.min(matrix[0][np.nonzero(matrix[0])]))[0]))
    except:
        return "Graph is disconnected at first vertex or only one vertex!"
    #created a function that adds the connection to the dictionary. The function also makes the
    #corresponding columns of the vertices equal to 0 and adds the vertices to the set.
    def addtodict(i,j):
        for m,n in [(i,j),(j,i)]:
            try:
                a_list[str(m)].append((str(n),matrix[m][n] if matrix[m][n] != 0 else matrix[n][m]))
            except:
                a_list[str(m)] = [(str(n),matrix[m][n] if matrix[m][n] != 0 else matrix[n][m])]
        for p in [i,j]:
            matrix[:,p] = 0
            in_dict.add(p)
    #used the function to add the first vertex 0 and the second vertex
    addtodict(0,sec_vertex)
    #created a loop that runs until all of the vertices are in the dictionary.
    while len(a_list) != len(matrix):
        #makes a matrix with the rows of the matrix that correspond to the vertices in the set.
        matrix_in_dict = matrix[list(in_dict)]
        #finds the smallest value not equal to zero
        try:
            min_val = np.min(matrix_in_dict[np.nonzero(matrix_in_dict)])
        except:
            return "Graph is disconnected!", a_list, "Graph is disconnected!"
        #finds the indices of the points with the smallest value and chooses one at random
        point = random.choice([(index, row.index(min_val)) for index, row in enumerate(matrix_in_dict.tolist()) if min_val in row])
        #uses the function addtodict to add the vertex to the dictionary and set and zero out the vertex's column
        addtodict(list(in_dict)[point[0]],point[1])
    return a_list
#Test function
print "Test Question 3"
graph = cg.Graph()
graph.insert_edge(100, 0, 4)
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
graph.insert_edge(100, 4, 0)
graph.insert_edge(100, 2, 1)
graph.insert_edge(101, 3, 1)
graph.insert_edge(102, 4, 1)
graph.insert_edge(103, 4, 3)
print question3(graph)
graph2 = cg.Graph()
graph2.insert_edge(1, 0, 4)
graph2.insert_edge(8, 1, 2)
graph2.insert_edge(11, 1, 3)
graph2.insert_edge(4, 1, 4)
graph2.insert_edge(3, 3, 4)
graph2.insert_edge(1, 4, 0)
graph2.insert_edge(8, 2, 1)
graph2.insert_edge(11, 3, 1)
graph2.insert_edge(4, 4, 1)
graph2.insert_edge(3, 4, 3)
print question3(graph2)
graph3 = cg.Graph()
graph3.insert_edge(15, 0, 4)
graph3.insert_edge(81, 1, 2)
graph3.insert_edge(10, 1, 3)
graph3.insert_edge(14, 1, 4)
graph3.insert_edge(31, 3, 4)
graph3.insert_edge(15, 4, 0)
graph3.insert_edge(81, 2, 1)
graph3.insert_edge(10, 3, 1)
graph3.insert_edge(14, 4, 1)
graph3.insert_edge(31, 4, 3)
print question3(graph3)
###Question 4:Find the least common ancestor between two nodes on a binary search tree. The least
###common ancestor is the farthest node from the root that is an ancestor of both nodes. For example,
###the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the
###root's left child, then that left child might be the lowest common ancestor. You can assume that
###both nodes are in the tree, and the tree itself adheres to all BST properties. The function
###definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix,
###where the index of the list is equal to the integer stored in that node and a 1 represents a child
###node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers
###representing the two nodes in no particular order. For example, one test case might be
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
    #Create a loop that does not stop until the intersection of the two sets is not empty. For each
    #set, the loop finds the parent of the lowest level node and puts the parent in the set.
    while len(set.intersection(set1,set2)) == 0:
        level1 = np.where(T[:,level1] == 1)[0].tolist()
        None if not level1 else set1.add(level1[0])
        level2 = np.where(T[:,level2] == 1)[0].tolist()
        None if not level2 else set2.add(level2[0])
        if not level1+level2:
            return "Tree is disconnected"
    #return the least common ancestor
    return list(set.intersection(set1,set2))[0]
#Test function
print "Test Question 4"
print question4([[0, 1, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[1, 0, 0, 0, 1],[0, 0, 0, 0, 0]],3,1,4)
print question4([[0, 1, 0, 0, 1],[0, 0, 1, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 1, 0]],0,1,4)
print question4([[0, 1, 0, 0, 1],[0, 0, 1, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 1, 0]],0,1,2)

###Question 5:Find the element in a singly linked list that's m elements from the end. For example, if
###a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function
###definition should look like question5(ll, m), where ll is the first node of a linked list and m is
###the "mth number from the end". You should copy/paste the Node class below to use as a representation
###of a node in the linked list. Return the value of the node at that position.
###class Node(object):
###  def __init__(self, data):
###    self.data = data
###    self.next = None
import linked_list as LL
def question5(ll, m):
    #make sure the value of m is more than 0
    if m <=0:
        return "m can't be zero or negative"
    #set a counter at 1 and find the head of the list
    counter = 1
    if ll.head:
        current = ll.head
    else:
        return "There is no head to this linked list"
    #Create a while loop to scroll through the linked list until it reaches the end. The loop also
    #adds one to the counter every time it reaches a new node.
    while current.next:
        current = current.next
        counter += 1
    #make sure m is not larger than the counter, or number of nodes in the linked list
    if m > counter:
        return "There are only {} nodes so you can't find {} from the end.".format(counter,m)
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
print question5(ll,1)
print question5(ll,4)
print question5(ll,2)
print question5(ll,0)
