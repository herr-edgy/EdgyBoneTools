
bl_info = {
    "name" : "EdgyBoneTools",
    "author" : "Mateo Egey",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "Screen",
    "warning" : "",
    "category" : "Herr Edgy"
}

import bpy

from . BoneOperators import *
from . BonePanels import *

classes = (
    Bone_PT_PerBonePanel,
    Bone_PT_ArmatureEditPanel,
    Bone_PT_ArmatureTransferPanel,

    Bone_FlipXY_Operator,
    Bone_FlipYZ_Operator,
    Bone_FlipZX_Operator,
    Bone_Rot_90_X_Operator,
    Bone_Roll_90_Operator,
    Bone_Rot_90_Z_Operator,
    
    ArmatureEdit_Delete_R_Operator,
    ArmatureEdit_Add_UE4_IK_Bones,

    ArmatureTransfer_CopyOrientations
)

def draw_item(self, context):
    layout = self.layout
    layout.menu(Bone_PT_PerBonePanel.bl_idname)
    layout.menu(Bone_PT_ArmatureEditPanel.bl_idname)
    layout.menu(Bone_PT_ArmatureTransferPanel.bl_idname)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # lets add ourselves to the main header
    #bpy.types.INFO_HT_header.append(draw_item)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    #bpy.types.INFO_HT_header.remove(draw_item)
