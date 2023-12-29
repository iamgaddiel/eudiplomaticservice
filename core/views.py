from django.shortcuts import render,redirect
from django.views.generic import TemplateView, DetailView

from custom_admin.models import Package, ShipmentHistory



class Root(TemplateView):
    template_name = 'core/index.html'


class About(TemplateView):
    template_name = 'core/about.html'


class ContactUs(TemplateView):
    template_name = 'core/contact.html'


class TermsAndCondition(TemplateView):
    template_name = 'core/terms_and_condition.html'


class PrivacyPolicy(TemplateView):
    template_name = 'core/privacy.html'


def handle_404_request(request, exception):
    template_name = '404.html'
    return render(request, template_name=template_name)


def handle_500_request(request):
    template_name = '505.html'
    return render(request, template_name, status=500)


def track_page(request):
    context: dict[str, str] = {}
    template_name = 'core/tracking_detail.html'

    if request.method == 'POST':
        carrier = request.POST.get('carrier')
        tracking_id = request.POST.get('tracking_id')
        shipment_medium = request.POST.get('shipment_medium')

        try:
            package = Package.objects.get(
                tracking_id=tracking_id,
                shipment_medium=shipment_medium,
                carrier=carrier
            )

            package_history = ShipmentHistory.objects.filter(package=package.pk)

            context['package'] = package
            context['package_history'] = package_history
        except (Package.DoesNotExist, ShipmentHistory.DoesNotExist):
            context = {
                'error': 'Package not found'
            }
            return render(request, template_name=template_name, context=context)

    return render(request, template_name=template_name, context=context)
