import maya.cmds as cmds
import random
#random number of objects
num_objects = random.randint(0, 10)
#type of object created
for i in range(num_objects):
    if i % 2 == 0:
        obj = cmds.polyCube()[0]
    else:
        obj = cmds.polySphere()[0]
        
    #random position
    random_x = random.uniform(-10,30)
    random_y = random.uniform(10,30)
    random_z = random.uniform(-10,30)
    
    cmds.move(random_x, random_y, random_z, obj)
    
    new_position = random_x, random_y, random_z
    
    #random scale
    scale_value = random.uniform(0.5, 3)
    cmds.scale(scale_value, scale_value, scale_value, obj)
    
    #label
    if scale_value > 1:
        label = "large"
    elif scale_value < 1:
        label = "small"    
    else:
        label = ""
        
    #change name
    if label:
        new_name = f"{obj}_{label}"
    else:
        new_name = obj
        
    #rename
    cmds.rename(obj, new_name)
    
    #debug
    print(f"{new_name}, {new_position[0]:.2f}, {new_position[1]:.2f}, {new_position[2]:.2f}")
