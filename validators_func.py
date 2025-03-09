import bpy


# This is the function that will be called when the user clicks their respective validate button
@staticmethod
def freezetransform_func(validation_type):

    if validation_type =="check":
        print("executing freezetransform_check")
    elif validation_type =="fix":
        print("freezetransform_fix")
    else:
        print("executing please specify a validation type")
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
