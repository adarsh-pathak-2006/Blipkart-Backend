from django.shortcuts import render, redirect
from auth.forms import RegisterForm
from django.contrib.auth.models import User
from django.views import View


class RegisterView(View):
    def get(self, request):
        form=RegisterForm
        return render(request, 'register.html', { 'form':form })

    def post(self, request): 
        form_data=RegisterForm(request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data['username']
            pass1=form_data.cleaned_data['password']
            pass2=form_data.cleaned_data['rep_password']

            if pass1==pass2:
                if User.objects.filter(username=name).exists():
                    return render(request, 'register.html', { 'user_err':'user already exists' })
                else:
                    User.objects.create_user(username=name, password=pass1)
                    return redirect('register')
                
            else:
                return render(request, 'register.html', { 'pass_err':'enter same password in both the fields' })
        else:
            return render(request, 'register.html', { 'invalid':'invalid inputs provided' })