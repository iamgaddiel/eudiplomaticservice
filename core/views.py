from django.shortcuts import render,redirect
from django.views.generic import TemplateView, DetailView

from custom_admin.models import Package, ShipmentHistory



class Root(TemplateView):
    template_name = 'core/index.html'


class About(TemplateView):
    template_name = 'core/about.html'


class ContactUs(TemplateView):
    template_name = 'core/contact.html'


class PackageTrackingDetails(TemplateView):
    # template_name = 
    pass


def track_page(request):
    context: dict[str, str] = {}
    template_name = 'core/tracking_detail.html'

    if request.method == 'POST':
        carrier = request.POST.get('carrier')
        tracking_id = request.POST.get('tracking_id')
        shipment_medium = request.POST.get('shipment_medium')

        print(carrier, tracking_id, shipment_medium, '<------')

        package = Package.objects.get(
            tracking_id=tracking_id,
            shipment_medium=shipment_medium,
            carrier=carrier
        )

        package_history = ShipmentHistory.objects.filter(package=package.pk)

        context['package'] = package
        context['package_history'] = package_history

    return render(request, template_name=template_name, context=context)