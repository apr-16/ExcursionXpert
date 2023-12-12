from wave import WAVE_FORMAT_PCM
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView,View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from TravelApp.models import district,packages,user_reg,confirm,payment,guidedetails

class IndexView(TemplateView):
    template_name = 'user/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        districts = district.objects.all()
        context['dis'] = districts
        return context
    
    def post(self, request):
        dis = request.POST.get('dis')
        pack = packages.objects.filter(dis_id=dis)
        return render(request, 'user/index.html', {'pack': pack})
    
class package_details(TemplateView):
    template_name = 'user/packages_details.html'
    def get_context_data(self, **kwargs):
        context = super(package_details,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        pr = packages.objects.filter(id=id)
        context['pr'] = pr
        return context
    
    def post(self, request, *args, **kwargs):
        idd = self.request.session.get('id')
        user = user_reg.objects.get(user_id=idd)
        persons = int(request.POST['persons'])
        date = request.POST['date']
        location = request.POST['location']
        id = self.request.GET['id']
        pr = packages.objects.get(id=id)
        price = pr.cost
        Total = persons * int(price)
        confirm.objects.filter(status='pending',user_id=user.id).delete()
        
        se = confirm()
        se.user_id = user.id
        se.pack_id = pr.id
        se.persons = persons
        se.date = date
        se.location = location
        se.status = 'pending'
        se.total = Total
        se.save()
        return HttpResponseRedirect("viewconfirm")
    
class viewconfirm(TemplateView):
    template_name = 'user/view_confirm.html'
    
    def get_context_data(self, **kwargs):
        context = super(viewconfirm, self).get_context_data(**kwargs)
        user = user_reg.objects.get(user_id=self.request.user.id)
        ct = confirm.objects.filter(status='pending', user_id=user.id)
        context['ct'] = ct
        return context
    
    def post(self, request, *args, **kwargs):
        user = user_reg.objects.get(user_id=self.request.user.id)
        cr=confirm.objects.get(user_id=user.id, status='pending')
        cr.status = 'sentbyadmin'
        cr.save()
        return HttpResponseRedirect("viewconfirm")
    
class viewbooking(TemplateView):
    template_name = 'user/view_booking.html'
    
    def get_context_data(self, **kwargs):
        context = super(viewbooking, self).get_context_data(**kwargs)
        user = user_reg.objects.get(user_id=self.request.user.id)
        ctc = confirm.objects.exclude(status='pending').filter(user_id=user.id)

        context['ctc'] = ctc
        return context
    
class pay(TemplateView):
    template_name = 'user/payment.html'
    
    def get_context_data(self, **kwargs):
        context = super(pay, self).get_context_data(**kwargs)
        user = user_reg.objects.get(user_id=self.request.user.id)
        ctc = confirm.objects.filter(user_id=user.id)
        context['ctc'] = ctc
        return context
    
    def post(self, request, *args, **kwargs):
        idd = self.request.session.get('id')
        user = user_reg.objects.get(user_id=idd)
        cardname = request.POST['cname']
        cardno = request.POST['cno']
        address = request.POST['add']
        cardyear = request.POST['cyear']
        id = self.request.GET.get('id')
        pr = packages.objects.get(id=id)
        
        se = payment()
        se.user_id = user.id
        se.pack_id = pr.id
        se.cardname = cardname
        se.cardno = cardno
        se.address = address
        se.cardyear = cardyear
        se.status = 'paid'
        se.save()
        
        cr = confirm.objects.get(user_id=user)
        cr.status = 'paid'
        cr.save()
        
        return HttpResponseRedirect("viewbooking")
    
class guidee(TemplateView):
    template_name = 'user/view_guide.html'

    def get_context_data(self, **kwargs):
        context = super(guidee, self).get_context_data(**kwargs)
        district = self.request.GET.get('district')

        if district:
            pr = guidedetails.objects.filter(dis__dis=district)
        else:
            pr = guidedetails.objects.filter(dis__dis=district)

        context['pr'] = pr
        return context
