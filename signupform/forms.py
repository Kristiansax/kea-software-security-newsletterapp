from django import forms

# Forms go here
class NewsLetterForm(forms.Form):
    username = forms.CharField(label='Your username', max_length=30)
    first_name = forms.CharField(label='Your first name', max_length=30)
    last_name = forms.CharField(label='Your last name', max_length=30)
    email_address = forms.EmailField()