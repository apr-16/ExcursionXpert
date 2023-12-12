from wave import WAVE_FORMAT_PCM
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from TravelApp.models import district,packages,confirm,payment,guidedetails
from django.db.models import Q

class IndexView(TemplateView):
    template_name = 'admin/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        pr = packages.objects.all()
        context['pr'] = pr
        return context
    
class dist(TemplateView):
    template_name = 'admin/district.html'
    def post(self,request):
        distri = request.POST['district']
        se = district()
        se.dis = distri
        se.save()
        return render(request, 'admin/district.html', {'message': "successfully added"})

class place(TemplateView):
    template_name = 'admin/packages.html'
    def get_context_data(self, **kwargs):
        context = super(place,self).get_context_data(**kwargs)
        pr = district.objects.all()
        context['pr'] = pr
        return context
    
    def post(self, request):
        distri = request.POST['district']
        packages_name = request.POST['packname']
        destination = request.POST['destination']
        date = request.POST['date']
        cost = request.POST['cost']
        inclusions = request.POST['inclu']
        attraction = request.POST['attra']
        more_info = request.POST['more']
        cli = request.POST['cli']
        image = request.FILES['img']
        fi = FileSystemStorage()
        files=fi.save(image.name,image)
        image2 = request.FILES['img2']
        fii=FileSystemStorage()
        filess=fii.save(image.name,image2)
        image3 = request.FILES['img3']
        fiii=FileSystemStorage()
        filesss=fiii.save(image.name,image3)
        se = packages()
        se.dis_id = distri
        se.packages_name = packages_name
        se.destination = destination
        se.date = date
        se.cost = cost
        se.inclusions = inclusions
        se.attraction = attraction
        se.more_info = more_info
        se.climate = cli
        se.images1 = files
        se.images2 = filess
        se.images3 = filesss
        se.save()
        return render(request, 'admin/index.html', {'message': "successfully added"})
    
    
class package_details(TemplateView):
    template_name = 'admin/packages_details.html'
    def get_context_data(self, **kwargs):
        context = super(package_details,self).get_context_data(**kwargs)
        pr = confirm.objects.filter(status='sentbyadmin')
        context['pr'] = pr
        return context
    
class pack_approve(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        con = confirm.objects.get(id=id)
        con.status='approved'
        con.save()
        return render(request,'admin/packages_details.html',{'message':" Account Approved"})
    
class pack_reject(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        con = confirm.objects.get(id=id)
        con.status='rejected'
        con.save()
        return render(request,'admin/packages_details.html',{'message':" Account Rejected"})
    
class View_bookings(TemplateView):
    template_name = 'admin/view_booking.html'
    def get_context_data(self, **kwargs):
        context = super(View_bookings,self).get_context_data(**kwargs)
        pr = payment.objects.filter(status='paid')
        context['pr'] = pr
        return context
    
class history(TemplateView):
    template_name = 'admin/history.html'
    def get_context_data(self, **kwargs):
        context = super(history,self).get_context_data(**kwargs)
        id = self.request.GET.get('id')
        pay = payment.objects.filter(id=id)
        context['pr'] = pay
        return context
    
class guidee(TemplateView):
    template_name = 'admin/guide_details.html'
    def get_context_data(self, **kwargs):
        context = super(guidee,self).get_context_data(**kwargs)
        pr = district.objects.all()
        context['pr'] = pr
        return context
    
    def post(self, request):
        distri = request.POST['district']
        guidename = request.POST['guidename']
        contact = request.POST['contact']
        se = guidedetails()
        se.dis_id = distri
        se.guide = guidename
        se.contact = contact
        se.save()
        return render(request, 'admin/index.html', {'message': "successfully added"})
    

class view_pack(TemplateView):
    template_name="admin/view_pack.html"
    
    def get_context_data(self, **kwargs):
        context = super(view_pack,self).get_context_data(**kwargs)
        pr = packages.objects.all()
        context['pr'] = pr
        return context
    
       
class delete_pack(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        packages.objects.get(id=id).delete()
        return HttpResponseRedirect("view_pack",{'message':"Removed"})
    
class pack_update(TemplateView):
    template_name = 'admin/edit_pack.html'
    
    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(pack_update,self).get_context_data(**kwargs)
        pr = packages.objects.filter(id=id)
        context['pr'] = pr
        
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        image = request.FILES['img']
        fi = FileSystemStorage()
        files=fi.save(image.name,image)
        image2 = request.FILES['img2']
        fii=FileSystemStorage()
        filess=fii.save(image.name,image2)
        image3 = request.FILES['img3']
        fiii=FileSystemStorage()
        filesss=fiii.save(image.name,image3)

        usr = packages.objects.get(id=id)
        usr.packages_name = request.POST['packname']
        usr.destination = request.POST['destination']
        usr.date = request.POST['date']
        usr.cost = request.POST['cost']
        usr.inclusions = request.POST['inclu']
        usr.attraction = request.POST['attra']
        usr.more_info = request.POST['more']
        usr.images1 = files
        usr.images2 = filess
        usr.images3 = filesss
        usr.save()
        return HttpResponseRedirect("view_pack",{'message':"Updated"})