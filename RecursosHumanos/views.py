from RecursosHumanos.forms import *
from RecursosHumanos.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from Contabilidad.models import to_json
from Contabilidad.models import ValuesQuerySetToDict
from django.contrib.auth.decorators import permission_required

@csrf_exempt
@permission_required('Logistica.can_add_departamento', login_url='/')
def create_department(request):
	if request.method=='POST':
		form=DepartamentoForm(request.POST)
		response_dict = {}
		if form.is_valid():
			form.save()
			response_dict.update({'mensage': 'Creado exitoso'})
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	else:
		form=DepartamentoForm()
	return render_to_response('departamentos.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Logistica.can_change_departamento', login_url='/')
def modify_department(request):
    if request.method == "POST":
        departamento=get_object_or_404(Departamento, id=request.POST['id'])
        response_dict = {}
        departamento.nombre_departamento=request.POST['nombre_departamento']
        historial.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
@permission_required('Logistica.can_view_departamento', login_url='/')
def get_department(request):
    if request.method=='POST':
    	departamento = get_object_or_404(Departamento, id=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(departamento)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Logistica.can_view_departamento', login_url='/')
def get_all_departments(request):
    if request.method=='POST':
        departamentos=Departamento.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(departamentos)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Logistica.can_add_cargo', login_url='/')
def create_charge(request):
	if request.method=='POST':
		form=CargoForm(request.POST)
		response_dict = {}
		if form.is_valid():
			form.save()
			response_dict.update({'mensage': 'Creado exitoso'})
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	else:
		form=CargoForm()
	return render_to_response('cargos.html', {'form':form}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Logistica.can_change_cargo', login_url='/')
def modify_charge(request):
    if request.method == "POST":
        cargo=get_object_or_404(Cargo, id=request.POST['id'])
        response_dict = {}
        cargo.nombre_cargo=request.POST['nombre_cargo']
        cargo.descripcion_cargo=request.POST['descripcion_cargo']
        cargo.salario_base=request.POST['salario_base']
        cargo.departamento=request.POST['departamento']
        cargo.desempenio=request.POST['desempenio']
        historial.save()
        response_dict.update({'mensage': 'Modificado exitoso'})
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@csrf_exempt
@permission_required('Logistica.can_view_cargo', login_url='/')
def get_charge(request):
    if request.method=='POST':
    	cargo = get_object_or_404(Cargo, id=request.POST['id'])
        return HttpResponse(simplejson.dumps(to_json(cargo)), mimetype='application/javascript')

@csrf_exempt
@permission_required('Logistica.can_view_cargo', login_url='/')
def get_all_charges(request):
    if request.method=='POST':
        cargos=Cargo.objects.all()
        return HttpResponse(simplejson.dumps(ValuesQuerySetToDict(cargos)), mimetype='application/javascript')