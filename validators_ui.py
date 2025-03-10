import bpy
from .validators_op import update_config


class MyPropertyGroup(bpy.types.PropertyGroup):

    '''Property group for storing validator properties'''

    config_preset : bpy.props.EnumProperty(name="Presets",
        items=[
            ('baseconfig', "None", ""),
            ('projectconfig_01', "Project 01", ""),
            ('projectconfig_02', "Project 02", "")
        ],
        
        default='baseconfig',  #default value                       
        update = update_config #update global variable when the value is changed

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

        current_config = scene.get("current_config",{}) #get the current config from the scene

        box = layout.box() 
        row = box.row(align=True)
        row.label(text="v 0.01")
        layout.prop(mypreset,"config_preset") #dropdown for the presets

        box = layout.box()
        row = box.row(align=True)
        row.label(text=" Mesh Validators:")  #label for the validators
        
        
        #list of validators
        #freezetransform function

        validators=[
            ('enable_freezetransform','object.freezetransform',"Freeze Transform",'CUBE'), #freezetransform
            ('enable_ngon','object.ngon',"N-gon",'CUBE'),                                  #ngon
            ('enable_non_manifold','object.non_manifold',"Non-Manifold",'CUBE'),           #non-manifold
            ('enable_loosegeometry','object.loosegeometry',"Loose Geometry",'CUBE')        #loosegeometry 
            
        ]
        
        #loop through the validators and add the operator to the UI
        for key,op_id,label,icon in validators:
            if current_config.get(key,True):
                row = box.row(align=True)
                row.operator(op_id, text=label, icon=icon)
    

        #separate the validate button with the rest of the validators
        box = layout.box()
        row = box.row(align=True)
        row.operator("object.validate", text="Validate", icon='ERROR')    



classes = [
            MyPropertyGroup,
            ValidatorsPanel
            ]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.my_preset = bpy.props.PointerProperty(type=MyPropertyGroup)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.my_preset