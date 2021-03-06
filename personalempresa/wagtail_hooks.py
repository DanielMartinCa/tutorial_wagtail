from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from personalempresa.models import PersonalEmpresa

class PersonalEmpresaAdmin(ModelAdmin):
    model = PersonalEmpresa
    search_fields = ('nombre', 'apellido', 'departamento')
    menu_icon = 'doc-full-inverse' 
    menu_order = 75
    list_filter= ('genero', 'departamento')
    list_display= ('nombre', 'apellidos','email', 'genero', 'departamento')




class PersonalEmpresaAdminGroup(ModelAdminGroup):
   
    menu_label = 'Personas'
    menu_icon = 'doc-full-inverse'
    menu_order = 75
    items = (PersonalEmpresaAdmin, )



modeladmin_register(PersonalEmpresaAdminGroup)