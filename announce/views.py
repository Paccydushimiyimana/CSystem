from django.shortcuts import render, redirect, get_object_or_404
from .models import Announcement


# def announces(request):
#     announces = get_object_or_404(Announcement)   
#     return render(request, 'announcements.html', {'announces':announces})

# def nu_announce(request, pk):
#     college = get_object_or_404(College, pk=pk)
#     if request.method == 'POST':
#         name= request.POST['name']
#         user = User.objects.first()

#         school = School.objects.create(
#             name=name,
#             college=college,
#         )

#         return redirect(col_schools, pk=college.pk)
#     return render(request, 'nu_school.html', {'college':college}) 