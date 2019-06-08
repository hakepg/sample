'''
print('pattern 51')
n = 5
for row in range(n,0,-1):
    print('  '*(n-row), end='')
    for column in range(row*2-1):
        print(chr(64+row),end=' ')
    print()
'''
'''
print('pattern 52')
n=10
for row in range(n,0,-2):
    print(' '*(n-row),end=' ')
    for column in range(1,row):
        print(chr(64+row-1),end=' ')
    print()
'''
'''
print('pattern 53')
n=5
for row in range(n,0,-1):
    print('  '*(n-row), end = ' ')
    for column in range(row*2-1):
        print(chr(65+column), end = ' ')
    print()
'''

# print('pattern 54')
# n=5
# for row in range(1,n+1):
#     print(''*(n-row), end = '')
#     for column in range(1,row+1):
#         print(column, end = '')
#         print()
#     for j in range(1,row):
#             print(''*j, end= '')
#             for k in range(1,n+1-j):
#                 print(k,end='')
#             print()

print('pattern 55')
n = 15
for row in range(1,n+1):
    for column in range(row):
        print(row, end = ' ')
    print()