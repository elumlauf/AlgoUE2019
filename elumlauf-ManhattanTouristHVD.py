import sys

stopprogram=0

def ManhattanTourist(n_down, n_right, down_matrix, right_matrix, diag_matrix):

    s_dict = {(0,0):0}

    for i in range(1, n_down + 1):
        s_dict[(i,0)] = s_dict[(i-1,0)] + down_matrix[i-1][0]

    for j in range(1, n_right + 1):
        s_dict[(0,j)] = s_dict[(0,j-1)] + right_matrix[0][j-1]

    # calculation
    for i in range(1, n_down + 1):
        for j in range(1, n_right + 1):
            s_dict[(i,j)] = max(s_dict[(i-1,j)]+down_matrix[i-1][j], s_dict[(i,j-1)] + right_matrix[i][j-1],s_dict[(i-1,j-1)] + diag_matrix[i-1][j-1])
    return s_dict[(n_down, n_right)]

if __name__ == "__main__":
    fin = sys.stdin
    line = fin.readline().rstrip('\n')
    down_matrix =[]
    while line != '---':
        if not line.startswith('G'):
            down_matrix.append([float(ii) for ii in line.split()])
        line = fin.readline().rstrip('\n')

    line = fin.readline().rstrip('\n')
    right_matrix=[]
    while line != '---':
        if not line.startswith('G'):
            right_matrix.append([float(ij) for ij in line.split()])
        line = fin.readline().rstrip('\n')

    line = fin.readline().rstrip('\n')
    diag_matrix=[]
    while line != '---':
        if not line.startswith('G'):
            diag_matrix.append([float(ijk) for ijk in line.split()])
        line = fin.readline().rstrip('\n')

    test_rightmatrixrows=len(right_matrix)
    test_rightmatrixelements=len(right_matrix[0])
    test_downmatrixrows=len(down_matrix)
    test_downmatrixelements=len(down_matrix[0])
    test_diagmatrixelements=len(diag_matrix[0])
    test_diagmatrixrows=len(diag_matrix)

    for right in range(0,test_rightmatrixrows):
        if len(right_matrix[right]) != test_rightmatrixelements:
            print ("Incorrect number of elements (right Matrix)!")
            stopprogram=1
            break
        if len(right_matrix[right]) != test_downmatrixrows:
            print ("Incorrect number of elements!")
            stopprogram=1
            break
    for down in range(0,test_downmatrixrows):
        if len(down_matrix[down]) != test_downmatrixelements:
            print ("Incorrect number of elements (down Matrix)!")
            stopprogram=1
            break
        if len(down_matrix[down]) != test_rightmatrixrows:
            print ("Incorrect number of elements!")
            stopprogram=1
            break
    for diag in range(0,test_diagmatrixrows):
        if len(diag_matrix[diag]) != test_diagmatrixelements:
            print ("Incorrect number of elements (diagonal Matrix)!")
            stopprogram=1
            break
        if len(diag_matrix) != len(right_matrix[0]):
            print ("Incorrect number of rows (diagonal Matrix)!")
            stopprogram=1
            break

    # run function

    n_down=test_downmatrixrows
    n_right=test_rightmatrixelements
    n_diag=test_diagmatrixelements

    if stopprogram==0:
        output = ManhattanTourist(n_down, n_right, down_matrix, right_matrix, diag_matrix)

        #output result
        print (output)
