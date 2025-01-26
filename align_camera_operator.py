import bpy

class VIEW3D_OT_align_camera_to_view(bpy.types.Operator):
    bl_idname = "view3d.align_camera_to_view"
    bl_label = "Alinear Cámara a Vista"
    bl_description = "Alinea la cámara activa a la vista actual"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.scene.camera is None:
            self.report({'WARNING'}, "No hay una cámara activa en la escena")
            return {'CANCELLED'}
        bpy.ops.view3d.camera_to_view()
        return {'FINISHED'}
