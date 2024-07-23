from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path("", views.home),
    path('adminCursos/', views.homeCurso),
    path('registrarCurso/', views.registrarCurso),
    path('adminCursos/edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('adminCursos/eliminarCurso/<codigo>', views.eliminarCurso),
    path('adminMatricula/', views.lista_cursos_estudiante, name='lista_cursos_estudiante'),
    path('matricular_curso/<str:codigo_curso>/', views.matricular_curso, name='matricular_curso'),
    path('adminEstudiantes/', views.homeEstudiantes),
    path('registrarEstudiante/', views.registrarEstudiante),
    path('adminEstudiantes/edicionEstudiante/<codigo>', views.edicionEstudiante),
    path('editarEstudiante/', views.editarEstudiante),
    path('adminEstudiantes/eliminarEstudiante/<codigo>', views.eliminarEstudiante), 
    path('verMatriculasEstudiante/', views.ver_matriculas_estudiante, name='ver_matriculas_estudiante'),
    ]
