"""
Challenge: Calculate the route a Snail would take by going Clockwise around a n x n grid and
return a list with the
Example: For a grid of [1, 2, 3], [4, 5, 6], [7, 8, 9] this would return a
result of [1,2,3,6,9,8,7,4,5].

"""

def spiralMatrixPrint(row, col, arr):
    # Defining the boundaries of the matrix.
    top = 0
    bottom = row-1
    left = 0
    right = col - 1

    # Defining the direction in which the array is to be traversed.
    dirc = 0
    res_arr = []
    
    while (top <= bottom and left <=right):    
        if dirc == 0:
            for i in range(left,right+1): # moving left->right
                res_arr.append(arr[top][i])

            # Since we have traversed the whole first
            # row, move down to the next row.
            top +=1
            dirc = 1

        elif dirc == 1:
            for i in range(top,bottom+1): # moving top->bottom
                res_arr.append(arr[i][right])

            # Since we have traversed the whole last
            # column, move down to the previous column.
            right -=1 
            dirc = 2
            
        elif dirc == 2:
            for i in range(right,left-1,-1): # moving right->left
                res_arr.append(arr[bottom][i])

            # Since we have traversed the whole last
            # row, move down to the previous row.
            bottom -=1
            dirc = 3
            
        elif dirc == 3:
            for i in range(bottom,top-1,-1): # moving bottom->top
                res_arr.append(arr[i][left])
            # Since we have traversed the whole first
            # column, move down to the next column.
            left +=1
            dirc = 0
            
    return res_arr

array = [[1,2,3],
     [4,5,6],
     [7,8,9]]
array_2 = [[1,2,3,4],
     [12,13,14,5],
     [11,16,15,6],
     [10,9,8,7]]

if __name__ == '__main__':
    # Checking with (3,3) Matrix
    print(spiralMatrixPrint(3, 3, array))
    # Checking with (4,4) Matrix
    print(spiralMatrixPrint(4, 4, array_2))
