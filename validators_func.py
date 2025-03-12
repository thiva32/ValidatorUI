from mathutils import Vector, Euler
from .statemanager import set_state
import bpy


# This is the function that will be called when the user clicks their respective validate button
@staticmethod
def freezetransform_func(validation_type):

    if validation_type not in ["check","fix"]:
        print("executing please specify a validation type")
        return {'FINISHED'}
    
    obj = bpy.context.active_object
    location = obj.location
    rotation = obj.rotation_euler
    scale = obj.scale
    

    #if the validation type is check, then we will check the transform
    if validation_type =="check":
        print("executing freezetransform_check")
    if  location == Vector((0.0,0.0,0.0)) and rotation == Euler((0.0,0.0,0.0)) and scale == Vector((1.0,1.0,1.0)):
        print("Transform is good") 
        set_state("freezetransform",'PASS')
    else:
        print("Transform is not good")
        set_state("freezetransform",'PASS') 
        
        

    #if the validation type is fix, then we will fix the transform
    if validation_type =="fix":
        bpy.ops.object.transform_apply(location=True,rotation=True,scale=True) 
        print("Transform Has Been Fixed")  
        set_state("freezetransform",'PASS')
        #rerun check to reconfirm that the transform has been fixed
        #freezetransform_func("check"),print("Executing Check for Safety")

    
    return {'FINISHED'}
    

@staticmethod
def ngon_func(validation_type):

    if validation_type =="check":
        print("executing ngon_check")
    elif validation_type =="fix":
        print("executing ngon_fix")
    else:
        print("Please specify a validation type")
    return {'FINISHED'}

@staticmethod
def non_manifold_func(validation_type):

    if validation_type =="check":
        print("executing non_manifold_check")
    elif validation_type =="fix":
        print("executing non_manifold_fix")
    else:
        print("Please specify a validation type")
    return {'FINISHED'}

@staticmethod
def loosegeometry_func(validation_type):
    
    if validation_type =="check":
        print("executing loosegeometry_check")
    elif validation_type =="fix":
        print("executing loosegeometry_fix")
    else:
        print("Please specify a validation type")
    return {'FINISHED'}
