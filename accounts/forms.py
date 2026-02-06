from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model() # sets 'User' to your 'CustomUser' model automatically

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone_number')
        


class UpdateUserInformation(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'phone_number', 'biography', 'profile_picture')