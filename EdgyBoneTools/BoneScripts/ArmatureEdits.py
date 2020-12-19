import bpy
from mathutils import Vector

def Delete_R_Bones():
    active_object = bpy.context.active_object
    if active_object.type != 'ARMATURE':
        raise TypeError("No armature as active object!")

    armature = active_object.data
    bpy.ops.object.mode_set(mode='EDIT')

    print("hello")
    for bone in armature.edit_bones:
        if bone.name.endswith("_r") or bone.name.endswith("_R"): 
            armature.edit_bones.remove(bone)

def Add_UE4_IK_Bones():
    active_object = bpy.context.active_object
    if active_object.type != 'ARMATURE':
        raise TypeError("No armature as active object!")

    armature = active_object.data
    bpy.ops.object.mode_set(mode='EDIT')

    hand_l_bone = armature.edit_bones.get('hand_l')
    hand_r_bone = armature.edit_bones.get('hand_r')
    foot_l_bone = armature.edit_bones.get('foot_l')
    foot_r_bone = armature.edit_bones.get('foot_r')    

    allExist = hand_l_bone is not None and foot_l_bone is not None and hand_r_bone is not None and foot_r_bone is not None

    # check if we have all left side bones
    if allExist is not True:
        raise TypeError("Required bones are missing")

    ik_hand_root_bone = armature.edit_bones.get('ik_hand_root')
    ik_hand_gun_bone = armature.edit_bones.get('ik_hand_gun')
    ik_hand_l_bone = armature.edit_bones.get('ik_hand_l')
    ik_hand_r_bone = armature.edit_bones.get('ik_hand_r')
    ik_foot_root_bone = armature.edit_bones.get('ik_foot_root')
    ik_foot_l_bone = armature.edit_bones.get('ik_foot_l')
    ik_foot_r_bone = armature.edit_bones.get('ik_foot_r')

    lengthOfBones = 10
   
    if ik_hand_root_bone is None:
        ik_hand_root_bone = armature.edit_bones.new('ik_hand_root')
        ik_hand_root_bone.head = Vector((0,0,0))
        ik_hand_root_bone.tail = Vector((0,lengthOfBones,0))
    if ik_hand_gun_bone is None:
        ik_hand_gun_bone = armature.edit_bones.new('ik_hand_gun')
        ik_hand_gun_bone.head = hand_r_bone.head
        ik_hand_gun_bone.tail = hand_r_bone.tail - Vector((0,5,0))
        ik_hand_gun_bone.matrix = hand_r_bone.matrix
        ik_hand_gun_bone.parent = ik_hand_root_bone
    if ik_hand_l_bone is None:
        ik_hand_l_bone = armature.edit_bones.new('ik_hand_l')
        ik_hand_l_bone.head = hand_l_bone.head
        ik_hand_l_bone.tail = hand_l_bone.tail - Vector((0,5,0))
        ik_hand_l_bone.matrix = hand_l_bone.matrix
        ik_hand_l_bone.parent = ik_hand_gun_bone
    if ik_hand_r_bone is None:
        ik_hand_r_bone = armature.edit_bones.new('ik_hand_r')
        ik_hand_r_bone.head = hand_r_bone.head
        ik_hand_r_bone.tail = hand_r_bone.tail - Vector((0,5,0))
        ik_hand_r_bone.matrix = hand_r_bone.matrix
        ik_hand_r_bone.parent = ik_hand_gun_bone 
    if ik_foot_root_bone is None:
        ik_foot_root_bone = armature.edit_bones.new('ik_foot_root')
        ik_foot_root_bone.head = Vector((0,0,0))
        ik_foot_root_bone.tail = Vector((0,lengthOfBones, 0))
    if ik_foot_l_bone is None:
        ik_foot_l_bone = armature.edit_bones.new('ik_foot_l')
        ik_foot_l_bone.head = foot_l_bone.head
        ik_foot_l_bone.tail = foot_l_bone.tail - Vector((0,5,0))
        ik_foot_l_bone.matrix = foot_l_bone.matrix
        ik_foot_l_bone.parent = ik_foot_root_bone
    if ik_foot_r_bone is None:
        ik_foot_r_bone = armature.edit_bones.new('ik_foot_r')
        ik_foot_r_bone.head = foot_r_bone.head
        ik_foot_r_bone.tail = foot_r_bone.tail - Vector((0,5,0))
        ik_foot_r_bone.matrix = foot_r_bone.matrix
        ik_foot_r_bone.parent = ik_foot_root_bone