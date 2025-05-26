from openscad import *
from math import floor
from pprint import pprint
import random

base_x = 438
base_y = 630
material = 4.9

step=100
height=70
hole_diam=20
cut=height/2
count_x=floor(base_x/(step+material))
count_y = floor(base_y/(step+material))

dist_x = base_x / count_x
dist_y = base_y / count_y

print(dist_x)
print(dist_y)

def path_x(height,material,count_x,dist_x,y_offset_m=0,hole="left",hole_diam=20):
    path = [
        [0,y_offset_m+0],
        [0,y_offset_m+height]
    ]
    
    for i in range(1,count_x):
        path.append([i*dist_x,y_offset_m+height])
        path.append([i*dist_x,y_offset_m+height-cut])
        path.append([(i*dist_x)+material,y_offset_m+height-cut])
        path.append([(i*dist_x)+material,y_offset_m+height])
    
    end_x = ((i+1)*dist_x)
    hole_y = y_offset_m + (height/2)
    
    path.append([end_x,y_offset_m+height])
    path.append([end_x,y_offset_m+0])
    
    if hole == "right":
        the_hole=circle(hole_diam).translate([end_x-(dist_x/2),hole_y])
    else:
        the_hole=circle(hole_diam).translate([(dist_x/2),hole_y])        
    
    rand_int = random.randint(2,count_x-1)
    print(rand_int)
    rand_hole = circle(hole_diam).translate([(rand_int*dist_x)-(dist_x/2),hole_y])
    print(rand_hole)
    
    return(polygon(path).difference(rand_hole).difference(the_hole))

def path_y(height,material,count_y,dist_y,x_offset_m=600, y_offset_m=0,hole_diam=20):
    cut = height/2
    path = [
        [x_offset_m,y_offset_m+0],
        [x_offset_m,y_offset_m+height]
    ]
    
    for i in range(1,count_y):
        path.append([x_offset_m + (i*dist_y),y_offset_m+height])
        path.append([x_offset_m + (i*dist_y),y_offset_m+height-cut])
        path.append([x_offset_m + (i*dist_y)+material,y_offset_m+height-cut])
        path.append([x_offset_m + (i*dist_y)+material,y_offset_m+height])
        
    
    end_x = ((i+1)*dist_y)
    
    path.append([x_offset_m + end_x,y_offset_m+height])
    path.append([x_offset_m + end_x,y_offset_m+0])    

    return(polygon(path))


out = []
for i in range(0,count_y-1):
    if i % 2:
        hole="left"
    else:
        hole="right"
        
    print(hole)
    out.append(path_x(height,material,count_x,dist_x,y_offset_m=i*(height+1),hole=hole))

holeys = []
x_offset_again = 600
hole = circle(hole_diam).translate([x_offset_again + (dist_x/2),height/2])
#holeys.append(hole)
max_rand_x = int(floor(((dist_x/2) - hole_diam - 10)))
max_rand_y = int(floor(((height/2) - hole_diam - 10)))

print(f"Rand_x: {max_rand_x}")
print(f"Rand_y: {max_rand_y}")

for x in range(0,count_y):
    for y in range(0,count_x):
        print(f"{x} {y}")
        rand_x = random.randint(-max_rand_x,max_rand_x)
        rand_y = random.randint(-max_rand_y,max_rand_y)
        holeys.append(hole.right((x*(dist_y))+rand_x).back((y*(height+1))+rand_y))
    
pprint(holeys)

for i in range(0,count_x-1):       
    out.append(path_y(height,material,count_y,dist_y,x_offset_m=x_offset_again, y_offset_m=i*(height+1)).difference(holeys))
    

        

#out += holeys

show(out)
