# from array import *

# my_array = array('i', [10, 20, 30, 40, 50])

# print(my_array[2])
# my_array.insert(5, 100)
# for i in my_array:
#     print(i)

# my_array.remove(40)
# print(my_array.index(50))
# my_array[2] = 200
# for i in my_array:
#     print(i)



############## lists

# list1 = ['Erik', 'Hayk', 2011, 2008]
# list2 = [1, 2, 3, 4, 5, 6, 7]
# print("list1[0]: ", list1[0])
# print("list2[1:5]: ", list2[1:5])



################### maps
import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
for i in res.maps:
    print(i, '\n')

# print('Keys = {}'.format(list(res.keys())))
# print('Values = {}'.format(list(res.values())))
#
# # Printing all the elements from the result
# print('elements:')
# for key, val in res.items():
#     print('{} = {}'.format(key, val))
# print()
#
# # Find a specific value in the result
# print('day3 in res: {}'.format(('day1' in res)))
# print('day4 in res: {}'.format(('day4' in res)))
#
# dict2['day4'] = 'Fri'
# print(res.maps, '\n')


# ################### Binary tree

# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data

#     def insert(self, data):
# # Compare the new value with the parent node
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data = data

# # Print the tree
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data),
#         if self.right:
#             self.right.PrintTree()

# # Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()















