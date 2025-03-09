import bpy
from .validators_ot import current_config,update_config


class mypropertygroup(bpy.types.PropertyGroup):

    '''Property group for storing validator properties'''

    config_preset : bpy.props.EnumProperty(name="Presets",
        items=[
            ('baseconfig', "None", ""),
            ('projectconfig_01', "Project 01", ""),
            ('projectconfig_02', "Project 02", "")
        ],
        #setting the default value for the preset
        default='baseconfig', #default value
        #update global variable when the value is changed
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
        #force update the UI  
        layout = self.layout
        scene = context.scene
        mypreset = scene.my_preset

        current_config = scene.get("current_config",{})

        box = layout.box() 
        row = box.row(align=True)
        row.label(text="v 0.01")
        layout.prop(mypreset,"config_preset")
        box = layout.box()
        row = box.row(align=True)
        row.label(text=" Mesh Validators:")
        
        
        #list of validators
        #freezetransform function
        
        if current_config.get('enable_freezetransform',True):
            row = box.row(align=True)
            row.operator("object.freezetransform", text="Freeze Transform", icon='CUBE')

        if current_config.get('enable_ngon',True):
            row = box.row(align=True)
            row.operator("object.ngon", text="N-gon", icon='CUBE')
        
        if current_config.get('enable_non_manifold',True):
            row = box.row(align=True)
            row.operator("object.non_manifold", text="Non-Manifold", icon='CUBE')
        
        if current_config.get('enable_loosegeometry',True):
            row = box.row(align=True)
            row.operator("object.loosegeometry", text="Loose Geometry", icon='CUBE')

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