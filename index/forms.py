from .models import Message,Subscribe
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name','subject','email','number','message')

class SubscribeEmail(forms.ModelForm):
	class Meta:
		model = Subscribe
		fields = ('email',)
			