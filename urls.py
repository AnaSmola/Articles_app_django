from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('news', views.news_list, name='list_news'),
    path('single/<int:pk>', views.new_single, name='new_single'),
    path('news/category/<int:category_id>', views.news_list, name='new_by_category'),
    path('tag/<int:tag_id>', views.news_list, name='new_by_tag'),
    path('news/add/article', views.add_new_article, name='add_new_article'),
    path('news/single/edit/<int:pk>', views.update_new, name='update_new'),
    path('news/single/delete/<int:pk>', views.delete_new, name='delete_new'),
    path('adds/add_new/', views.create_new_add, name='create_add'),
    path('adds', views.adds_list, name='list_adds'),
    path('single_add/<int:pk>', views.single_add, name='add_single'),
    path('add_single/edit_add/<int:pk>', views.edit_add, name='edit_add'),
    path('add_single/delete_add/<int:pk>', views.delete_add, name='delete_add'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
