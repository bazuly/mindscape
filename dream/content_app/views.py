from django.shortcuts import render

from .models import NewsUpdateModel, FAQModel, AboutModel
from .services.pagination import paginate_queryset


def news_update_view(request):
    news_data = NewsUpdateModel.objects.all().order_by('-publish_at')
    paginate_news_data = paginate_queryset(news_data, request)
    context = {
        'news_data': paginate_news_data
    }
    return render(request, 'templates/pages/news.html', context)


def faq_view(request):
    faq_data = FAQModel.objects.all()
    faq_paginate_data = paginate_queryset(faq_data, request)
    context = {
        'faq_data': faq_paginate_data
    }
    return render(request, 'templates/pages/faq.html', context)


def about_view(request):
    about_data = AboutModel.objects.all()
    paginate_about_data = paginate_queryset(about_data, request)
    context = {
        'paginate_about_data': paginate_about_data
    }
    return render(request, 'templates/pages/about.html', context)

