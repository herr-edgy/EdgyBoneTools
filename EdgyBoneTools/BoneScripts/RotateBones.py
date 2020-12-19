import bpy
import math
from math import radians
from mathutils import Matrix

def Rotate90_X():
    bones = bpy.context.selected_editable_bones
    if len(bones) == 0:
        raise RuntimeError("No bones selected in edit mode!")

    bpy.context.scene.transform_orientation_slots[0].type = 'NORMAL'
    bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
    # for bone in bones:
    #     roll = bone.roll
    #     bone.roll = roll + 0.5 * math.pi

    bone = bones[0]

    old_head = bone.head.copy()
    R = Matrix.Rotation(radians(90), 4, bone.x_axis.normalized())
    bone.transform(R, roll=True) 
    offset_vec = -(bone.head - old_head)
    bone.head += offset_vec
    bone.tail += offset_vec

def Rotate90_Z():
    bones = bpy.context.selected_editable_bones
    if len(bones) == 0:
        raise RuntimeError("No bones selected in edit mode!")

    bpy.context.scene.transform_orientation_slots[0].type = 'NORMAL'
    bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
    # for bone in bones:
    #     roll = bone.roll
    #     bone.roll = roll + 0.5 * math.pi

    bone = bones[0]

    old_head = bone.head.copy()
    R = Matrix.Rotation(radians(90), 4, bone.z_axis.normalized())
    bone.transform(R, roll=True) 
    offset_vec = -(bone.head - old_head)
    bone.head += offset_vec
    bone.tail += offset_vec