from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,ListView,DetailView,UpdateView,CreateView
from myapp.forms import RegistrationForm,LoginForm,PasswordResetForm,AppointmentForm,DoctorDepartmentForm,DoctorDepartmentEditForm,DepartmentForm,DepartmentEditForm
from django.contrib.auth.models import User
from django.contrib import messages
from myapp.models import Doctor,Appointment,Department
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator




def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login to perform this action !!!")
            return redirect("signin")
        return fn(request,*args,**kwargs)
    return wrapper




class SignUpView(CreateView):
    
    model=User
    template_name="register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")

    def form_valid(self, form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)
    


class SignInView(FormView):
    model=User
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("index")
            messages.error(request,"invalid creadential")
        return render(request,self.template_name,{"form":form})


@method_decorator(signin_required,name="dispatch") 
class AppointmentCreateView(CreateView):
    model=User
    template_name="appointment.html"
    form_class=AppointmentForm

    success_url=reverse_lazy("appointment-list")
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"appointment has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create appointment")
        return super().form_invalid(form)


@method_decorator(signin_required,name="dispatch")   
class IndexView(TemplateView):
    template_name="index.html"



class PasswordResetView(FormView):
    model=User
    template_name="password-reset.html"
    form_class=PasswordResetForm

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)

        if form.is_valid():
            username=form.cleaned_data.get("username")
            email=form.cleaned_data.get("email")
            pwd1=form.cleaned_data.get("password1")
            pwd2=form.cleaned_data.get("password2")

            if pwd1==pwd2:
                try:
                    usr=User.objects.get(username=username,email=email)
                    usr.set_password(pwd1)
                    usr.save()
                    messages.success(request,"password has been changed")
                    return redirect("signin")
                except Exception as e:
                    messages.error(request,"invalid credentials")
                    return render(request,self.template_name,{"form":form})
            else:
                messages.error(request,"password mismatch")
                return render(request,self.template_name,{"form":form})


@method_decorator(signin_required,name="dispatch")
class HomeView(TemplateView):
    
    template_name="home.html"

@method_decorator(signin_required,name="dispatch")
class DoctorDepartmentCreateView(CreateView):
    model=Doctor
    template_name="doc-dep.html"
    form_class=DoctorDepartmentForm
    success_url=reverse_lazy("doclist")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"doctor has been created")
        return super().form_valid(form)
    

    
    

@method_decorator(signin_required,name="dispatch")
class DoctorDepartmentListView(ListView):
    model=Doctor
    template_name="doctor-list.html"
    context_object_name="doctors"


@method_decorator(signin_required,name="dispatch")
class DoctorDepartmentDetailView(DetailView):
    model=Doctor
    template_name="doctor-detail.html"
    context_object_name="doctors"


@method_decorator(signin_required,name="dispatch")
class DoctorDepartmentEditView(UpdateView):
    model=Doctor
    form_class=DoctorDepartmentEditForm
    template_name="doc-edit.html"
    success_url=reverse_lazy("doclist")

    def form_valid(self, form):
        messages.success(self.request,"changed")
        return super().form_valid(form)
    


def sign_out_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logged out")
    return redirect("signin")


@signin_required
def doctor_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    obj=Doctor.objects.get(id=id)
    if obj.user == request.user:
        Doctor.objects.get(id=id).delete()
        messages.success(request,"doctor removed")
        return redirect("doclist")
    else:
        messages.error(request,"you donot have the permission to perform this action")
        return redirect("signin")
    

@method_decorator(signin_required,name="dispatch")
class AppointmentListView(ListView):
    model=Appointment
    template_name="appointment-list.html"
    context_object_name="appointments"


@method_decorator(signin_required,name="dispatch")
class DepartmentCreateView(CreateView):
    model=User
    template_name="department.html"
    form_class=DepartmentForm

    success_url=reverse_lazy("department-list")
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"department has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create department")
        return super().form_invalid(form)
    

@method_decorator(signin_required,name="dispatch")
class DepartmentListView(ListView):
    model=Department
    template_name="department-list.html"
    context_object_name="departments"



@method_decorator(signin_required,name="dispatch")
class DepartmentEditView(UpdateView):
    model=Department
    form_class=DepartmentEditForm
    template_name="department-edit.html"
    success_url=reverse_lazy("department-list")

    def form_valid(self, form):
        messages.success(self.request,"changed")
        return super().form_valid(form)



    

@method_decorator(signin_required,name="dispatch")
class DepartmentDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Department.objects.get(id=id).delete()
        return redirect("department-list")