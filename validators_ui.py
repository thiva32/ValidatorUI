import bpy
from .validators_ot import current_config,update_config


class mypropertygroup(bpy.types.PropertyGroup):
    '''Property group for storing validator properties'''

    config_preset : bpy.props.EnumProperty(name="Preset",
        items=[
            ('projectconfig_01', "Project 01", ""),
            ('projectconfig_02', "Project 02", "")
        ],
        default='projectconfig_01', #default value
        update = update_config
        ) # type: ignore
    
class ValidatorsPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Validator"
    bl_idname = "OBJECT_PT_validators"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Validator'

    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
        mypreset = scene.my_preset

        box = layout.box() 
        row = box.row(align=True)
        row.label(text="v 0.01")

        box = layout.box()
        row = box.row(align=True)
        row.label(text=" Mesh Validators:")
        row = box.row(align=True)
        layout.prop(mypreset,"config_preset")
        
        
        if current_config.get('enable_validate_01',True):
            row = box.row(align=True)
            row.operator("object.validate_01", text="Validate 01", icon='CUBE')

        if current_config.get('enable_validate_02',True):
            row = box.row(align=True)
            row.operator("object.validate_02", text="Validate 02", icon='CUBE')
        
        if current_config.get('enable_validate_03',True):
            row = box.row(align=True)
            row.operator("object.validate_03", text="Validate 03", icon='CUBE')
        
        if current_config.get('enable_validate_04',True):
            row = box.row(align=True)
            row.operator("object.validate_04", text="Validate 04", icon='CUBE')

        #separate the validate button with the rest of the validators
        box = layout.box()
        row = box.row(align=True)
        row.operator("object.validate", text="Validate", icon='ERROR')    



validatorpanels = [mypropertygroup,ValidatorsPanel]

def register():
    for panel in validatorpanels:
        bpy.utils.register_class(panel)

    bpy.types.Scene.my_preset = bpy.props.PointerProperty(type=mypropertygroup)

def unregister():
    for panel in validatorpanels:
        bpy.utils.unregister_class(panel)

    del bpy.types.Scene.my_preset