from django import forms
from django.core.exceptions import  ValidationError


# def checkEmail(value):
#
#     if value.find('mytectra.com') == -1:
#         raise ValidationError("Please pass valid Email of myTectra")
#
# def checkName(value):
#
#     if value.isdigit():
#         raise ValidationError("Required parameter is string only!!!")




class coreForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()

class formExample(forms.Form):

    ch = (
        ('', 'Select options--'),
        ('pn', 'Pune'),
        ('bng' ,'Bangalore'),
        ('dl' , 'Delhi'),
        ('mum' , 'Mumbai')

    )
    gn = (
        ('m', 'Male'),
        ('f' , 'Female'),
        ('t', 'Trans')

    )

    name = forms.CharField(label='waquar',min_length=5, max_length= 20, initial='Mr.', disabled=False)
    email = forms.EmailField()
    address = forms.CharField(max_length=250, widget=forms.Textarea)
    city = forms.ChoiceField(choices=ch, required= False)
    gender = forms.ChoiceField(choices = gn , widget= forms.RadioSelect())
    active = forms.CharField(widget=forms.CheckboxInput())


    def clean(self):

        form_data = self.cleaned_data

        if 'email' in form_data and form_data ['email'].find('mytectra.com') == -1:
            self.errors['email'] = ['Please pass valid Email of myTectra']

        if 'name' in form_data and form_data ['name'].isdigit():
            self.errors['name'] = ['Provide name in strings only']


        return  form_data



