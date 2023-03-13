from .models import Client
from django.views import generic


class View(generic.ListView):
    model = Client
    template_name = 'views.html'
    context_object_name = 'views'


class Detail(generic.DetailView):
    model = Client
    template_name = 'credit_detail.html'
