# getting openscad functions into namespace
from openscad import *

ipad_width=300
ipad_height=200
corner_radius=20

def backpane(w,h,r,z=[0,0]):
    scene = []    
    scene.append(polygon([
      [z[0] + r  , z[1]],
      [z[0] + w-r, z[1]],
      [z[0] + w-r, z[1] + h],
      [z[0] + r  , z[1] + h],
    ]))
    
    scene.append(polygon([
      [z[0]               , z[1] + r],
      [z[0]               , z[1] + h-r],
      [z[0] + r           , z[1] + h-r],
      [z[0] + r           , z[1] + r],
    ]))

    scene.append(polygon([
      [z[0] + w - r       , z[1] + r],
      [z[0] + w - r       , z[1] + h-r],
      [z[0] + w           , z[1] + h-r],
      [z[0] + w           , z[1] + r],
    ]))

    circle_0 = circle(r).translate([z[0] + r,z[1] +r])
    scene.append(circle_0)
    scene.append(circle_0.right(w-(2*r)))
    scene.append(circle_0.back(h-(2*r)))
    scene.append(circle_0.right(w-(2*r)).back(h-(2*r)))
    
    return(scene)
   
def border(w,h,r,z=[0,0]):
    scene = []    
    scene.append(polygon([
      [z[0] + r  , z[1]],
      [z[0] + w-r, z[1]],
      [z[0] + w-r, z[1] + h],
      [z[0] + r  , z[1] + h],
    ]))
    
    scene.append(polygon([
      [z[0]               , z[1] + r],
      [z[0]               , z[1] + h-r],
      [z[0] + r           , z[1] + h-r],
      [z[0] + r           , z[1] + r],
    ]))

    scene.append(polygon([
      [z[0] + w - r       , z[1] + r],
      [z[0] + w - r       , z[1] + h-r],
      [z[0] + w           , z[1] + h-r],
      [z[0] + w           , z[1] + r],
    ]))

    circle_0 = circle(r).translate([z[0] + r,z[1] +r])
    scene.append(circle_0)
    scene.append(circle_0.right(w-(2*r)))
    scene.append(circle_0.back(h-(2*r)))
    scene.append(circle_0.right(w-(2*r)).back(h-(2*r)))
    
    return(scene)
   
    
    
    
scene = []

scene += backpane(ipad_width,ipad_height,corner_radius,[0,0])

b=20
border = backpane(ipad_width+(2*b),ipad_height+(2*b),corner_radius+b,[0,ipad_height+2+(2*b)])
#border -= backpane(ipad_width,ipad_height,corner_radius,[b,b+ipad_height+2])

scene += border

#scene += backpane(ipad_width,ipad_height,corner_radius,[0,ipad_height+2])


show(scene)

