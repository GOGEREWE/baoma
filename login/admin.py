from django import forms
from .models import users
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='PasswordConformation',
                                widget=forms.PasswordInput)
    
    class Meta:
        model = users
        fields = ['email','username']
    
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError("password don't match")
        return password2
    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = users
        fields = ["email","password","username","is_active","is_admin"]

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["email","username","is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None,{"fields":['email','password']}),
        ("Personal",{'fields':['username']}),
        ("Permissions",{'fields':['is_admin']}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes":['wide'],
                "fields":['email','date_of_birth','password',]
            }
        )
    ]
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []


admin.site.register(users, UserAdmin)
admin.site.unregister(Group)