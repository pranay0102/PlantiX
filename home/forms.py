
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User 
from blog.models import Profile,Comment
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms

class EditProfileForm(UserChangeForm): 
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_name =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    # is_superuser = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_staff = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_active = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # date_joined = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model =   Profile
        fields = ('username','email','first_name','password','profile_pic')
class CommentForm(forms.ModelForm):
    body = RichTextUploadingField()
    class Meta:
        model = Comment
        fields = ('name','body')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model :Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'profile_image'
        ]