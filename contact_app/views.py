from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import NewUserForm, AddContactForm
from .models import Contact

def sign_up(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = NewUserForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        pw = request.POST.get('password')

        user = authenticate(request, username=u, password=pw)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Credentials incorrect")
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')

def add_contact(request):
    if request.method == 'POST':
        form = AddContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_contact')
    else:
        form = AddContactForm()

    return render(request, "addcontact.html", {"form": form})

def viewcontacts(request):
    contacts = Contact.objects.all()
    return render(request, 'viewcontact.html', {'contacts': contacts})

def delete_contact(request, cid):
    data = Contact.objects.get(cid=cid)
    data.delete()

    contacts = Contact.objects.all()
    return render(request, 'viewcontact.html', {"contacts": contacts})

def edit_contact(request, cid):
    data = Contact.objects.get(cid=cid)
    return render(request, 'editcontact.html', {"data": data})

def update_contact(request, cid):
    data = Contact.objects.get(cid=cid)
    form = AddContactForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        form.save()
        return redirect('viewcontact')
    else:
        return render(request, 'editcontact.html', {'data': data})  
