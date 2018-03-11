from django import  forms
from indexapp.models import  Bank, Customer



class bankform(forms.ModelForm):

    class Meta:
        model = Bank
        fields = ('name', 'email' , 'address')

class customerform(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('name', 'bank', 'email')

