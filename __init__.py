bl_info = {
    "name": "Herramientas para artistas 3D",
    "description": "Addon con herramientas útiles para artistas 3D",
    "author": "Tu Nombre",
    "version": (1, 0, 0),
    "blender": (4, 3, 2),
    "location": "View3D > Herramientas",
    "category": "Object",
}

import bpy
from bpy.utils import register_class, unregister_class

# Importar operadores
from .origin_operator import OBJECT_OT_origin_to_world
from .align_camera_operator import VIEW3D_OT_align_camera_to_view
from .apply_transforms_operator import OBJECT_OT_apply_transforms
from .shade_operator import OBJECT_OT_shade_flat, OBJECT_OT_shade_smooth

# Panel lateral
class VIEW3D_PT_tools_panel(bpy.types.Panel):
    bl_label = "Herramientas 3D"
    bl_idname = "VIEW3D_PT_tools_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Herramientas"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.origin_to_world", text="Mover Origen al Mundo", icon='OBJECT_ORIGIN')
        layout.operator("view3d.align_camera_to_view", text="Alinear Cámara a Vista", icon='CAMERA_DATA')
        layout.operator("object.apply_transforms", text="Aplicar Transformaciones", icon='FILE_TICK')
        layout.operator("object.shade_flat", text="Sombreado Plano", icon='MOD_WIREFRAME')
        layout.operator("object.shade_smooth", text="Sombreado Suave", icon='SHADING_RENDERED')

# Lista de clases
classes = [
    OBJECT_OT_origin_to_world,
    VIEW3D_OT_align_camera_to_view,
    OBJECT_OT_apply_transforms,
    OBJECT_OT_shade_flat,
    OBJECT_OT_shade_smooth,
    VIEW3D_PT_tools_panel,
]

def register():
    for cls in classes:
        register_class(cls)

def unregister():
    for cls in classes:
        unregister_class(cls)

if __name__ == "__main__":
    register()
