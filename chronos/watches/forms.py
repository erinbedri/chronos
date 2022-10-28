from django import forms

from chronos.watches.models import Watch, WatchComment


class CreateWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('brand', 'model', 'reference_number', 'year', 'style', 'price_paid', 'condition', 'description', 'image')
        widgets = {'brand': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Brand',
                                                   }),
                   'model': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Model',
                                                   }),
                   'reference_number': forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Reference Number',
                                                              }),
                   'year': forms.NumberInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Year',
                                                    }),
                   'style': forms.Select(attrs={'class': 'form-control',
                                                }),
                   'price_paid': forms.NumberInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Price Paid in EUR',
                                                          }),
                   'condition': forms.Textarea(attrs={'class': 'form-control',
                                                      'rows': 1,
                                                      'placeholder': 'Condition',
                                                      }),
                   'description': forms.Textarea(attrs={'class': 'form-control',
                                                        'rows': 3,
                                                        'placeholder': 'Description',
                                                        }),
                   'image': forms.FileInput(attrs={'class': 'form-control',
                                                   })}


class DeleteWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ()


class EditWatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = ('brand', 'model', 'reference_number', 'year', 'style', 'price_paid', 'condition', 'description', 'image')
        widgets = {'brand': forms.TextInput(attrs={'class': 'form-control',
                                                   }),
                   'model': forms.TextInput(attrs={'class': 'form-control',
                                                   }),
                   'reference_number': forms.TextInput(attrs={'class': 'form-control',
                                                              }),
                   'year': forms.NumberInput(attrs={'class': 'form-control',
                                                    }),
                   'style': forms.Select(attrs={'class': 'form-control',
                                                }),
                   'price_paid': forms.NumberInput(attrs={'class': 'form-control',
                                                          }),
                   'condition': forms.Textarea(attrs={'class': 'form-control',
                                                      'rows': 1,
                                                      }),
                   'description': forms.Textarea(attrs={'class': 'form-control',
                                                        'rows': 3,
                                                        }),
                   'image': forms.FileInput(attrs={'class': 'form-control',
                                                   })}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price_paid'].label = 'Price paid in EUR'


class WatchCommentForm(forms.ModelForm):
    class Meta:
        model = WatchComment
        fields = ('body',)
        widgets = {'body': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Your comment',
                                                 'rows': 2,
                                                 })}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = ''
