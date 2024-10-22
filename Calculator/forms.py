from django import forms

class IPForm(forms.Form):
    ip_address = forms.CharField(
        label='IP Address',
        max_length=15,  # Ограничение на длину IP-адреса (например, IPv4)
        widget=forms.TextInput(attrs={'placeholder': 'Enter IP address'})  # Добавим placeholder для красоты
    )
    mask = forms.IntegerField(
        label='Subnet Mask',
        min_value=1,  # Минимальное значение маски (1)
        max_value=32,  # Максимальное значение маски (32)
        widget=forms.NumberInput(attrs={'placeholder': 'Enter subnet mask (1-32)'})
    )
