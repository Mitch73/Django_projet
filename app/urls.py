from django.urls import path
from app.views import AppHome

# la variable permet de preciser les urls
app_name = "chopi"

urlpatterns = [
# path permet de retouner la classe Apphome entant que vue
    path('', AppHome.as_view(), name='home')
]

