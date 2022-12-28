n = int(input())
matrix = []
for i in range(n):
    loc = input()
    matrix.append(loc)

print(matrix)

princes_pos = []
bot_pos = [(n-1)//2,(n-1)//2] #Due to center always

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (matrix[i][j]=='p'):
            princes_pos.append(i)
            princes_pos.append(j)

# print(prices_pos,bot_pos)


directions = []
# FOR UPWARD AND DOWNWARD
if (princes_pos[0]>bot_pos[0]):
    for i in range(princes_pos[0] - bot_pos[0]):
        directions.append('DOWN')
else:
    for i in range(bot_pos[0] - princes_pos[0]):
        directions.append('UP')

# print(directions)

# FOR LEFT AND RIGHT
if (princes_pos[1]>bot_pos[1]):
    for i in range(princes_pos[1] - bot_pos[1]):
        directions.append("RIGHT")
else:
    for i in range(bot_pos[1] - princes_pos[1]):
        directions.append("LEFT")

# print(directions)
for i in directions:
    print(i)