"""hospitalmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("login/",views.SignInView.as_view(),name="signin"),
    path("appointmentadd/",views.AppointmentCreateView.as_view(),name="appointment"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("password/change/",views.PasswordResetView.as_view(),name="password-reset"),
    path("HospitalManagementSystem/",views.HomeView.as_view(),name="home"),
    path("docdep/",views.DoctorDepartmentCreateView.as_view(),name="doc-dep"),
    path("doclist/",views.DoctorDepartmentListView.as_view(),name="doclist"),
    path("docdetail/<int:pk>/",views.DoctorDepartmentDetailView.as_view(),name="docdetail"),
    path("docedit/<int:pk>/change/",views.DoctorDepartmentEditView.as_view(),name="docedit"),
    path("doctor/<int:pk>/remove/",views.doctor_delete_view,name="docdelete"),
    path("appointmentlist/",views.AppointmentListView.as_view(),name="appointment-list"),
    path("departmentadd/",views.DepartmentCreateView.as_view(),name="department-add"),
    path("departmentlist/",views.DepartmentListView.as_view(),name="department-list"),
    path("departmentedit/<int:pk>/change/",views.DepartmentEditView.as_view(),name="department-edit"),
    path("departmentdelete/<int:pk>/remove/",views.DepartmentDeleteView.as_view(),name="department-delete"),
    path("logout/",views.sign_out_view,name="signout")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
