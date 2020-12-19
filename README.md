## Edgy Bone Tools: Small bone manipulation addon

This addon was written to help me with manipulating bones because I bought a model with the UE4 skeleton, that didn't have the correct bone orientations.
I decided to make it available for whomever this is of use.
It contains functionality to transfer bone orientations from one armature to the next (mapping per name), to add UE4 IK bones from the existing FK bones, to flip and rotate bones and some other niceties.

## How to setup
Just download the latest Release .zip and install it inside Blender

If you want to tweak source, I recommend using VSCode and the Blender Development extension from Jacques Lucke.
Just open up the root folder in VSCode, hit F1 and use the Blender: Build and Run command. Select your blender executable and blender should start with the addon enabled.

## How to use
All operations are found under the Tool tab. Currently there are three panels:

### Per-Bone Panel
This panel is available when you select at least one bone in Edit Mode.
![alt text](https://github.com/herr-edgy/EdgyBoneTools/blob/main/Resources/PerBonePanel.png?raw=true)

### Armature Edit Panel
This panel is available when you select an armature in Object Mode
![alt text](https://github.com/herr-edgy/EdgyBoneTools/blob/main/Resources/ArmatureEditPanel.png?raw=true)

### Armature Transfer Panel
This panel is available when you select two armatures in Object Mode
![alt text](https://github.com/herr-edgy/EdgyBoneTools/blob/main/Resources/ArmatureTransferPanel.png?raw=true)
