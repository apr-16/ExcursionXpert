from django.shortcuts import render
from django.views.generic import TemplateView
from TravelApp import *
from django.contrib.auth.models import User
from TravelApp.models import UserType, user_reg, district, packages
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect

class indexview(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        districts = district.objects.all()
        context['dis'] = districts
        return context
    
    def post(self, request):
        dis = request.POST.get('dis')
        pack = packages.objects.filter(dis_id=dis)
        return render(request, 'index.html', {'pack': pack})
    
class package_details(TemplateView):
    template_name = 'packages_details.html'
    def get_context_data(self, **kwargs):
        context = super(package_details,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        pr = packages.objects.filter(id=id)
        context['pr'] = pr
        return context

class registration(TemplateView):
    template_name='register.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        username = request.POST['username']
        phone=request.POST['phone']
        address=request.POST['address']
        location=request.POST['location']
        email= request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email,username=email):
            print ('pass')
            return render(request,'register.html',{'message':"already added the username or email"})

        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=name,last_name='1')
            user.save()
            se = user_reg()
            se.user = user
            se.phone = phone
            se.address=address
            se.location=location
            se.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            
            return render(request, 'index.html', {'message': "successfully added"})
        
        
class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:

            login(request,user)
            if user.last_name == '1':
                request.session['id'] = user.id
                request.session.save()
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
            else:
                


                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            
            return render(request,'login.html',{'message':"Invalid Username or Password"})