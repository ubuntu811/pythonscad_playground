from openscad import *
from math import floor
import random

size=[200,150]
corner=10


def backpane(size=[100,200],r=10,z=[0,0]):
    [w,h] = size
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

scene += backpane(size,corner)
[w,h] = size
cutout = polygon([
                   [(w/2) - 1     , 5 ],
                   [(w/2) - 1     , 15],
                   [(w/2) - 1 - 5 , 15],
                   [(w/2) - 1 - 5 , 35],
                   [(w/2) - 1     , 35],

                   [(w/2) - 1     , h-30-35],
                   [(w/2) - 1 - 5 , h-30-35],
                   [(w/2) - 1 - 5 , h-30-15],
                   [(w/2) - 1     , h-30-15],

                   [(w/2) - 1     , h-30],
                   
                   [w - 40 + 1    , 30],
                   [(w/2) + 1     , 5],
                 ])
scene -= cutout

#cutout = polygon([
#                   [(w/2) - 1,h-30],
#                   [(w/2) + 1,h-30],
#                   [w - 40 + 1,30],
#                   [w - 40 - 1,30],
#                 ])
#scene -= cutout
#
#cutout = polygon([
#                   [w - 40 + 1,30],
#                   [w - 40 - 1,30],
#                   [(w/2) - 1,0],
#                   [(w/2) - 1,h-30],                   
#                 ])
#scene -= cutout



show(scene)