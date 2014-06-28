from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blog.models import posts
 
def home(request):
    blog_posts = posts.objects.all()
    paginator = Paginator(blog_posts, 3)
    
    page = request.GET.get('page')
    try:
        entries = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        entries = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        entries = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {'posts' : entries})