from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class TipocontratoResource(resources.ModelResource):
    class Meta:
        model = Tipocontrato

class TipocontratoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['tituloContrato']
    list_display = ('tituloContrato', 'textoinicialContrato', 'descripcionContrato','marcatipoContrato')
    resource_class = TipocontratoResource

admin.site.register(Tipocontrato, TipocontratoAdmin)


   

class SecuenciaResource(resources.ModelResource):
    class Meta:
        model = Secuencia

class SecuenciaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['textoSecuencia']
    list_display = ('tipocontrato', 'nivel1', 'nivel2', 'nivel3','nivel4', 'identificador','textoSecuencia')
    resource_class = SecuenciaResource

admin.site.register(Secuencia, SecuenciaAdmin)

class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = Departamento
        import_id_fields = ('claveDepartamento',)

class DepartamentoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['claveDepartamento']
    list_display = ('claveDepartamento', 'nombreDepartamento')
    resource_class = DepartamentoResource

admin.site.register(Departamento, DepartamentoAdmin)

class PartesResource(resources.ModelResource):
    class Meta:
        model = Partes
      
class PartesAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombreParte' ]
    list_display = ('nombreParte','claveDepartamento','nombresParte', 'apellidoPaternoParte', 'apellidoMaternoParte' )
    resource_class = PartesResource

admin.site.register(Partes, PartesAdmin)

class PuestosResource(resources.ModelResource):
    class Meta:
        model = Puestos

class PuestosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombrePuesto']
    list_display = ('nombrePuesto', 'claveCampus')
    resource_class = PuestosResource

admin.site.register(Puestos, PuestosAdmin)

class ValidaResource(resources.ModelResource):
    class Meta:
        model = Valida

class ValidaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['tipocontrato']
    list_display = ('tipocontrato', 'nombreCampo', 'nombreVariable')
    resource_class = ValidaResource

admin.site.register(Valida, ValidaAdmin)

class EstadosResource(resources.ModelResource):
    class Meta:
        model = Estados

class EstadosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombreEstado']
    list_display = ('nombreEstado', 'claveEstado')
    resource_class = EstadosResource

admin.site.register(Estados, EstadosAdmin)

class RequisitosResource(resources.ModelResource):
    class Meta:
        model = Requisitos

class RequisitosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['requisito']
    list_display = ('tipocontrato', 'requisito')
    resource_class = RequisitosResource

admin.site.register(Requisitos, RequisitosAdmin)



class AreaResource(resources.ModelResource):
    class Meta:
        model = Area

class AreaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombreArea']
    list_display = ('nombreArea', 'idArea')
    resource_class = AreaResource

admin.site.register(Area, AreaAdmin)





admin.site.register(Campus)
admin.site.register(Ciclos)

admin.site.register(Contratos)

admin.site.register(Niveles)
admin.site.register(Profesiones)
admin.site.register(Regimen)
