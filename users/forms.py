from .models import profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterationForm(UserCreationForm):
        first_name = forms.CharField(max_length=150, required=True)
        last_name = forms.CharField(max_length=150, required=True)
        email = forms.EmailField(required=True)
        phone=forms.CharField(max_length=200)
        address=forms.CharField(max_length=300)
        pincode=forms.CharField(max_length=300)
        city=address=forms.CharField(max_length=300)
        state=forms.CharField(max_length=300)
        country=forms.CharField(max_length=300)
        class Meta:
                model = User
                fields=['first_name','last_name','username','email','password1','password2']

        def save(self, commit=True):
                user = super().save(commit=False)
                user.first_name=self.cleaned_data['first_name']
                user.last_name = self.cleaned_data['last_name']
                user.email = self.cleaned_data['email']
                
                if commit:
                    user.save()
                    
                    # Create the related profile with the extra fields
                    profile.objects.create(
                        user=user,
                        phone=self.cleaned_data['phone'],
                        address=self.cleaned_data['address'],
                        pincode=self.cleaned_data['pincode'],
                        city=self.cleaned_data['city'],
                        state=self.cleaned_data['state'],
                        country=self.cleaned_data['country']
                    )
                    
                return user
