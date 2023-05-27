from django.db.models.aggregates import Count
from django.shortcuts import render, HttpResponse
from blog.models import BlogPost
import math
from blog.models import BlogComment
from blog.views import blogPost,BlogComment
from explore.models import Explore

# Create your views here.
def home(request):
    explore= Explore.objects.all()
    charam = BlogPost.objects.all()
    karam = BlogPost.objects.order_by('-post_view')[:5]
    no_of_post = 4
    # comment = BlogComment.objects.filter(post = karam)
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    
    param = BlogPost.objects.all()
    length = len(param)
    param = param[(page - 1)*(no_of_post):page*no_of_post]
    if page>1:
        prev = page -1 
    else:
         prev = None

    if page<math.ceil(length/no_of_post):
        nxt = page+1

    elif page>math.ceil(length/no_of_post):
        nxt = None
        prev = math.ceil(length/no_of_post) - 1
        page = math.ceil(length/no_of_post)
    else: 
        nxt = None

    tour1 = BlogPost.objects.filter(category = 'tour')
    tour = tour1.count()
    rural1 = BlogPost.objects.filter(category = 'rural')
    rural = rural1.count()
    cultural1 = BlogPost.objects.filter(category = 'cultural')
    cultural = cultural1.count()
    adventure1 = BlogPost.objects.filter(category = 'adventure')
    adventure = adventure1.count()
    beach1 = BlogPost.objects.filter(category = 'beach')
    beach = beach1.count()
    context = {'dests':param,'explore':explore, 'prev':prev, 'nxt':nxt, 'page':page, 'charam':charam, 'tour':tour, 'rural':rural, 
    'cultural':cultural, 'adventure':adventure, 'beach':beach, 'karam':karam}
    return render(request, 'home/index.html', context)
    

def Contact(request):
    return render(request, 'home/Contact.html')

def about(request):
    return render(request, 'home/about.html')

def page3(request):
    return render(request, 'page3.html')

def error_404_view(request):
    return render(request, '404.html')