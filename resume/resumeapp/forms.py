from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': "Name"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': "Email"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'input-field', 'placeholder': "Message"}))

