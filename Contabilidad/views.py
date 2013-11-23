from Contabilidad.forms import *
from Contabilidad.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_bill(request):
	if request.method=='POST':
		form=FacturaForm(request.POST)
		response_dict = {}
		if form.is_valid():
			form.save()
			response_dict.update({'mensage': 'Creado exitoso'})
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	else:
		form=FacturaForm()
	return render_to_response('bills.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
def modify_bill(request):
    if request.method == "POST":
        factura=get_object_or_404(Factura, id=request.POST['id'])
        response_dict = {}
        factura.cliente= request.POST['cliente']
        factura.fecha_factura= request.POST['fecha_factura']
        factura.tipo_factura= request.POST['tipo_factura']
        factura.empleado= request.POST['empleado']
        factura.cuenta= request.POST['cuenta']
        factura.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
def get_bill(request):
    if request.method=='POST':
        if(request.POST['tipo']=='compra'):
            factura = get_object_or_404(Factura, id=request.POST['id'])
        if(request.POST['tipo']=='venta'):
            factura = get_object_or_404(Factura, numero_factura=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(factura)), mimetype='application/javascript')

@csrf_exempt
def get_all_bills(request):
    if request.method=='POST':
        facturas=Factura.objects.filter(tipo_factura="V")
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(facturas)), mimetype='application/javascript')

@csrf_exempt
def create_sale_order(request):
    if request.method=='POST':
        form=ProductoFacturaForm(request.POST)
        response_dict = {}
        if form.is_valid():
            form.save()
            response_dict.update({'mensage': 'Creado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    else:
        form=ProductoFacturaForm()
        facturas=Factura.objects.filter(tipo_factura='V').values('id')
    return render_to_response('orders.html', {'form':form, 'facturas':facturas}, context_instance=RequestContext(request))

def modify_sale_order(request):
    if request.method == "POST":
        pedido=get_object_or_404(Producto_Factura, id=request.POST['id'])
        response_dict = {}
        pedido.cantidad= request.POST['cantidad']
        pedido.producto= Producto.objects.get(id=request.POST['producto'])
        pedido.factura= Factura.objects.get(id=request.POST['factura'])
        pedido.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
def get_sale_order(request):
    if request.method=='POST':
        pedido = get_object_or_404(Producto_Factura, id=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(pedido)), mimetype='application/javascript')

@csrf_exempt
def get_all_orders(request):
    if request.method=='POST':
        ordenes=Producto_Factura.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(ordenes)), mimetype='application/javascript')

@csrf_exempt
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
    return render_to_response('products.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
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
def get_product(request):
    if request.method=='POST':
        producto = get_object_or_404(Producto, id=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(producto)), mimetype='application/javascript')

@csrf_exempt
def delete_product(request):
    if request.method=='POST':
        producto = get_object_or_404(Producto, id=request.POST['id']).delete()
        response_dict = {}
        response_dict.update({'mensage': 'Eliminado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
def get_all_products(request):
    if request.method=='POST':
        productos=Producto.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(productos)), mimetype='application/javascript')

@csrf_exempt
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
    return render_to_response('accounts.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
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
def get_account(request):
    if request.method=='POST':
        cuenta = get_object_or_404(Cuenta, numero_cuenta=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(cuenta)), mimetype='application/javascript')

@csrf_exempt
def get_all_accounts(request):
    if request.method=='POST':
        cuentas=Cuenta.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(cuentas)), mimetype='application/javascript')

@csrf_exempt
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
    return render_to_response('subaccounts.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
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
def get_subaccount(request):
    if request.method=='POST':
        subcuenta = get_object_or_404(SubCuenta, numero_subcuenta=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(subcuenta)), mimetype='application/javascript')

@csrf_exempt
def get_all_subaccounts(request):
    if request.method=='POST':
        subcuentas=SubCuenta.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(subcuentas)), mimetype='application/javascript')

@csrf_exempt
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
    return render_to_response('liquidation.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
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
def get_liquidation(request):
    if request.method=='POST':
        liquidacion = get_object_or_404(Liquidacion, id=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(liquidacion)), mimetype='application/javascript')

@csrf_exempt
def get_all_liquidations(request):
    if request.method=='POST':
        subcuentas=SubCuenta.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(subcuentas)), mimetype='application/javascript')
