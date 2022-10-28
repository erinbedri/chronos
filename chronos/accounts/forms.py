from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(required=True,
                                 max_length=30,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(required=True,
                                max_length=30,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email Address',
                                                           'class': 'form-control',
                                                           }))
    username = forms.CharField(required=True,
                               max_length=30,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password1 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        return self.cleaned_data


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 }))
    remember_me = forms.BooleanField(required=False)


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(required=True,
                                 max_length=30,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               }))
    last_name = forms.CharField(required=True,
                                max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           }))
    username = forms.CharField(required=True,
                               max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class DeleteUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ()