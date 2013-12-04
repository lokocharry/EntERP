from Contabilidad.models import *
from django.contrib import admin

admin.site.register(Producto)
admin.site.register(Cuenta)
admin.site.register(SubCuenta)
admin.site.register(Liquidacion)
admin.site.register(Producto_Factura)

class Producto_FacturaInline(admin.TabularInline):
	model = Producto_Factura
	extra = 10

class FacturaAdmin(admin.ModelAdmin):
    inlines = (Producto_FacturaInline,)

admin.site.register(Factura, FacturaAdmin)