size = input("Enter the size of the Square Matrix : ")
matrix = [[0 for x in range(size)] for y in range(size)]

primary = 0
secondary = 0

# get values for matrix
for i in range(0, size) :
    for j in range(0, size):
        matrix[i][j] = input("Enter the matrix value of matrix[%d][%d]" % (i,j))

for i in range(0,size) :
    primary = primary + matrix[i][i]
for i in range(0,size) :
    size = size - 1
    secondary = secondary + matrix[i][size]


print "primary diagonal is : ", primary
print "secondary diagonal is : ", secondary

abs_diff = abs(primary - secondary)

print "Abs diff is : ", abs_diff
