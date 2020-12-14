from django import forms
from blogapp.models import Post, Category


class PostCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'id': 'summernote','style': 'height: auto;'}))

    class Meta:
        model = Post
        fields = ('title', 'category', 'content')