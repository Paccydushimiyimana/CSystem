# from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import College, School, Department, Level


from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request,user)
            return redirect('index')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request, 'register.html', {'form':form})    
    form = UserCreationForm
    return render(request, 'register.html', {'form':form})

def select(request):
    users=User.objects.all()
    schools=School.objects.all()
    departments=Department.objects.all()
    levels=Level.objects.all()
    return render(request, 'select.html', {'users':users, 'schools':schools, 'departments':departments, 'levels':levels})

def col_schools(request, pk):
    college = get_object_or_404(College, pk=pk)    
    return render(request, 'col_schools.html', {'college':college})

def nu_school(request, pk):
    college = get_object_or_404(College, pk=pk)
    if request.method == 'POST':
        name= request.POST['name']
        user = User.objects.first()

        school = School.objects.create(
            name=name,
            college=college,
        )

        return redirect(col_schools, pk=college.pk)
    return render(request, 'nu_school.html', {'college':college})  

def skl_departs(request, pk, skl_pk):
    school=get_object_or_404(School, college__pk=pk, pk=skl_pk)
    return render(request, 'skl_departs.html', {'school':school})      

def nu_depart(request, pk, skl_pk):
    school=get_object_or_404(School,college__pk=pk, pk=skl_pk)   
    if request.method == 'POST':
        name= request.POST['name']
        user = User.objects.first()

        department = Department.objects.create(
            name=name,
            school=school,
        )

        return redirect(skl_departs, pk=school.college.pk, skl_pk=school.pk )
    return render(request, 'nu_depart.html', {'school':school})   

def depart_levels(request, pk, skl_pk, depart_pk):
    department=get_object_or_404(Department, school__college__pk=pk, school__pk=skl_pk, pk=depart_pk )
    return render(request, 'depart_levels.html', {'department':department})      

def nu_level(request, pk, skl_pk, depart_pk):
    department=get_object_or_404(Department, school__college__pk=pk, school__pk=skl_pk, pk=depart_pk)   
    if request.method == 'POST':
        name= request.POST['name']
        user = User.objects.first()

        level = Level.objects.create(
            name=name,
            department=department,
        )

        return redirect(depart_levels, pk=department.school.college.pk,skl_pk=department.school.pk, depart_pk=department.pk)
    return render(request, 'nu_level.html', {'department':department})   

 