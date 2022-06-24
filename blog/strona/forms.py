from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','autor', 'title_tag','description','Image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.Select(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'Image': forms.TextInput(attrs={'class':'form-control'}),

        }
