from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm,ChangeUserForm
from car.models import Car
from .import models
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.utils.decorators import method_decorator
from django.views.generic import ListView
# Create your views here.



def signup(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created successfully')
            return redirect('signup')
    else:
        register_form = RegistrationForm()
    return render(request,'signup.html',{'form' : register_form ,'type' : 'SignUp'})

        
class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
@method_decorator(login_required, name='dispatch')
class ProfileView(ListView):
    model = models.OrderCarUser
    template_name = 'profile.html'
    context_object_name = 'dt'

    def get_queryset(self):
        return models.OrderCarUser.objects.filter(user=self.request.user)
    

@login_required
def user_logout(request):
    messages.success(request,'Logout successfully ')
    logout(request)
    return redirect('user_login')



@login_required
def pass_change(request):

    if request.method == 'POST':
        change_pass = PasswordChangeForm(user=request.user,data = request.POST)
        if change_pass.is_valid():
            change_pass.save()
            messages.success(request,'Password Updated successfully')
            update_session_auth_hash(request,change_pass.user)
            return redirect('profile')
    else:
        change_pass = PasswordChangeForm(user=request.user)
    return render(request,'passchange1.html',{'form' : change_pass})

@login_required
def pass_change2(request):

    if request.method == 'POST':
        change_pass = SetPasswordForm(user=request.user,data = request.POST)
        if change_pass.is_valid():
            change_pass.save()
            messages.success(request,'Password Updated successfully')
            update_session_auth_hash(request,change_pass.user)
            return redirect('profile')
    else:
        change_pass = SetPasswordForm(user=request.user)
    return render(request,'passchange1.html',{'form' : change_pass})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_form = ChangeUserForm(request.POST,instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile')
    else:
        edit_form=ChangeUserForm(instance = request.user)
    return render(request,'updateProfile.html',{'form': edit_form})


def CarBuyUser(request,id):
    car = Car.objects.get(pk=id)
    print(car.price)
    if car.quantity > 0:
        models.OrderCarUser.objects.create(user=request.user,car = car)
        car.quantity = car.quantity -  1
        car.save()
    return redirect('car_details',id = car.id)

