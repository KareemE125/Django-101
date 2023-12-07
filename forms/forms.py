from django import forms
from .models import User

# Create your forms here.

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)