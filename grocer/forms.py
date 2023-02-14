from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    password =  forms.CharField(widget=forms.PasswordInput)
    confirm_password =  forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Post
        fields = ('first_name', 'last_name','contact','email','address','city','state','pincode','username','password',)
