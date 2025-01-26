import bpy

class OBJECT_OT_apply_transforms(bpy.types.Operator):
    bl_idname = "object.apply_transforms"
    bl_label = "Aplicar Transformaciones"
    bl_description = "Aplica la posición, rotación y escala al objeto activo"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if obj:
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "No hay un objeto activo")
            return {'CANCELLED'}
