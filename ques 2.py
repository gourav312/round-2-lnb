# Taking input for the number of rows and columns
row, col = map(int, input().split())

# Initializing arrays
avg = [0] * col
ans = [0] * row
arr = []

# Taking input for the 2D array
for i in range(row):
    arr.append(list(map(int, input().split())))

# Calculating the average of each column
for i in range(col):
    for j in range(row):
        avg[i] += arr[j][i]
    avg[i] = avg[i] // row

# Finding the index of the minimum average
min_avg = avg[0]
eleminate_index = 0
for i in range(1, col):
    if avg[i] < min_avg:
        min_avg = avg[i]
        eleminate_index = i

# Calculating the sum of remaining subjects for each row
res = [0] * row
for i in range(row):
    for j in range(col):
        if eleminate_index != j:
            res[i] += arr[i][j]

# now results
for j in range(row):
    print(res[j], end=" ")
