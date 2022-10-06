from cProfile import label
from todolist.models import Task
from django import forms


class TaskForm(forms.ModelForm):
    # title = forms.CharField(
    #     required=True
    #     )
    # deskripsi = forms.Textarea(
    #     # required=True,
    #     # widget=forms.widgets.Textarea(
    #     #     attrs={
    #     #         "placeholder": "Masukkan deskripsi",
    #     #     }
    #     # ),
    #     # label="",
    # )
    
    class Meta:
        model = Task
        fields = ('user', 'date', 'title', 'deskripsi')
        exclude = ['user', 'date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Masukkan title',
                'required': 'true'
                }),
            'deskripsi': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Masukkan deskripsi'
                })
        }