__author__ = "saimadhu.polamuri"

""" Create a program print the elements in the 2 d array in spiral order """

class solution:
    def get_spiral_order(self, array):

        rows = len(array)
        columns = len(array[0])

        # Directions initialization

        direction = "left_to_right"

        top_row_index = 0
        bottom_row_index = rows
        right_column_index = columns
        left_column_index = 0

        spiral_order = list()

        if columns == 1:

            for i in range(0, rows):
                spiral_order.append(array[i][0])
        elif rows == 1:

            for i in range(0, columns):
                spiral_order.append(array[0][i])
        elif rows == 1 and columns == 1:
            spiral_order.append(array[0][0])
        else:

            while (top_row_index <= bottom_row_index-1) & (left_column_index <= right_column_index-1):

                if direction == "left_to_right":
                    for i in range(left_column_index, right_column_index):
                        element = array[top_row_index][i]
                        spiral_order.append(element)
                    direction = "top_to_bottom"
                    top_row_index += 1

                elif direction == "top_to_bottom":
                    for i in range(top_row_index, bottom_row_index):
                        element = array[i][right_column_index - 1]
                        spiral_order.append(element)
                    direction = "right_to_left"
                    right_column_index -= 1

                elif direction == "right_to_left":
                    for i in range(right_column_index-1, left_column_index-1, -1):
                        element = array[bottom_row_index-1][i]
                        spiral_order.append(element)
                    direction = "bottom_to_top"
                    bottom_row_index -= 1

                elif direction == "bottom_to_top":
                    for i in range(bottom_row_index-1, top_row_index-1, -1):

                        element = array[i][left_column_index]
                        spiral_order.append(element)
                    direction = "left_to_right"
                    left_column_index += 1

        return spiral_order

test_list = [[1,2,3],[4,5,6],[7,8,9]]

test_sol = solution()

print(test_sol.get_spiral_order(test_list))









