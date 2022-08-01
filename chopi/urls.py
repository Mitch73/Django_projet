from django.contrib import admin
from django.urls import path
from app.views import index, product_detail, add_to_basket, basket, delete_basket
from django.conf.urls.static import static
from chopi import settings
from new_user.views import signup, logout_user, login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('product/<str:slug>/', product_detail, name='product'),
    path('product/<str:slug>/add_to_basket/', add_to_basket, name='add_to_basket'),
    path('basket/', basket, name='basket'),
    path('basket/delete/', delete_basket, name='delete_basket'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
