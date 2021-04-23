from .models import blog
from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import TemplateView
from django.db.models import Count,Q

def home(request):
    blog_list = blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 6)
    try:
        paginated_query = paginator.page(page)
    except PageNotAnInteger:
        paginated_query = paginator.page(1)
    except EmptyPage:
        paginated_query = paginator.page(paginator.num_pages)
    return render(request,'blog/index.html',{
                                            'users':paginated_query,
                                            })

def contact(request):
    return render(request,'blog/contact.html')

def about(request):
    return render(request,'blog/about.html')

def category(request):
    data_tag = blog.objects.all().order_by('-timestamp')[:5]
    data = blog.objects.all()
    most_recent = blog.objects.order_by('-timestamp')[:3]
    blog_list = blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 6)
    try:
        paginated_query = paginator.page(page)
    except PageNotAnInteger:
        paginated_query = paginator.page(1)
    except EmptyPage:
        paginated_query = paginator.page(paginator.num_pages)
    return render(request,'blog/category.html',{
                                            'data':data,
                                            'most_recent':most_recent,
                                            'users':paginated_query,
                                            'data_tag':data_tag,
                                            })

def post(request, id):
    try:
        data = blog.objects.filter(id=id)
    except:
        data = None
    most_recent = blog.objects.order_by('-timestamp')[:3]
    data_tag = blog.objects.all().order_by('-timestamp')[:5]
    return render(request,'blog/post.html',{
                                            'data':data,
                                            'data_tag':data_tag,
                                            'most_recent':most_recent,
                                            })

def search(request):
    if request.method == 'POST':
        srch_data = request.POST.get('search_data')
        try:
            data = blog.objects.filter(title__icontains=srch_data)[:3]
        except:
            data = None
        if srch_data:
            scrh_data_show_upper = srch_data.upper()
        else:
            scrh_data_show_upper = None
        return render(request,'blog/search.html',{
                                            'data':data,
                                            'srch_data':scrh_data_show_upper,
                                            })
    else:
        return render(request,'blog/search.html',)