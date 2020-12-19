import bpy

def CopyOrientations():
    arma_a = bpy.context.selected_objects[0]
    arma_b = bpy.context.selected_objects[1]

    if arma_b == bpy.context.active_object:
        arma_tmp = arma_a
        arma_a = arma_b
        arma_b = arma_tmp

    print(arma_a.name)
    print(arma_b.name)

    # select both armatures and go into edit mode...

    if arma_a.type != 'ARMATURE' or arma_b.type != 'ARMATURE':
            raise TypeError("No armature as active object!")

    bpy.ops.object.mode_set(mode='EDIT')

    # calculates the diff between tail & head position in world space, then uses that diff to update ae_bones' tails and rolls in armature space
    for ae_bone in arma_a.data.edit_bones:
        if ae_bone.name in arma_b.data.edit_bones:
            be_bone = arma_b.data.edit_bones [ae_bone.name]
            print(be_bone.tail)
            be_bone_tail_world = arma_b.matrix_world @ be_bone.tail
            be_bone_head_world = arma_b.matrix_world @ be_bone.head
            headToTail_world = be_bone_tail_world - be_bone_head_world
            print(headToTail_world)
            new_ae_bone_tail_loc = arma_b.matrix_world.inverted() @ ((arma_b.matrix_world @ ae_bone.head) + headToTail_world)
            print(new_ae_bone_tail_loc)
            ae_bone.tail, ae_bone.roll = new_ae_bone_tail_loc, be_bone.roll 