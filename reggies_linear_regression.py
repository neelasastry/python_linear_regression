This is done in script.py code academy embedded space for running the code itself.

# Task 1
# Write your get_y() function here
def get_y(m, b, x):
  y = m * x + b
  return y

# Uncomment each print() statement to check your work. Each of the following should print True
print(get_y(1, 0, 7) == 7)
print(get_y(5, 10, 3) == 25)


# Tasks 2 and 3
# Write your calculate_error() function here
def calculate_error(m , b, point):
  x_point = point[0]
  y_point = point[1]
  y_value = get_y(m,b,x_point)
  difference = y_value - y_point
  return abs(difference)

# Task 4
# Uncomment each print() statement and check the output against the expected result

# this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))

# the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))

# the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))

# the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))


# Task 5
# Write your calculate_all_error() function here
def calculate_all_error(m, b, point):
  total_error = 0
  for point in datapoints:
    total_error += calculate_error(m, b, point)
  return total_error



# Task 6
# Uncomment each print() statement and check the output against the expected result
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]

# every point in this dataset lies upon y=x, so the total error should be zero:
print(calculate_all_error(1, 0, datapoints))

# every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
print(calculate_all_error(1, 1, datapoints))

# every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
print(calculate_all_error(1, -1, datapoints))

# the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
print(calculate_all_error(-1, 1, datapoints))


# Tasks 8 and 9
possible_ms = [x / 10 for x in range(-100,101)]
possible_bs = [b / 10 for b in range(-20,21)]


# Task 10
datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf")
best_m = 0
best_b = 0

# Tasks 11, 12
for m in possible_ms:
  for b in possible_bs:
    error = calculate_all_error(m, b, datapoints) 
    if error < smallest_error:
      smallest_error = error
      best_m = m
      best_b = b
  print(best_m)
  print(best_b)
  print(smallest_error)

# Task 13
#get_y(m, b, x):
print(get_y(0.4, 1.6, 6))
print(f"Our model predicts that the 6cm ball will bounce 4.0m.")
