from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Person,Department


# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Person
#         fields = ('name', 'school', 'department')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['department'].queryset = Department.objects.none()

#         if 'school' in self.data:
#             try:
#                 school_id = int(self.data.get('school'))
#                 self.fields['department'].queryset = Department.objects.filter(school_id=school_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty Department queryset
#         elif self.instance.pk:
#             self.fields['department'].queryset = self.instance.school.department_set.order_by('name')
