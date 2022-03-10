import numpy as np

num_list = [int(line) for line in open('/content/drive/MyDrive/Advent/advent1.txt').readlines()]

# ---- PART I ----

higher_depth = 0
for line in range(1, len(num_list)):
  if num_list[line] > num_list[line - 1]:
    higher_depth += 1
print("The answer to Part 1 is:", higher_depth)

# ---- PART II ----

slider_depth = 0
slider_sum = np.convolve(num_list, np.ones(3,dtype=int), 'valid')
for line in range(1, len(slider_sum)):
  if slider_sum[line] > slider_sum[line - 1]:
    slider_depth += 1
print("The answer to Part 2 is:", slider_depth)
