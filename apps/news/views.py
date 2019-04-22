from django.shortcuts import render
from .models import News,NewsCategory
from django.conf import settings
from utils import restful
from .serializers import NewsSerializer, CommentSerializer
from django.http import Http404
from .forms import PublicCommentForm
from .models import Comment
from apps.xfzauth.decorators import xfz_login_required
from django.db.models import Q
# Create your views here.
def index(request):
    count = settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.all().select_related('category','author').all()[0:count]
    categories = NewsCategory.objects.all()
    context = {
        'newses': newses,
        'categories': categories
    }
    return render(request, 'news/index.html', context=context)

#通过p参数来获取第几页的数据，并且这个p参数是根据查询字符串的方式传递过来 / news / list /?p = 2
def news_list(request):
    page = int(request.GET.get('p', 1))
    # 分类为0，不进行任何分类，之间按照时间倒叙排序
    category_id = int(request.GET.get('category_id', 0))

    start = (page-1)*settings.ONE_PAGE_NEWS_COUNT
    end = start + settings.ONE_PAGE_NEWS_COUNT
    if category_id == 0:
        newses = News.objects.select_related('category', 'author').all()[start:end]
    else:
        newses = News.objects.filter(category_id=category_id)[start:end]

    serializer = NewsSerializer(newses, many=True)
    data = serializer.data
    return restful.result(data=data)


def news_detail(request, news_id):
    try:
        news = News.objects.select_related('category', 'author').get(pk=news_id)
        context = {
            'news': news
        }
        return render(request, 'news/news_detail.html', context=context)
    except News.DoesNotExist:
        raise Http404
@xfz_login_required
def public_comment(request):
    form = PublicCommentForm(request.POST)
    if form.is_valid():
        news_id = form.cleaned_data.get('news_id')
        content = form.cleaned_data.get('content')
        news = News.objects.get(pk=news_id)
        comment = Comment.objects.create(content=content,news=news,author=request.user)
        serializer = CommentSerializer(comment)
        return restful.result(data=serializer.data)
    else:
        return restful.params_error(message=form.get_errors())

def search(request):
    q = request.GET.get('q')
    context = {}
    if(q):
        newses = News.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
        context['newses'] = newses
    return render(request,'search/search.html', context=context)


def login(request):
    return render(request, 'log/login.html')

def register(request):
    return render(request, 'log/login_register.html')