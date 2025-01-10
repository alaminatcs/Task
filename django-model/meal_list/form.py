from django import forms

class djangoForm(forms.Form):
    name = forms.CharField(label="Full Name : ", error_messages={'required': 'Please enter your name.'}, widget=forms.TextInput(attrs = {'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter your name'}))
    # email = forms.EmailField(label = "User Email")
    gender = [('M', 'Male'), ('F', 'Female')]
    # sex = forms.ChoiceField(choices = gender, widget = forms.RadioSelect)

    # birthday = forms.CharField(required=False, widget = forms.DateInput(attrs = {'type' : 'date'}))
    # appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))

    meals = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    # item = forms.MultipleChoiceField(choices = meals, widget = forms.CheckboxSelectMultiple)

    file = forms.FileField(label = 'Enter a file: ')

    # check = forms.BooleanField(help_text = "Terms and Conditions Accepted")


    # form validations
    # def clean(self):
    #     cleaned_data =  super().clean()
