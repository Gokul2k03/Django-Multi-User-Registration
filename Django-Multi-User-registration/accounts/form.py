from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Doctor,Patient

class DoctorSignUpForm(UserCreationForm):
    profile_pic=forms.ImageField(required=False)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_id = forms.CharField(required=True)
    address_line = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    pincode = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.profile_pic=self.cleaned_data.get('profile_pic')
        doctor.email_id=self.cleaned_data.get('email_id')
        doctor.address_line=self.cleaned_data.get('address_line')
        doctor.city=self.cleaned_data.get('city')
        doctor.state=self.cleaned_data.get('state')
        doctor.pincode=self.cleaned_data.get('pincode')
        doctor.save()
        return user

class PatientSignUpForm(UserCreationForm):
    profile_pic=forms.ImageField(required=False)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email_id = forms.CharField(required=True)
    address_line = forms.CharField(required=True)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    pincode = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        patient = Patient.objects.create(user=user)
        patient.profile_pic=self.cleaned_data.get('profile_pic')
        patient.email_id=self.cleaned_data.get('email_id')
        patient.address_line=self.cleaned_data.get('address_line')
        patient.city=self.cleaned_data.get('city')
        patient.state=self.cleaned_data.get('state')
        patient.pincode=self.cleaned_data.get('pincode')
        patient.save()
        return user
