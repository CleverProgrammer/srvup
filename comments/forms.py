from django import forms

from .models import Comment

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('text',)

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
