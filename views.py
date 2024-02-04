from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import News, Category, Comments
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.db.models import Q
from django.forms.utils import ErrorList
from .forms import *
from django import forms


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def news_list(request, category_id=None, tag_id=None):
    """Show all news
    """

    category = None
    categories = Category.objects.all()
    news = News.objects.filter(status='published').order_by('-created')
    tag = None
    search_query = request.GET.get('search','')

    if search_query:
        news = News.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    else:
        news = News.objects.all()

    if tag_id:
        tag = get_object_or_404(Tag, id=tag_id)
        news = news.filter(tags=tag)

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        news = news.filter(category=category)

    return render(request, "main/news/news_list.html", {"news": news,
                                                        "categories": categories,
                                                        "category": category,
                                                        "tag": tag,
                                                        })


def add_new_article(request):

    if request.method == 'POST':
        # submitting the form
        form = CreateNewArticle(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('list_news')
    else:
        form = CreateNewArticle()
    return render(request, 'main/news/create_new.html', {"form": form})


def update_new(request, pk):

    action = "Update the article!"
    new = get_object_or_404(News, id=pk)
    form = CreateNewArticle(request.POST or None, instance=new)

    if form.is_valid():
        # update the add here
        form.save()
        # redirect to single add page
        return redirect('new_single', new.pk)

    else:
        return render(request, 'main/news/update.html', locals())


def delete_new(request, pk):
    new = get_object_or_404(News, id=pk)

    if request.method == "POST":
        new.delete()
        return redirect('list_news')
    else:
        return render(request, 'main/news/delete.html', locals())



def new_single(request, pk):

    """Show single new
    """

    new = get_object_or_404(News, id=pk)
    comments = Comments.objects.filter(new=pk)
    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.new = new
            user_comment.save()
            return redirect(new_single, pk)  # locals()
    else:
        comment_form = NewCommentForm()
    return render(request, "main/news/new_single.html",{"new": new,
                                                        "comment": user_comment,
                                                        "comment_form": comment_form,
                                                        "comments": comments})


def adds_list(request):

    all_adds = Adds.objects.order_by('-published')
    return render(request, 'main/ads/adds_list.html',
                {'action': 'Here there are all advertisements of the group', 'all_adds': all_adds})


def single_add(request, pk):
    add = get_object_or_404(Adds, id=pk)
    return render(request, "main/ads/add_single.html",
                  {"add": add})


def create_new_add(request):
    """Create single add
    """
    if request.method == 'POST':
        form = CreateAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_adds')

    else:
        form = CreateAddForm()
    return render(request, 'main/ads/create_add.html', locals())


def edit_add(request, pk):

    action = "Update your add!"

    add = get_object_or_404(Adds, id=pk)
    form = CreateAddForm(request.POST or None, instance=add)

    if form.is_valid():
        # update the add here
        form.save()
        # redirect to single add page
        return redirect('add_single', add.pk)

    else:
        return render(request, 'main/ads/update.html', locals())


def delete_add(request, pk):

    add = get_object_or_404(Adds, id=pk)
    if request.method == "POST":
        add.delete()
        return redirect('list_adds')
    else:
        return render(request, 'main/ads/delete.html', locals())

