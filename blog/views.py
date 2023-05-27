from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import BlogPost, BlogComment
# Create your views here.
def blogHome(request):
    return render(request, 'home/index.html')


def blogPost(request, slug):
    recentPost = BlogPost.objects.order_by('?')[:8]
    comments = BlogComment.objects.all()
    post = BlogPost.objects.filter(slug = slug).first()
    comment = BlogComment.objects.filter(post = post)
    post.post_view = post.post_view + 1
    # time.sleep(5)
    post.save()
    context = {'post':post, 'comments':comment, 'recentPost':recentPost}
    return render(request, 'blog/place1.html', context)

def category(request, category):
    cat = BlogPost.objects.filter(category = category)
    count = cat.count()
    context = {'cat':cat}
    return render(request, 'blog/category.html', context)

def postComment(request):
    comment = None
    if request.method == "POST":
        comment = request.POST.get('comment')
        name = request.POST.get('name')
        email = request.POST.get('email')
        postSno = request.POST.get('postSno')
        post = BlogPost.objects.get(id = postSno)
        comment = BlogComment(comment = comment, post = post, name = name, email = email)
        comment.save()
        return redirect(f"/blog/{post.slug}")


def Contact(request):
    return render(request, 'home/Contact.html')