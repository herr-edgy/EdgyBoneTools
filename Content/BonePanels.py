import bpy

class Bone_PT_PerBonePanel(bpy.types.Panel):
    bl_idname = "BONE_PT_PerBonePanel"
    bl_label = "Bone Manipulation"
    bl_category = "Tool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('bonehelpers.flip_xy', text="Flip XY")
        row.operator('bonehelpers.flip_yz', text="Flip YZ")
        row.operator('bonehelpers.flip_zx', text="Flip ZX")

        boneRotationRow = layout.row()
        boneRotationRow.operator('bonehelpers.rot_90_x', text="Rot 90 X")
        boneRotationRow.operator('bonehelpers.roll_90', text="Rot 90 Y")
        boneRotationRow.operator('bonehelpers.rot_90_z', text="Rot 90 Z")

    @classmethod
    def poll(cls, context):
        if bpy.context.object.mode != 'EDIT':
            return False
        if bpy.context.mode != 'EDIT_ARMATURE':
            return False
        
        bones = bpy.context.selected_editable_bones
        #print(bones)
        return len(bones) > 0

class Bone_PT_ArmatureEditPanel(bpy.types.Panel):
    bl_idname = "BONE_PT_ArmatureEditPanel"
    bl_label = "Armature Edit"
    bl_category = "Tool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('armatureedit.add_ue4_ik_bones', text="Add UE4 IK Bones")
        row2 = layout.row()
        row2.operator('armatureedit.delete_r_bones', text="Delete right bones")

    @classmethod
    def poll(cls, context):
        if bpy.context.object.mode != 'OBJECT':
            return False
        
        armatures = bpy.context.selected_objects
        conditionFulfilled = len(armatures) == 1 and armatures[0].type == 'ARMATURE'
        return conditionFulfilled

class Bone_PT_ArmatureTransferPanel(bpy.types.Panel):
    bl_idname = "BONE_PT_ArmatureTransferPanel"
    bl_label = "Armature Transfer"
    bl_category = "Tool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('armaturetransfer.copy_orientations', text="Copy orientations")

    @classmethod
    def poll(cls, context):
        if bpy.context.object.mode != 'OBJECT':
            return False
        
        armatures = bpy.context.selected_objects
        conditionFulfilled = len(armatures) == 2 and armatures[0].type == 'ARMATURE' and armatures[1].type == 'ARMATURE'
        return conditionFulfilled
        