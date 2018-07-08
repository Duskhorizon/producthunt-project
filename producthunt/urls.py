from django.contrib import admin
from django.urls import path
from django.urls import include
# from django.conf import settings
# from django.conf.urls.static import static
import products.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
]
