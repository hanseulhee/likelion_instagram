from django import forms
from .models import Post, CustomUser, Comment, Hashtag
#from django.contrib.auth.models import User
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['place', 'content', 'image', 'hashtag_field']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'nickname', 'phone_number','profile_image']        
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image' : forms.FileInput(attrs={'class': 'form-control-file'})
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']