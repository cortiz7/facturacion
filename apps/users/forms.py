#encoding:utf-8
from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):

	username = forms.CharField(max_length=50,
					widget=forms.TextInput(attrs={
						'type' : 'text',
						'placeholder' : 'Ingrese un nombre de Usuario',
						}))
	password = forms.CharField(max_length=50,
					widget=forms.TextInput(attrs={
						'type' : 'password',
						'placeholder' : 'Ingrese una Contraseña'
						}))

	def clean(self):
		if not User.objects.filter(username = self.cleaned_data['username']):
			self.add_error('username', 'El nombre de usuario no existe')
		else:
			user = User.objects.get(username = self.cleaned_data['username'])
			if not user.check_password(self.cleaned_data['password']):
				self.add_error('password', 'La contraseña es incorrecta')


class UserCreateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password')
		widgets = {
			'username' : forms.TextInput(attrs={
					'type' : 'text',
					'placeholder' : 'Ingresa nombre de Usuario',
				}),
			'password' : forms.TextInput(attrs={
					'type' : 'password',
					'placeholder' : 'Ingrese una Contraseña',
				})
		} 