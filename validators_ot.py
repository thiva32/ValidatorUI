import bpy,bpy.props
from .validators_func import *
from .loadconfig import load_config

#loadvalidator config
current_config = {}

def update_config(self, context):
    global current_config
    current_config = load_config(self.config_preset)
    print (f'{current_config}')


class OT_Validate(bpy.types.Operator):
    '''Operator that executes all validator options'''

    bl_idname = "object.validate"
    bl_label = "Validate"
    bl_options = {'REGISTER', 'UNDO'}


    @classmethod
    #only allow users to execute if an object is selected

    def poll(cls, context):
        return context.active_object is not None 

    def execute(self, context):
        """Main function to execute all validators"""


        return {'FINISHED'}

class OT_Validate_01(bpy.types.Operator):
    """Operator that executes validator 01"""

    bl_idname = "object.validate_01"
    bl_label = "Validate 01"
    bl_options = {'REGISTER', 'UNDO'}

    validation_type: bpy.props.StringProperty(name="Validation Type", default="check") # type: ignore

    @classmethod
    #only allow users to execute if an object is selected

    def poll(cls, context):
        return context.active_object is not None and current_config.get('enable_validate_01',True)
    
    def execute(self, context):
        result = testvalidate_01_func(self.validation_type)
        return result
    
class OT_Validate_02(bpy.types.Operator):
    """Operator that executes validator 02"""

    bl_idname = "object.validate_02"
    bl_label = "Validate 02"
    bl_options = {'REGISTER', 'UNDO'} 

    validation_type: bpy.props.StringProperty(name="Validation Type", default="check") # type: ignore

    @classmethod
    #only allow users to execute if an object is selected

    def poll(cls, context):
        return context.active_object is not None and current_config.get('enable_validate_02',True)
    
    def execute(self, context):
        result = testvalidate_02_func(self.validation_type)
        return result
    
class OT_Validate_03(bpy.types.Operator):
    """Operator that executes validator 03"""

    bl_idname = "object.validate_03"
    bl_label = "Validate 03"
    bl_options = {'REGISTER', 'UNDO'} 

    validation_type: bpy.props.StringProperty(name="Validation Type", default="check") # type: ignore

    @classmethod
    #only allow users to execute if an object is selected

    def poll(cls, context):
        return context.active_object is not None and current_config.get('enable_validate_03',True)
    
    def execute(self, context):
        result = testvalidate_03_func(self.validation_type)
        return result

class OT_Validate_04(bpy.types.Operator):
    """Operator that executes validator 02"""

    bl_idname = "object.validate_04"
    bl_label = "Validate 04"
    bl_options = {'REGISTER', 'UNDO'} 

    validation_type: bpy.props.StringProperty(name="Validation Type", default="check") # type: ignore

    @classmethod
    #only allow users to execute if an object is selected

    def poll(cls, context):
        return context.active_object is not None and current_config.get('enable_validate_04',True)
    
    def execute(self, context):
        result = testvalidate_04_func(self.validation_type)
        return result
    

validateoroperators = [OT_Validate,OT_Validate_01,OT_Validate_02,OT_Validate_03,OT_Validate_04]

def register():
    for operator in validateoroperators:
        bpy.utils.register_class(operator)

def unregister():
    for operator in validateoroperators:
        bpy.utils.unregister_class(operator)