from django.contrib.auth.forms import UserChangeForm, UserCreationForm
import django.forms as forms

from authapp.models import ShopUser
from mainapp.models import ProductCategory

class AdminShopUserUpdateForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data