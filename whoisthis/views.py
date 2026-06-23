from django.shortcuts import render, redirect
from whoisthis.forms import RegisterForm
from django.contrib.auth.models import User
from django.views import View


class RegisterView(View):
    def get(self, request):
        form=RegisterForm
        return render(request, 'register.html', { 'form':form })

    def post(self, request): 
        form_data=RegisterForm(request.POST)
        if form_data.is_valid():
            f_name=form_data.cleaned_data['first_name']
            l_name=form_data.cleaned_data['last_name']
            name=form_data.cleaned_data['username']
            email=form_data.cleaned_data['email']
            pass1=form_data.cleaned_data['password']
            pass2=form_data.cleaned_data['rep_password']

            if pass1==pass2:
                if User.objects.filter(username=name).exists():
                    return render(request, 'register.html', { 'user_err':'user already exists' })
                else:
                    User.objects.create_user(username=name, first_name=f_name, last_name=l_name, email=email,password=pass1)
                    return redirect('register')
                
            else:
                return render(request, 'register.html', { 'pass_err':'enter same password in both the fields' })
        else:
            return render(request, 'register.html', { 'invalid':'invalid inputs provided' })
        
