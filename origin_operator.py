import bpy

class OBJECT_OT_origin_to_world(bpy.types.Operator):
    bl_idname = "object.origin_to_world"
    bl_label = "Mover Origen al Origen del Mundo"
    bl_description = "Mueve el origen del objeto al origen del mundo (0, 0, 0)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if obj:
            obj.location = (0, 0, 0)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "No hay un objeto activo")
            return {'CANCELLED'}
