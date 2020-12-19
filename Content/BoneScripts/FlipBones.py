import bpy
import math
from math import radians
from mathutils import Matrix

def FlipBoneXY():
    bones = bpy.context.selected_editable_bones
    if len(bones) == 0:
        raise RuntimeError("No bones selected in edit mode!")

    bpy.context.scene.transform_orientation_slots[0].type = 'NORMAL'
    bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
    # for bone in bones:
    #     roll = bone.roll
    #     bone.roll = roll + 0.5 * math.pi

  
    for bone in bones:
        old_head = bone.head.copy()
        R = Matrix.Rotation(radians(180), 4, bone.z_axis.normalized())
        bone.transform(R, roll=True) 
        offset_vec = -(bone.head - old_head)
        bone.head += offset_vec
        bone.tail += offset_vec

def FlipBoneYZ():
    bones = bpy.context.selected_editable_bones
    if len(bones) == 0:
        raise RuntimeError("No bones selected in edit mode!")

    bpy.context.scene.transform_orientation_slots[0].type = 'NORMAL'
    bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
    # for bone in bones:
    #     roll = bone.roll
    #     bone.roll = roll + 0.5 * math.pi

    
    for bone in bones:
        old_head = bone.head.copy()
        R = Matrix.Rotation(radians(180), 4, bone.x_axis.normalized())
        bone.transform(R, roll=True) 
        offset_vec = -(bone.head - old_head)
        bone.head += offset_vec
        bone.tail += offset_vec

def FlipBoneZX():
    bones = bpy.context.selected_editable_bones
    if len(bones) == 0:
        raise RuntimeError("No bones selected in edit mode!")

    bpy.context.scene.transform_orientation_slots[0].type = 'NORMAL'
    bpy.context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
    # for bone in bones:
    #     roll = bone.roll
    #     bone.roll = roll + 0.5 * math.pi

    for bone in bones:
        old_head = bone.head.copy()
        R = Matrix.Rotation(radians(180), 4, bone.y_axis.normalized())
        bone.transform(R, roll=True) 
        offset_vec = -(bone.head - old_head)
        bone.head += offset_vec
        bone.tail += offset_vec


def RollBone90():
    bones = bpy.context.selected_editable_bones
    if len(bones) == 0:
        raise RuntimeError("No bones selected in edit mode!")

    for bone in bones:
        roll = bone.roll
        print(roll)
        newRoll = roll + 0.5 * math.pi
        print(newRoll)
        if(newRoll > 2.0 * math.pi):
            print(newRoll)
            newRoll = newRoll - 2.0 * math.pi
        bone.roll = newRoll