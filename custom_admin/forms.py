from django import forms
from .models import Package, ShipmentHistory


class PackageCreateForm(forms.ModelForm):
    class Meta:
        model = Package
        exclude = ['tracking_id', 'freight_cost']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'carrier': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'max-height: 50px;'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'origin': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'length': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'width': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'height': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'shipment_medium': forms.Select(attrs={'class': 'form-control'}),
            'pickup_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'pickup_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
        }


class ShipmentHistoryCreateForm(forms.ModelForm):
    class Meta:
        model = ShipmentHistory
        exclude = ['package']

        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'remarks': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
        }
