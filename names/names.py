import time

from binary_search_tree import BinarySearchTree

"""
    using my Binary Search Tree so i can use the methods created previously.
    (Hint: You might try importing a data structure you built during the week)

    """
"""
 First Past Planning:

 removed excessive code, looking at what what's required the additonal code isn't necessary
 compares the two files and prints out duplicate name entries
 so we have two files names_1.txt and names_2.txt

 """


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
tree_traversal = BinarySearchTree("new_list")

for name in names_1:
    tree_traversal.insert(name)

    for name2 in names_2:
        if tree_traversal.contains(name2):
            duplicates.append(name2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

"""
    Try running the code with python3 names.py. Be patient because it might take a while:
    approximately six seconds on my laptop. What is the runtime complexity of this code?

    Six seconds is an eternity so you've been tasked with speeding up the code. Can you get
    the runtime to under a second? Under one hundredth of a second?


    64 duplicates:

    Hallie Vazquez, Peyton Lloyd, Daphne Hamilton, Jaden Hawkins, Dulce Hines, Piper Hamilton, Marisol Morris, Josie Dawson, Giancarlo Warren, Amiah Hobbs, Jaydin Sawyer, Franklin Cooper, Diego Chaney, Carley Gallegos, Ahmad Watts, Malcolm Nelson, Malcolm Tucker, Grace Bridges, Luciana Ford, Davion Arias, Pablo Berg, Jadyn Mays, Marley Rivers, Abel Newman, Sanai Harrison, Cloe Norris, Clay Wilkinson, Salma Meza, Addison Clarke, Nelson Acevedo, Devyn Aguirre, Winston Austin, Carsen Tyler, Hayley Morgan, Aleah Valentine, Camryn Doyle, Josie Cole, Nathalie Little, Leia Foley, Jordin Schneider, Justine Soto, Lennon Hunt, Zara Suarez, Kale Sawyer, William Maldonado, Irvin Krause, Maliyah Serrano, Selah Hansen, Kameron Osborne, Alvaro Robbins, Leon Cochran, Andre Carrillo, Dashawn Green, Eden Howe, Logan Morrow, Ralph Roth, Trace Gates, Megan Porter, Aydan Calderon, Raven Christensen, Ashlee Randall, Victoria Roach, River Johnson, Ali Collier


    runtime: 7.591180086135864 seconds

    original code:
    for name_1 in names_1:
       for name_2 in names_2:
           if name_1 == name_2:
               duplicates.append(name_1)

    nest loops = O(n^2) runtime

    """

# ---------- Stretch Goal - ----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
