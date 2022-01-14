from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Gives nested namespace for configurations and keeps configurations in one place
    class Meta:
        # The models that wiill be affected is the User. form.save() will be saved in this user model
        model = User 
        fields = ['username', 'email', 'password1', 'password2'] # Order of the form