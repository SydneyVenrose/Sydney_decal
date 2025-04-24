#2.1 Making A List
#number_list = list(range(21))
#print(number_list)

#2.2 Working with List Elements
#number_list = list(range(21))

#def squareList(input_list):
    #return [x**2 for x in input_list]

#squared_numbers = squareList(number_list)
#print(squared_numbers)#

#2.3
# def first_fifteen_elements(input_list):
   # return input_list[:15]

# Assuming this is your list from Part 2.2
#number_list = list(range(21))
#squared_numbers = [x**2 for x in number_list]

# Calling the function
#print(first_fifteen_elements(squared_numbers))

#2.4
# # number_list = list(range(21))

# def squareList(input_list):
#     return [x**2 for x in input_list]

# squared_numbers = squareList(number_list)

# def first_fifteen_elements(input_list):
#     return input_list[:15]

# first_15 = first_fifteen_elements(squared_numbers)
# print(first_15)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]

# def every_fifth_element(input_list):
#     return input_list[4::5]

# fifth_elements = every_fifth_element(squared_numbers)
# print(fifth_elements)  # Output: [16, 81, 196, 361]

#2.5 
# def fancy_function(input_list):
#     return input_list[-3::-3]

# number_list = list(range(21))
# squared_numbers = [x**2 for x in number_list]
# result = fancy_function(squared_numbers)
# print(result)  # Output: [400, 289, 196, 121, 64, 25, 4]

#3.1
# def create_2d_list():
#     matrix = []
#     count = 1
#     for i in range(5):
#         row = []
#         for j in range(5):
#             row.append(count)
#             count += 1
#         matrix.append(row)
#     return matrix

# matrix = create_2d_list()
# print(matrix)
# Output: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
#          [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

#3.2
# def modified_2d_list(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] % 3 == 0:
#                 matrix[i][j] = "?"
#     return matrix

# matrix = create_2d_list()
# modified_matrix = modified_2d_list(matrix)
# print(modified_matrix)
# Output: [[1, 2, '?', 4, 5],
#          ['?', 7, 8, '?', 10],
#          [11, '?', 13, 14, '?'],
#          [16, 17, '?', 19, 20],
#          ['?', 22, 23, '?', 25]]

#3.3
# def sum_non_question_elements(matrix):
#     total = 0
#     for row in matrix:
#         for element in row:
#             if element != "?":
#                 total += element
#     return total

# matrix = create_2d_list()
# new_matrix = modified_2d_list(matrix)
# result = sum_non_question_elements(new_matrix)
# print(result)  # Output: 217
