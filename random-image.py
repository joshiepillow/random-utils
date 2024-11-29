import random

height = 10
width = 2
print("image-data-to-image(",height,", ",width,", [list:",sep = '')
for i in range(height):
    print("[list:")
    for j in range(width):
        print("color(",random.randint(0, 255),",",random.randint(0,255),",",random.randint(0,255),")",end="",sep = '')
        if (j != width - 1):
          print(",")
        elif (i != height - 1): 
          print("],")
print("]])")
