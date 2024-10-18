from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_personas')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')


@login_required
def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas/lista_personas.html', {'personas': personas})

def detalle_persona(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    return render(request, 'personas/detalle_persona.html', {'persona': persona})

def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'personas/crear_persona.html', {'form': form})

def editar_persona(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'personas/editar_persona.html', {'form': form})

def eliminar_persona(request, persona_id):
    persona = Persona.objects.get(id=persona_id)
    persona.delete()
    return redirect('lista_personas')

def confirmar_eliminar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)
    if request.method == 'POST':
        persona.delete()
        return redirect('lista_personas')
    return render(request, 'personas/confirmar_eliminar.html', {'persona': persona})






