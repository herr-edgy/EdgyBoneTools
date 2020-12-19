import bpy
from . BoneScripts.FlipBones import *
from . BoneScripts.RotateBones import *
from . BoneScripts.ArmatureEdits import *
from . BoneScripts.ArmatureTransfers import *

### Per Bone Operators
class Bone_FlipXY_Operator(bpy.types.Operator):
    bl_idname = "bonehelpers.flip_xy"
    bl_label = "Flip XY"

    def execute(self, context):
        FlipBoneXY()
        bpy.ops.ed.undo_push()
        return {'FINISHED'}

class Bone_FlipYZ_Operator(bpy.types.Operator):
    bl_idname = "bonehelpers.flip_yz"
    bl_label = "Flip YZ"

    def execute(self, context):
        FlipBoneYZ()
        bpy.ops.ed.undo_push()
        return {'FINISHED'}

class Bone_FlipZX_Operator(bpy.types.Operator):
    bl_idname = "bonehelpers.flip_zx"
    bl_label = "Flip ZX"

    def execute(self, context):
        FlipBoneZX()
        bpy.ops.ed.undo_push()
        return {'FINISHED'}

class Bone_Roll_90_Operator(bpy.types.Operator):
    bl_idname = "bonehelpers.roll_90"
    bl_label = "Roll 90"

    def execute(self, context):
        RollBone90()
        bpy.ops.ed.undo_push()
        return {'FINISHED'}

class Bone_Rot_90_X_Operator(bpy.types.Operator):
    bl_idname = "bonehelpers.rot_90_x"
    bl_label = "Rot 90 X"

    def execute(self, context):
        Rotate90_X()
        bpy.ops.ed.undo_push()
        return {'FINISHED'}

class Bone_Rot_90_Z_Operator(bpy.types.Operator):
    bl_idname = "bonehelpers.rot_90_z"
    bl_label = "Rot 90 Z"

    def execute(self, context):
        Rotate90_Z()
        bpy.ops.ed.undo_push()
        return {'FINISHED'}

### Armature Edit Operators
class ArmatureEdit_Delete_R_Operator(bpy.types.Operator):
    bl_idname = "armatureedit.delete_r_bones"
    bl_label = "Delete right side"

    def execute(self, context):
        Delete_R_Bones()
        bpy.ops.ed.undo_push()
        return {'FINISHED'}

class ArmatureEdit_Add_UE4_IK_Bones(bpy.types.Operator):
    bl_idname = "armatureedit.add_ue4_ik_bones"
    bl_label = "Add UE4 IK Bones"

    def execute(self, context):
        Add_UE4_IK_Bones()
        bpy.ops.ed.undo_push()
        return {'FINISHED'}

### Armature Transfer Operators
class ArmatureTransfer_CopyOrientations(bpy.types.Operator):
    bl_idname = "armaturetransfer.copy_orientations"
    bl_label = "Copy orientations"

    def execute(self, context):
        CopyOrientations()
        bpy.ops.ed.undo_push()
        return {'FINISHED'}