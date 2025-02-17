import random
import maya.cmds as cmds

#create random objects function
def create_random_obj():
    choice = random.choice(['cube', 'sphere', 'cylinder', 'cone'])
    if choice == 'cube':
        return cmds.polyCube()[0]
    elif choice == 'sphere':
        return cmds.polySphere()[0]
    elif choice == 'cylinder':
        return cmds.polyCylinder()[0]
    else:
        return cmds.polyCone()[0]      

#assign random positions
def random_position(obj):
    position_x = random.uniform(-10, 10)
    position_y = random.uniform(0, 10)
    position_z = random.uniform(-10, 10)
#move to random positions
    cmds.move(position_x, position_y, position_z,obj)

#scale randomization function
def random_scale(obj):
    scale_value = random.uniform(0.5, 4)
#scale 
    cmds.scale(scale_value, scale_value, scale_value, obj)
    return scale_value

#get size and rename function
def object_size(obj, scale_value):
    if scale_value > 1:
        size = "large"
    elif scale_value < 1:
        size = "small"
    else:
        size = ""
    cmds.rename(f"{obj}_{size}")
           
def main():
    num_objects = random.randint(5, 20)
    for _ in range(num_objects):
        obj = create_random_obj()
        random_position(obj)
        scale_value = random_scale(obj)
        object_size(obj, scale_value)
        
        
main()
