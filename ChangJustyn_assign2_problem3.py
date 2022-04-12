"""
Assignment #2, Problem #3
Justyn Chang
"""
#print title sequence
print("Minecraft block distance calculator")
print()

#create inputs for block 1 and 2 x, y, z values
block1_x = int(input("Block #1 x: "))
block1_y = int(input("Block #2 y: "))
block1_z = int(input("Block #3 z: "))
block2_x = int(input("Block #2 x: "))
block2_y = int(input("Block #2 y: "))
block2_z = int(input("Block #2 z: "))
print()

#calculate x, y, z distances between block 1 and 2
x_dist = abs(block1_x - block2_x)
y_dist = abs(block1_y - block2_y)
z_dist = abs(block1_z - block2_z)
print("X distance: ", x_dist)
print("Y distance: ", y_dist)
print("Z distance: ", z_dist)

#calculate straight line distance between block 1 and 2
import math
straight_line = math.sqrt(math.pow(x_dist, 2) + math.pow(y_dist, 2) + math.pow(z_dist, 2))
fstraight = format(straight_line, ".2f")
print("Straight line distance: ", fstraight)
