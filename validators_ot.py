import bpy
from bpy.props import StringProperty
from .validators_func import freezetransform_func, ngon_func, non_manifold_func, loosegeometry_func
from .loadconfig import load_config

#loadvalidator config
current_config = {}

#update the config
def update_config(self, context):
    #config = load_config(self.config_preset)
    current_config = load_config(self.config_preset)
    print (f'updated config : {current_config}')

    context.scene["current_config"] = current_config


class OT_Validate(bpy.types.Operator):
    '''Operator that executes all validator options'''

    bl_idname = "object.validate"
    bl_label = "Validate"
    bl_options = {'REGISTER', 'UNDO'}
    
    #Adds a string property to the operator to specify the validation type
    validation_type: bpy.props.StringProperty(
        name="Validation Type", 
        default="check", #default value
        options={'HIDDEN'} #hide the property from the user
        ) # type: ignore

    @classmethod
    #only allow users to execute if an object is selected

    def poll(cls, context):
        return context.active_object is not None 

    def execute(self, context):
        """Main function to execute all validators"""


        return {'FINISHED'}
    

class BaseValidatorOperator(bpy.types.Operator):
    """Base class for validators operators"""

    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None and current_config.get(f'enable_{cls.validator_key}',True)

    def execute(self, context):
        result = self.validator_function(self.validation_type)
        return result
    
    def invoke(self, context, event):
        """call execute when the operator is invoked"""
        return self.execute(context)
    



class OT_freezetransform(BaseValidatorOperator):
    """Operator that executes freezetranform validator"""

    bl_idname = "object.freezetransform"
    bl_label = "Freeze Transform"
    validator_key = "freezetransform"
    validator_function = freezetransform_func
    validation_type = "check"

    

class OT_ngon(BaseValidatorOperator):
    """Operator that executes ngon validator"""

    bl_idname = "object.ngon"
    bl_label = "N-gon"
    validator_key = "ngon"
    validator_function = ngon_func
    validation_type = "check"
    
class OT_non_manifold(BaseValidatorOperator):
    """Operator that executes non-manifold validator"""
    
    bl_idname = "object.non_manifold"
    bl_label = "Non-manifold"
    validator_key = "non_manifold"
    validator_function = non_manifold_func
    validation_type = "check"

class OT_loosegeometry(BaseValidatorOperator):
    """Operator that executes loosegeometry validator"""
    
    bl_idname = "object.loosegeometry"
    bl_label = "Loose Geometry"
    validator_key = "loosegeometry"
    validator_function = loosegeometry_func
    validation_type = "check"
    
    

validateoroperators = [OT_Validate, OT_freezetransform, OT_ngon, OT_non_manifold, OT_loosegeometry]

def register():
    for operator in validateoroperators:
        bpy.utils.register_class(operator)

def unregister():
    for operator in validateoroperators:
        bpy.utils.unregister_class(operator)