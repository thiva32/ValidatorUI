import bpy

def testvalidate_01_func(validation_type):

    if validation_type =="check":
        print("testvalidate_01_check")
    elif validation_type =="fix":
        bpy.ops.mesh.primitive_cube_add(size=1)
        print("testvalidate_01_fix")
    else:
        print("please specify a validation type")
    return {'FINISHED'}
    

def testvalidate_02_func(validation_type):

    if validation_type =="check":
        print("testvalidate_02_check")
    elif validation_type =="fix":
        print("testvalidate_02_fix")
    else:
        print("Please specify a validation type")
    return {'FINISHED'}

def testvalidate_03_func(validation_type):

    if validation_type =="check":
        print("testvalidate_03_check")
    elif validation_type =="fix":
        print("testvalidate_03_fix")
    else:
        print("Please specify a validation type")
    return {'FINISHED'}

def testvalidate_04_func(validation_type):
    
    if validation_type =="check":
        print("testvalidate_04_check")
    elif validation_type =="fix":
        print("testvalidate_04_fix")
    else:
        print("Please specify a validation type")
    return {'FINISHED'}