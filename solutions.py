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

