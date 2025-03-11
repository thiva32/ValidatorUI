import bpy

checker_states = ["UNCHECKED","PASS","NEEDS_FIXING"]

def get_state(func_name):

    scene = bpy.context.scene
    return scene.get(f"validation_state_{func_name}","UNCHECKED")

def set_state(func_name,state):
    if state in checker_states:
        bpy.context.scene[f"validation_state_{func_name}"] = state
        print(f"validation state for {func_name} set to {state}")              
    else:
        print(f"invalid state: {state}")

