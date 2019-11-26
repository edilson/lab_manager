from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

        def sanitize_email(self):
            email = self.cleaned_data.get('email')
            already_user = User.objects.filter(email=email).exists()

            if already_user:
                raise forms.ValidationError('Sorry but someone is already using this email')
            return email