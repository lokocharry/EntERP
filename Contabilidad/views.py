from Contabilidad.forms import *
from Contabilidad.models import *
from Logistica.models import Pagos_O_Descuentos
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth.decorators import permission_required

@csrf_exempt
@permission_required('Contabilidad.can_add_factura', login_url='/')
def create_bill(request):
    if request.method=='POST':
        form=FacturaForm(request.POST)
        fset=FacturaFormSet(instance=Factura)
        response_dict={}
        if form.is_valid():
            factura=form.save()
            fset=FacturaFormSet(request.POST, request.FILES, instance=factura)
            if fset.is_valid():
                fset.save()
                response_dict.update({'mensage':'Creado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    else:
        form=FacturaForm()
        fset=FacturaFormSet()
        return render_to_response('facturas.html', {'form':form, 'fieldset':fset}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Contabilidad.can_change_factura', login_url='/')
def modify_bill(request):
    if request.method == "POST":
        factura=get_object_or_404(Factura, id=request.POST['id'])
        response_dict = {}
        factura.cliente= request.POST['cliente']
        factura.fecha_factura= request.POST['fecha_factura']
        factura.tipo_factura= request.POST['tipo_factura']
        factura.empleado= request.POST['empleado']
        factura.prodcstos=request.POST['productos']
        factura.cuenta= request.POST['cuenta']
        factura.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_factura', login_url='/')
def get_bill(request):
    if request.method=='POST':
        if(request.POST['tipo']=='compra'):
            factura = get_object_or_404(Factura, id=request.POST['id'])
        if(request.POST['tipo']=='venta'):
            factura = get_object_or_404(Factura, numero_factura=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(factura)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_factura', login_url='/')
def get_all_bills(request):
    if request.method=='POST':
        facturas=Factura.objects.filter(tipo_factura="V")
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(facturas)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_add_producto', login_url='/')
def create_product(request):
    if request.method=='POST':
        form=ProductoForm(request.POST)
        response_dict = {}
        if form.is_valid():
            form.save()
            response_dict.update({'mensage': 'Creado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    else:
        form=ProductoForm()
    return render_to_response('productos.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Contabilidad.can_change_producto', login_url='/')
def modify_product(request):
    if request.method == "POST":
        producto=get_object_or_404(Producto, id=request.POST['id'])
        response_dict = {}
        producto.nombre_producto=request.POST['nombre_producto']
        producto.descripcion_producto=request.POST['descripcion_producto']
        producto.cantidad_minima=request.POST['cantidad_minima']
        producto.precio_minimo=request.POST['precio_minimo']
        producto.precio_maximo=request.POST['precio_maximo']
        producto.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_producto', login_url='/')
def get_product(request):
    if request.method=='POST':
        producto = get_object_or_404(Producto, id=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(producto)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_delete_producto', login_url='/')
def delete_product(request):
    if request.method=='POST':
        producto = get_object_or_404(Producto, id=request.POST['id']).delete()
        response_dict = {}
        response_dict.update({'mensage': 'Eliminado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_producto', login_url='/')
def get_all_products(request):
    if request.method=='POST':
        productos=Producto.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(productos)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_add_cuenta', login_url='/')
def create_account(request):
    if request.method=='POST':
        form=CuentaForm(request.POST)
        response_dict = {}
        if form.is_valid():
            form.save()
            response_dict.update({'mensage': 'Creado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    else:
        form=CuentaForm()
    return render_to_response('cuentas.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Contabilidad.can_change_cuenta', login_url='/')
def modify_account(request):
    if request.method == "POST":
        cuenta=get_object_or_404(Cuenta, id=request.POST['id'])
        response_dict = {}
        cuenta.numero_cuenta=request.POST['numero_cuenta']
        cuenta.descripcion_cuenta=request.POST['descripcion_cuenta']
        cuenta.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_cuenta', login_url='/')
def get_account(request):
    if request.method=='POST':
        cuenta = get_object_or_404(Cuenta, numero_cuenta=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(cuenta)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_cuenta', login_url='/')
def get_all_accounts(request):
    if request.method=='POST':
        cuentas=Cuenta.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(cuentas)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_add_subcuenta', login_url='/')
def create_subaccount(request):
    if request.method=='POST':
        form=SubCuentaForm(request.POST)
        response_dict = {}
        if form.is_valid():
            form.save()
            response_dict.update({'mensage': 'Creado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    else:
        form=SubCuentaForm()
    return render_to_response('subCuentas.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Contabilidad.can_change_subcuenta', login_url='/')
def modify_subaccount(request):
    if request.method == "POST":
        subcuenta=get_object_or_404(SubCuenta, id=request.POST['id'])
        response_dict = {}
        subcuenta.numero_cuenta=request.POST['numero_cuenta']
        subcuenta.descripcion_subcuenta=request.POST['descripcion_subcuenta']
        subcuenta.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_subcuenta', login_url='/')
def get_subaccount(request):
    if request.method=='POST':
        subcuenta = get_object_or_404(SubCuenta, numero_subcuenta=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(subcuenta)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_subcuenta', login_url='/')
def get_all_subaccounts(request):
    if request.method=='POST':
        subcuentas=SubCuenta.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(subcuentas)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_add_liquidacion', login_url='/')
def create_liquidation(request):
    if request.method=='POST':
        form=LiquidacionForm(request.POST)
        response_dict = {}
        if form.is_valid():
            form.save()
            liquidacion=Liquidacion.objects.filter(empleado=request.POST['empleado']).order_by('-id')[0]
            liquidacion.valor=liquidacion._get_pago()
            liquidacion.save()
            response_dict.update({'mensage': 'Creado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    else:
        form=LiquidacionForm()
    return render_to_response('liquidacion.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Contabilidad.can_change_liquidacion', login_url='/')
def modify_liquidation(request):
    if request.method == "POST":
        liquidacion=get_object_or_404(Liquidacion, id=request.POST['id'])
        response_dict = {}
        liquidacion.empleado=Liquidacion.objects.get(id=request.POST['empleado'])
        liquidacion.fecha_factura=request.POST['fecha_factura']
        subcuenta.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_liquidacion', login_url='/')
def get_liquidation(request):
    if request.method=='POST':
        liquidacion = get_object_or_404(Liquidacion, id=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(liquidacion)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_liquidacion', login_url='/')
def get_all_liquidations(request):
    if request.method=='POST':
        subcuentas=SubCuenta.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(subcuentas)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Contabilidad.can_view_reports', login_url='/')
def get_bills_report(request):
    if request.method=='POST':
        fecha=request.POST['fecha']
        lista=Factura.objects.filter(Q(tipo_factura="V") | Q(tipo_factura="C"), fecha_factura__year=fecha[:4], fecha_factura__month=fecha[5:7])
        return render_to_response('informeFacturas.html', {'lista':lista, 'titulo':"Informe de Facturas", 'tipo':"Lista de Facturas"}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Contabilidad.can_view_reports', login_url='/')
def get_products_report(request):
    if request.method=='POST':
        fecha=request.POST['fecha_venta']
        lista=Producto_Factura.objects.filter(factura__tipo_factura="V", factura__fecha_factura__year=fecha[:4], factura__fecha_factura__month=fecha[5:7]).values('producto').annotate(venta=models.Sum('cantidad'))
        return render_to_response('productosVendidos.html', {'lista':lista, 'titulo':"Informe de Productos", 'tipo':"Lista de Productos (Compras)"}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Contabilidad.can_view_reports', login_url='/')
def get_products2_report(request):
    if request.method=='POST':
        fecha=request.POST['fecha_compra']
        lista=Producto_Factura.objects.filter(factura__tipo_factura="C", factura__fecha_factura__year=fecha[:4], factura__fecha_factura__month=fecha[5:7]).values('producto').annotate(venta=models.Sum('cantidad'))
        return render_to_response('productosComprados.html', {'lista':lista, 'titulo':"Informe de Productos", 'tipo':"Lista de Productos (Ventas)"}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Contabilidad.can_view_reports', login_url='/')
def get_payroll_report(request):
    if request.method=='POST':
        fecha=request.POST['fecha_nomina']
        lista=Factura.objects.filter(tipo_factura="C", fecha_factura__year=fecha[:4], fecha_factura__month=fecha[5:7])
        lista1=Factura.objects.filter(tipo_factura="V", fecha_factura__year=fecha[:4], fecha_factura__month=fecha[5:7])
        lista2=Liquidacion.objects.filter(fecha_liquidacion__year=fecha[:4], fecha_liquidacion__month=fecha[5:7])
        lista3=Pagos_O_Descuentos.objects.filter(fecha__year=fecha[:4], fecha__month=fecha[5:7])
        return render_to_response('informeNomina.html', {'lista':lista, 'titulo':"Informe de Nomina", 'tipo':"Nomina", 'lista1':lista1, 'lista2':lista2, 'lista3':lista3}, context_instance=RequestContext(request))
