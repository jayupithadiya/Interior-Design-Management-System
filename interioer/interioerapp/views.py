from django.shortcuts import render, redirect , get_object_or_404
from .models import add_page
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import contact as contacts
from django.contrib.auth.decorators import login_required

def home(request):
    alls = add_page.objects.order_by('-completed_date')[:1]
    return render(request, 'index.html' , {'alls':alls} )

def our_workz(request):
    projects = add_page.objects.all()
    return render(request, 'our_work.html', {'projects': projects})

def contact(request):
    if request.method == "POST":
        obj = contacts()
        obj.name = request.POST.get('name')
        obj.email = request.POST.get('email')
        obj.number = request.POST.get('number')
        obj.project_details = request.POST.get('project_details')
        obj.save()
        return redirect("contact")

    return render(request, 'contact.html')


@login_required
def admins(request):  
    if request.method == "POST":
        obj = add_page()
        obj.title = request.POST.get('title')
        obj.completed_date = request.POST.get('completed_date')
        obj.description = request.POST.get('description')
        obj.image = request.FILES.get('image')
        obj.save()
        return redirect("admins")

    projects = add_page.objects.all()
    inquiries = contacts.objects.all()

    return render(
        request,
        'admin/admin.html',
        {
            'projects': projects,
            'inquiries': inquiries
        }
    )

@login_required
def update_inquiry_status(request,id,status_type):
    inquiry = get_object_or_404(contacts,id=id)
    
    if status_type == 'contacted':
        inquiry.status = 'contacted'
    elif status_type == 'pending':
        inquiry.status = 'pending'
        
    inquiry.save()
    return redirect('admins')

@login_required
def delsd(request,id):
    inquiry = contacts.objects.get(id=id)
    inquiry.delete()
    return redirect("admins")

@login_required
def jasgd(request,id):
    projects = add_page.objects.get(id=id)
    projects.delete()
    return redirect("admins")

def logins(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        
        user = authenticate(request, username=u, password=p)
        
        if user is not None:
            login(request, user)
            return redirect('admins') 
        else:
            messages.error(request, "Username ya Password galat hai!")
            
    return render(request, 'admin/adminlogin.html')

