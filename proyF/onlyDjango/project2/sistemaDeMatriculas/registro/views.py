from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Estudiante
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model

CustomUser=get_user_model()

# Create your views here.
def home(request):
    return render(request,"main.html")

@login_required
def admin(request):
    return render(request,"admin_dashboard.html")

@login_required
def homeCurso(request):
    cursosListados = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursosListados})

@login_required
def estudiante_dashboard(request):
    try:
        estudiante = Estudiante.objects.get(user=request.user)
    except Estudiante.DoesNotExist:
        messages.error(request, 'No se encontró el perfil de estudiante asociado con tu cuenta.')
        return redirect('login')  
    cursos_matriculados = estudiante.cursos.all()
    cursos_disponibles = Curso.objects.exclude(codigo__in=estudiante.cursos.values_list('codigo', flat=True))
    
    return render(request, "estudiante_dashboard.html", {
        'cursos_matriculados': cursos_matriculados,
        'cursos_disponibles': cursos_disponibles
    })

@login_required
def matricular_curso_estudiante(request, codigo_curso):
    if request.method == 'POST':
        estudiante = get_object_or_404(Estudiante, user=request.user)
        try:
            curso = Curso.objects.get(codigo=codigo_curso)
        except Curso.DoesNotExist:
            messages.error(request, 'Curso no encontrado.')
            return redirect('estudiante_dashboard')

        if estudiante.cursos.filter(codigo=codigo_curso).exists():
            messages.warning(request, 'Ya estás matriculado en este curso.')
        elif curso.cupos <= 0:
            messages.warning(request, 'No hay cupos disponibles en este curso.')
        elif estudiante.creditos_usados + curso.creditos > estudiante.creditos_maximos:
            messages.warning(request, 'Superas el límite de créditos permitidos.')
        else:
            estudiante.cursos.add(curso)
            estudiante.creditos_usados += curso.creditos
            curso.cupos -= 1
            curso.save()
            estudiante.save()
            messages.success(request, 'Matriculado con éxito.')

        return redirect('estudiante_dashboard')
    
def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']
    cupos=request.POST['numCupos']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, cupos=cupos)
    curso.save()
    return redirect('/adminCursos/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']
    cupos=request.POST['numCupos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.cupos=cupos
    curso.save()

    return redirect('/adminCursos/')

def eliminarCurso(request, codigo):
    curso =Curso.objects.get(codigo=codigo)
    curso.delete()

    return redirect('/adminCursos/')

def lista_cursos_estudiante(request):
    cursos = Curso.objects.all()
    return render(request, "lista_cursos_estudiante.html", {"cursos": cursos})

def matricular_curso(request, codigo_curso):
    if request.method == 'POST':
        try:
            codigo_estudiante = request.POST['codigo_estudiante']
            estudiante = Estudiante.objects.get(codigo=codigo_estudiante)
            curso = Curso.objects.get(codigo=codigo_curso)
        except:
                messages.success(request, 'Código inválido o no registrado.')
                return redirect('/adminMatricula/')
        if estudiante.cursos.filter(codigo=codigo_curso).exists():
            messages.success(request, 'Ya estás matriculado en este curso.')
        elif curso.cupos <= 0:
            messages.success(request, 'No hay cupos disponibles en este curso.')
        elif estudiante.creditos_usados + curso.creditos > estudiante.creditos_maximos:
            messages.success(request, 'Superas el límite de créditos permitidos.')
        else:
            estudiante.cursos.add(curso)
            estudiante.creditos_usados += curso.creditos
            curso.cupos -= 1
            curso.save()
            estudiante.save()
            messages.success(request, 'Matriculado con éxito.')
        
        return redirect('/adminMatricula/')
    
@login_required
def homeEstudiantes(request):
    estudiantesListados = Estudiante.objects.all()
    return render(request, "estudiantes.html", {"estudiantes": estudiantesListados})

def registrarEstudiante(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        creditos = request.POST.get('creditos')

        if CustomUser.objects.filter(username=username).exists():
            messages.success(request, "El nombre de usuario ya está en uso.")
            return redirect('/adminEstudiantes/')
        
        user = CustomUser.objects.create_user(username=username, password=password)
        user.es_estudiante = True
        user.save()  

        estudiante = Estudiante(user=user, codigo=codigo, nombre=nombre, creditos_maximos=creditos)
        estudiante.save() 
        
        messages.success(request, "Estudiante registrado con éxito.")
        return redirect('/adminEstudiantes/')

    return redirect('/adminEstudiantes/')

def edicionEstudiante(request, codigo):
    estudiante = Estudiante.objects.get(codigo=codigo)
    return render(request, "edicionEstudiante.html", {"estudiante": estudiante})

def editarEstudiante(request):
    codigo = request.POST.get('codigo')
    nombre = request.POST.get('nombre')
    creditos = request.POST.get('creditos')

    estudiante = Estudiante.objects.get(codigo=codigo)
    estudiante.nombre = nombre
    estudiante.creditos_maximos=creditos
    estudiante.save()

    return redirect('/adminEstudiantes/')

def eliminarEstudiante(request, codigo):
    estudiante =Estudiante.objects.get(codigo=codigo)
    estudiante.delete()

    return redirect('/adminEstudiantes/')

def ver_matriculas_estudiante(request):
    estudiantes = Estudiante.objects.all()
    if request.method == 'POST':
        codigo_estudiante = request.POST.get('codigo_estudiante')
        estudiante = get_object_or_404(Estudiante, codigo=codigo_estudiante)
        cursos = estudiante.cursos.all()
        return render(request, "ver_matriculas_estudiante.html", {
            'estudiantes': estudiantes,
            'cursos': cursos,
            'selected_estudiante': estudiante
        })
    return render(request, "ver_matriculas_estudiante.html", {'estudiantes': estudiantes})