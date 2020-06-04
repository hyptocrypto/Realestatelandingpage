from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget  = forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Name'}), required = True)
    email = forms.EmailField(widget = forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Email'}), required = True )
    phone  = forms.IntegerField(widget = forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Phone Number'}), required = False)
    message = forms.CharField(widget = forms.Textarea(attrs={'class': 'input100', 'placeholder': 'Message'}), required = True)