This is the README of the Technical Interview Practice for Udacity's Career Development. There are five questions. Each question will be listed along with a text explanation of the efficiency of the code and design choice.
*Python 2.7 is needed to run all code. Each function in Python has three test runs.

Question 1: Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.
Answer: This was written in one line of code, so the code is really efficient. I used an if else statement.
No additional libraries were used.

Question 2: Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.
Answer: First, I created an empty list to put the palindrome. Then, I made sure all of the letters in the string were lower cased. Since I am searching for the longest, it makes sense to search the entire string for a palindrome, then decrease the characters by one and search each substring within the string. This needs to continue until palindrome(s) is found. Once found, the loop adds the palindrome to the empty list, but the loop needs to continue to make sure there aren't any other palindromes in substrings of equal length. The loop adds other palindromes of equal length to the list. Then the code can stop running, or break. Then return 'There is no palindrome!' if there aren't any palindromes, else return the list of the largest palindrome(s). 

Question 3: Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
{'A':[('B',2)], 'B':[('A',2),('C',5)], 'C':[('B',5)]}
Vertices are represented as unique strings. The function definition should be question3(G).
Answer: The minimum spanning tree must connect all vertices. Therefore each vertex must connect to another vertex. I create an empty dictionary and a set with 0, the first index, in the set. I get the adjacency matrix from the graph and convert it to a numpy array matrix. I make sure all of my diagonals are zero and then find the vertex with the lowest edge that connects to vertex 0. I created a function that adds the connection to the dictionary. The function also makes the corresponding columns of the vertices equal to 0 and adds the vertices to the set. I then created a loop that runs until all of the vertices are in the dictionary. The loop takes the rows of the matrix that correspond to the vertices in the set. Then the loop finds a the smallest edge that connects a vertex not in the set to the other vertices in the set. It then uses the function addtodict to add the vertex to the dictionary and set. It returns the dictionary when finished.
*Python libraries numpy and random, also Python file class_graph.py (attachment given) needed and imported to run the code.

Question 4: Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be
question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
Answer: Create two sets, one for each node. Put the node in its set. Create veriables that maintains the lowest level of both sets. Create a loop that does not stop until the intersection of the two sets is not empty. For each set, the loop finds the parent of the lowest level node and puts the parent in the set. Once the loop is finished, return the node that is the intersection of the two sets. This is the least common ancestor.
*Python library numpy needed and imported to run the code.

Question 5: Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
Answer: The Node class along with the LinkedList class is contained in the file linked_list.py, which is needed and imported to complete question 5. First, I make sure the value of m is more than 0. If not, it returns an error message. Then I set a counter at 1 and find the head of the list. I create a while loop to sroll through the linked list until it reaches the end. The loop also adds one to the counter every time it reaches a new node. I make sure m is not larger than the counter, or number of nodes in the linked list. If it is not, the function returns the data of the mth node from the end.
*Python file class_graph.py (attachment given) needed and imported to run the code.