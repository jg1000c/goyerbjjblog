from django.views.generic import ListView, DetailView

from .models import Technique

class TechniqueDetailView(DetailView):
    model = Technique

class LucasListView(ListView):
    model = Technique
    paginate_by = 10

    def get_queryset(self):
        queryset = Technique.objects.filter(author__startswith='Lucas')
        return queryset

