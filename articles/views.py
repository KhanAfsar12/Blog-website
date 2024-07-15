from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .forms import LoginForm
from .models import Article
from django.contrib.auth import authenticate, login

# Create your views here.
def article_list(request):
    article_list = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'article_list': article_list})


def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(request, username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                login(request, user)
                return HttpResponse("You are authenticated")
            
            else:
                return HttpResponse("Invalid login")
            
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})