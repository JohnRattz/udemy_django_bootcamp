from django import forms
from .models import Post, Comment

# TODO: Add ['post_detail', 'post_list'] url mappings.
class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author','title','text')
        widgets = {
            # 'textinputclass' and 'postcontent' are our own CSS classes.
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author','text')
        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
