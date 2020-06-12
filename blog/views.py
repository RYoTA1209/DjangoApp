from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'posts':posts})