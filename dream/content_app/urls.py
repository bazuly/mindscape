from django.urls import path
from .views import about_view, faq_view, news_update_view

app_name = 'content_app'


urlpatterns = [
    path('about_view/', about_view, name='about_view'),
    path('faq_view/', faq_view, name='faq_view'),
    path('news_update_view', news_update_view, name='news_update_view'),
    
]
