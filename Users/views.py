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

@csrf_exempt
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
	return render_to_response('newUser.html',{'form':form}, context_instance=RequestContext(request))

@csrf_exempt
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
	return render_to_response('newClient.html',{'form':form}, context_instance=RequestContext(request))

@csrf_exempt
def log_in(request):
	if request.method=='POST':
		form=AuthenticationForm(request.POST)
		if form.is_valid:
			response_dict = {}
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
	else:
		form=AuthenticationForm()
	return render_to_response('login.html',{'form':form}, context_instance=RequestContext(request))