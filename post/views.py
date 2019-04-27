from django.shortcuts import render, HttpResponse, get_object_or_404
from.models import post
from django.shortcuts import render, HttpResponse



def post_index(request):
    posts = post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request, id):
    posts = get_object_or_404(post, id=id)
    context={
        'post': posts,
    }
    return render(request, 'post/detail.html', context)

def post_create(request):
    return HttpResponse('Burası post create sayfası')

def post_update(request):
    return HttpResponse('Burası post update sayfası')

def post_delete(request):
    return HttpResponse('Burası post delete sayfası')

def home_view(request):
    if request.user.is_authenticated:
        context = {

            'isim': 'İlker',
        }
    else:
        context = {

            'isim': 'Misafir',
        }

    return render(request, 'home.html', context)


