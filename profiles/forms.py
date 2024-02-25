# profiles/forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field 
from .models import Profile 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('bio', rows="3"),  # Example - adjust styling for bio
            'location',
            'birth_date',
            Submit('submit', 'Save', css_class='btn btn-primary'),  # Bootstrap styling
        )
