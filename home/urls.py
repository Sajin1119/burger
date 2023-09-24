from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('book',views.book,name='book'),
    path('menu',views.menu,name='menu'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
