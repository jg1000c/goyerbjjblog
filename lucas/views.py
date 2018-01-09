from django.views.generic import ListView, DetailView

from .models import Lucas


class LucasListView(ListView):
    model = Lucas
    paginate_by = 10


class LucasDetailView(DetailView):
    model = Lucas
