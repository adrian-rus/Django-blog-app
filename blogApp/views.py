from django.shortcuts import render
from django.utils import timezone
from .models import Post


# creating a view that will return a list of Posts
# that were published prior to 'now' and
# render them to the 'blogposts.html' template

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    return render(request, 'blogposts.html',
                  {'posts': posts})
