from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.home, name='home'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/create', views.createLibros, name='create'),
    path('libros/edit', views.editLibros, name='edit'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/edit/<int:id>', views.editLibros, name='edit'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
