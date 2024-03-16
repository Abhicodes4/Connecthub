from django import forms
from .models import Post,Profile
class Postform(forms.ModelForm):
    
    class Meta():
        model=Post
        exclude=['us']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'name','id':'ABC',}),
            }
        

class Profileform(forms.ModelForm):
    
    class Meta():
        model=Profile
        exclude=['user']

        widgets={
          
            }       