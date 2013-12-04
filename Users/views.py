from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from Users.forms import *
from django.utils import simplejson
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
	form=AuthenticationForm(request.POST)
	for field in form.fields:
			form.fields[field].widget.attrs['class'] = 'form-control'
			form.fields[field].widget.attrs['placeholder'] = field
	return render_to_response('index.html', {'form':form}, context_instance=RequestContext(request))

@permission_required('Contabilidad.can_view_report', raise_exception=True)
def reports(request):
	return render_to_response('informes.html', context_instance=RequestContext(request))

@permission_required('Users.can_view_about', raise_exception=True)
def about(request):
	return render_to_response('about.html', context_instance=RequestContext(request))

@permission_required('Contabilidad.can_view_report', raise_exception=True)
def accounting(request):
	return render_to_response('contabilidad.html', context_instance=RequestContext(request))

@permission_required('Contabilidad.can_view_report', raise_exception=True)
def logistics(request):
	return render_to_response('logistica.html', context_instance=RequestContext(request))

@permission_required('Contabilidad.can_view_report', raise_exception=True)
def human_resources(request):
	return render_to_response('recursosHumanos.html', context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Contabilidad.can_add_user', raise_exception=True)
def create_user(request):
	if request.method=='POST':
		form=EmpleadoForm(request.POST)
		response_dict = {}
		if form.is_valid():
			form.save()
			response_dict.update({'mensage': 'Usuario creado'})
			#user=Persona.objects.all().order_by('-id')[0]
			#g = Group.objects.get(name='Clientes')
			#if g is not None:
				#g.user_set.add(user)
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	else:
		form=EmpleadoForm()
	return render_to_response('nuevoUsuario.html',{'form':form}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required('Contabilidad.can_add_user', raise_exception=True)
def create_client(request):
	if request.method=='POST':
		form=ClienteForm(request.POST)
		response_dict = {}
		if form.is_valid():
			form.save()
			response_dict.update({'mensage': 'Cliente creado'})
			#user=Persona.objects.all().order_by('-id')[0]
			#g = Group.objects.get(name='Clientes')
			#if g is not None:
				#g.user_set.add(user)
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	else:
		form=ClienteForm()
	return render_to_response('nuevoCliente.html',{'form':form}, context_instance=RequestContext(request))

@csrf_exempt
def log_in(request):
	response_dict = {}
	if request.method=='POST':
		form=AuthenticationForm(request.POST)
		if form.is_valid:
			user=request.POST['username']
			passw=request.POST['password']
			acces=authenticate(username=user, password=passw)
			if acces is not None:
				if acces.is_active:
					login(request, acces)
					response_dict.update({'mensage': 'Ingreso exitoso'})
					return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
				else:
					response_dict.update({'mensage': 'Usuario inactivo'})
					return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
			else:
				response_dict.update({'mensage': 'El usuario/contrasenia no existe'})
				return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

@login_required(login_url='/')
def log_out(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url='/')
def contact(request):
	return HttpResponse('http//:www.uptc.edu.co')