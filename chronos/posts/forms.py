from django import forms

from chronos.posts.models import PostComment


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('body',)
        widgets = {'body': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Your comment',
                                                 'rows': 2})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = ''
