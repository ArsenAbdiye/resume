from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import main_banner

urlpatterns = [
    path("", main_banner, name='main_banner'),  # Главная страница
]

# Добавляем поддержку медиа-файлов, если в DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
