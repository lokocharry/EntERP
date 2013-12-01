from Logistica.forms import *
from Logistica.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from Contabilidad.models import to_json
from Contabilidad.models import ValuesQuerySetToDict

@csrf_exempt
def create_job_history(request):
	if request.method=='POST':
		form=HistorialTrabajoForm(request.POST)
		response_dict = {}
		if form.is_valid():
			form.save()
			response_dict.update({'mensage': 'Creado exitoso'})
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	else:
		form=HistorialTrabajoForm()
	return render_to_response('historialTrabajo.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
def modify_job_history(request):
    if request.method == "POST":
        historial=get_object_or_404(Historial_Trabajo, id=request.POST['id'])
        response_dict = {}
        hisrorial.fecha_inicio= request.POST['fecha_inicio']
        hisrorial.fecha_fin= request.POST['fecha_fin']
        hisrorial.empleado= request.POST['empleado']
        hisrorial.cargo= request.POST['cargo']
        historial.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
def get_job_history(request):
    if request.method=='POST':
    	historial = get_object_or_404(Historial_Trabajo, id=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(historial)), mimetype='application/javascript')

@csrf_exempt
def get_all_job_historys(request):
    if request.method=='POST':
        historiales=Historial_Trabajo.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(historiales)), mimetype='application/javascript')

@csrf_exempt
def create_pay_discount(request):
	if request.method=='POST':
		form=PagosODescuentosForm(request.POST)
		response_dict = {}
		if form.is_valid():
			form.save()
			response_dict.update({'mensage': 'Creado exitoso'})
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	else:
		form=PagosODescuentosForm()
	return render_to_response('pagoDescuento.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
def modify_pay_discount(request):
    if request.method == "POST":
        pago_descuento=get_object_or_404(Pagos_O_Descuentos, id=request.POST['id'])
        response_dict = {}
        pago_descuento.empleado= request.POST['empleado']
        pago_descuento.descripcion= request.POST['descripcion']
        pago_descuento.valor= request.POST['valor']
        pago_descuento.fecha= request.POST['fecha']
        pago_descuento.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
def get_pay_discount(request):
    if request.method=='POST':
    	pago_descuento = get_object_or_404(Pagos_O_Descuentos, id=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(pago_descuento)), mimetype='application/javascript')

@csrf_exempt
def get_all_pay_discounts(request):
    if request.method=='POST':
        pagos_descuentos=Pagos_O_Descuentos.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(pagos_descuentos)), mimetype='application/javascript')

@csrf_exempt
def get_pays_report(request):
    if request.method=='POST':
        fecha=request.POST['fecha_pago']
        lista=Pagos_O_Descuentos.objects.filter(fecha__year=fecha[:4], fecha__month=fecha[5:7], valor__gte=0)
        return render_to_response('informe.html', {'lista':lista, 'titulo':"Informe de Pagos", 'tipo':"Lista de Pagos"}, context_instance=RequestContext(request))

@csrf_exempt
def get_discounts_report(request):
    if request.method=='POST':
        fecha=request.POST['fecha_descuento']
        lista=Pagos_O_Descuentos.objects.filter(fecha__year=fecha[:4], fecha__month=fecha[5:7], valor__lt=0)
        return render_to_response('informe.html', {'lista':lista, 'titulo':"Informe de Descuentos", 'tipo':"Lista de Descuentos"}, context_instance=RequestContext(request))        

@csrf_exempt
def get_jobs_report(request):
    if request.method=='POST':
        empleado=request.POST['id']
        lista=Historial_Trabajo.objects.filter(empleado__id_empleado=empleado)
        return render_to_response('informe.html', {'lista':lista, 'titulo':"Informe de Trabajoss", 'tipo':"Lista de Trabajos"}, context_instance=RequestContext(request))