from django.contrib import admin
from .models import College,School,Department,Level,Category,Student_category,Lecturer_category
from .models import College_council,School_council,Department_council,Academic_council,Profile

admin.site.register(Profile)
admin.site.register(College)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Category)
admin.site.register(Student_category)  
admin.site.register(College_council)
admin.site.register(School_council)
admin.site.register(Department_council)  
admin.site.register(Academic_council)
admin.site.register(Lecturer_category)