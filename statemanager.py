import bpy

state_manager = {}

def set_state(operator_name,state):

    state_manager[operator_name] = state
    bpy.context.scene.validation_states = str(state_manager)

def get_state(operator_name):
    return state_manager.get(operator_name,'UNCHECKED')


def register_state():
    bpy.types.Scene.validation_states = bpy.props.StringProperty(name="ValidationStates")

def unregister_state():
    del bpy.types.Scene.validation_states


