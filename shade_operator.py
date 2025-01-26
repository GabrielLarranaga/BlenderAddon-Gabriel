import bpy

class OBJECT_OT_shade_flat(bpy.types.Operator):
    bl_idname = "object.shade_flat"
    bl_label = "Sombreado Plano"
    bl_description = "Aplica sombreado plano al objeto seleccionado"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if obj:
            bpy.ops.object.shade_flat()
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "No hay un objeto activo")
            return {'CANCELLED'}

class OBJECT_OT_shade_smooth(bpy.types.Operator):
    bl_idname = "object.shade_smooth"
    bl_label = "Sombreado Suave"
    bl_description = "Aplica sombreado suave al objeto seleccionado"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if obj:
            bpy.ops.object.shade_smooth()
            return {'FINISHED'}
        else:
            self.report({'WARNING'}, "No hay un objeto activo")
            return {'CANCELLED'}
