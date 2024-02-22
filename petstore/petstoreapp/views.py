from django.shortcuts import render ,HttpResponse,redirect,HttpResponseRedirect
from django.views import View
from petstoreapp.models import PetStore
from django.urls import reverse
from django.template import loader

from django.utils.datastructures import MultiValueDictKeyError
def create(request):
       print("Request is :",request.method)
       if request.method=='GET':
            print("IT is in if condition")
            return render(request,'create.html')
       else:
             n=request.POST['uname']
             mail=request.POST['uemail']
             mob=request.POST['phone']
             msg=request.POST['msg']
             m=PetStore.objects.create(Name=n,email=mail,mobile=mob,Msg=msg)
             m.save()
             return redirect('/dashboard')
       
 ###########################################################################
#read
def dashboard(request):
      m=PetStore.objects.all()   
      print(m) 
      context={}
      context['data']=m
      return  render(request,'dashboard.html',context) 

#######################################################################################
# delete 
def delete(request,rid):
      m=PetStore.objects.filter(id=rid)
      print(m)
      m.delete()
      return redirect("/dashboard")

#####################################################################################

#update
'''def edit(request,rid):
      m=PetStore.objects.get(id=rid)
      template=loader.get_template('edit.html')
      context={
            'm':m,
      }
      return HttpResponse(template.render(context,request))'''

      
def update(request, id):
      try:
            first = request.POST['first']
            last = request.POST['last']
            member = PetStore.objects.get(id=id)
            member.firstname = first
            member.lastname = last
            member.save()
      except MultiValueDictKeyError:
            first = False
            last=False
      return HttpResponseRedirect(reverse('/dashboard'))     
      
      
      
      
'''      if request.method=='POST':
             context={}
             context['data']=m
             n=request.POST['upname']
             mail=request.POST['upemail']
             mob=request.POST['uphone']
             msg=request.POST['umsg']
             m=PetStore.objects.filter(id=rid)
             m.update(Name=n,email=mail,mobile=mob,Msg=msg)
            # m.save()
             return redirect('/dashboard')'''
