from django import forms
from .models import URL

class ContactForm(forms.Form):
	full_name = forms.CharField(required = False)
	email = forms.EmailField()
	messsage = forms.CharField()

class URLform(forms.ModelForm):
	class Meta:
		model = URL
		fields = ['myurl', 'price', 'revenue']
		#myurl = forms.URLField(widget=forms.TextInput(attrs={'size': '40'}))

	def clean_myurl(self):
		print (self.cleaned_data)
		myurl = self.cleaned_data['myurl']
		return myurl


# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = SignUp
# 		fields = ['full_name', 'email']

# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		email_base, provider = email.split('@')
# 		domain, extension = provider.split('.')
# 		#if not domain == 'USC':
# 		#	raise forms.ValidationError("Please make sure that you use a USC email")
		
# 		if not extension == "edu":
# 		 	raise forms.ValidationError("Please use a valid .EDU email address")
# 		return email

# 	def clean_full_name(self):
# 		full_name = self.cleaned_data.get('full_name')
# 		return full_name