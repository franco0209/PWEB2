from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Estudiante
from django.contrib import messages
from rest_framework import viewsets
from .serializers import CursoSerializer, EstudianteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

# Vistas basadas en funciones
def home(request):
    return render(request, "admin_dashboard.html")

def homeCurso(request):
    cursosListados = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos = request.POST['numCreditos']
        cupos = request.POST['numCupos']

        Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, cupos=cupos)
        return redirect('/adminCursos/')
    return render(request, "registrarCurso.html")

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos = request.POST['numCreditos']
        cupos = request.POST['numCupos']

        curso = Curso.objects.get(codigo=codigo)
        curso.nombre = nombre
        curso.creditos = creditos
        curso.cupos = cupos
        curso.save()

        return redirect('/adminCursos/')
    return redirect('/adminCursos/')  # Cambiar según el diseño de tu formulario

def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
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
            return redirect('/adminMatricula/')
        
        if estudiante.cursos.filter(codigo=codigo_curso).exists():
            messages.error(request, 'Ya estás matriculado en este curso.')
        elif curso.cupos <= 0:
            messages.error(request, 'No hay cupos disponibles en este curso.')
        elif estudiante.creditos_usados + curso.creditos > estudiante.creditos_maximos:
            messages.error(request, 'Superas el límite de créditos permitidos.')
        else:
            estudiante.cursos.add(curso)
            estudiante.creditos_usados += curso.creditos
            curso.cupos -= 1
            curso.save()
            estudiante.save()
            messages.success(request, 'Matriculado con éxito.')
        
        return redirect('/adminMatricula/')
    return redirect('/adminMatricula/')  # Cambiar según el diseño de tu formulario

def homeEstudiantes(request):
    estudiantesListados = Estudiante.objects.all()
    return render(request, "estudiantes.html", {"estudiantes": estudiantesListados})

def registrarEstudiante(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos = request.POST["numCreditos"]

        Estudiante.objects.create(codigo=codigo, nombre=nombre, creditos_maximos=creditos)
        return redirect('/adminEstudiantes/')
    return render(request, "registrarEstudiante.html")

def edicionEstudiante(request, codigo):
    estudiante = Estudiante.objects.get(codigo=codigo)
    return render(request, "edicionEstudiante.html", {"estudiante": estudiante})

def editarEstudiante(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos = request.POST["numCreditos"]

        estudiante = Estudiante.objects.get(codigo=codigo)
        estudiante.nombre = nombre
        estudiante.save()

        return redirect('/adminEstudiantes/')
    return redirect('/adminEstudiantes/')  # Cambiar según el diseño de tu formulario

def eliminarEstudiante(request, codigo):
    estudiante = Estudiante.objects.get(codigo=codigo)
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
