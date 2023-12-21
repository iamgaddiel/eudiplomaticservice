from typing import Any
from uuid import uuid4
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, resolve_url, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from random import  randrange
from .models import Package, ShipmentHistory
from .forms import PackageCreateForm, ShipmentHistoryCreateForm




def generate_random_string(n: int) -> str:
    string = ""
    for _ in range(n):
        string += str(randrange(10))
    return string


def logout_view(request):
    logout(request)
    return redirect('custom_admin:login')



class DashboardView(LoginRequiredMixin, ListView):
    model = Package
    template_name = 'custom_admin/dashboard.html'
    context_object_name = 'packages'


class CreateShipmentHistory(CreateView):
    model = ShipmentHistory
    template_name =  'custom_admin/package_create.html'
    form_class = ShipmentHistoryCreateForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['context'] = 'Tacking History'
        context['package_id'] = self.kwargs.get('package_id')
        return context
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        package_id = self.request.session['PACKAGE_ID']
        form.instance.package = Package.objects.get(pk=package_id)
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        package_id = self.request.session['PACKAGE_ID']
        return resolve_url('custom_admin:history_list', pk=package_id)


class ListHistory(ListView):
    template_name = 'custom_admin/history_list.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.request.session['PACKAGE_ID'] = str(self.kwargs.get('pk'))
        return super().get(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet[Any]:
        return ShipmentHistory.objects.filter(package=self.kwargs.get('pk')).order_by('-date')


class ListPackages(ListView):
    model = Package
    template_name = 'custom_admin/package_list.html'


class PackageDetail(DetailView):
    model = Package
    template_name = 'custom_admin/package_detail.html'


class CreatePackage(CreateView):
    model = Package
    form_class = PackageCreateForm
    success_url = reverse_lazy('custom_admin:package_list')
    template_name = 'custom_admin/package_create.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['context'] = 'Package'
        return context

    def form_valid(self, form):
        height: float = form.instance.height
        length: float = form.instance.length
        weight: float = form.instance.weight
        width: float = form.instance.width
        item_quantity = form.instance.quantity
        shipment_medium = form.instance.shipment_medium
        origin = form.instance.origin

        # Fright density calculations
        cubic_inches: float = height * width * length
        cubic_feet = cubic_inches // 1728
        freight_density = (weight * item_quantity) // cubic_feet

        # Fee Calculations
        road_fee = 1765
        shipping_fee = 2992
        flight_fee = 3907

        freight_cost: int | float = 0
        print(shipment_medium, '<0------')
        if shipment_medium == 'Road':
            freight_cost = freight_density * road_fee

        if shipment_medium == 'Ship':
            freight_cost = freight_density * shipping_fee

        if shipment_medium == 'Flight':
            freight_cost = freight_density * flight_fee

        # Generate tracing Id
        # generated_id = generate_random_string(10)
        generated_id = uuid4()
        tracking_id = 'EDU-{generated_id}'.format(generated_id=generated_id)
        form.instance.tracking_id = tracking_id
        form.instance.freight_cost = freight_cost

        form_instance = form.save()
        
        # Crate Initial Shipment History
        ShipmentHistory.objects.create(
            package = form_instance,
            location = origin,
            date = form.instance.pickup_date,
            time = form.instance.pickup_time
        ).save()
        return super().form_valid(form)
