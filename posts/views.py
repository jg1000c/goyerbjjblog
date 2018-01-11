from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.order_by('-pub_date')
        return queryset

class PostDetailView(DetailView):
    model = Post
