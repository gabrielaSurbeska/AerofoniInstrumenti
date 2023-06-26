"""
URL configuration for Domashno5_2011858 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Instruments.views import index, registerorsingin, register, singin, koshnicka, hamrmonika_info, duvacki_info, \
    duvacki_Instrumenti, slobodni_Aerofoni, list_objavi, add_item, add_item_to_card, payment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('registerorsingin/', registerorsingin, name="registerorsingin"),
    path('register/', register, name="register"),
    path('singin/', singin, name="singin"),
    path('koshnicka/', koshnicka, name="koshnicka"),
    path('hamrmonika_info/', hamrmonika_info, name="hamrmonika_info"),
    path('duvacki_info/', duvacki_info, name="duvacki_info"),
    path('duvacki_Instrumenti/', duvacki_Instrumenti, name="duvacki_Instrumenti"),
    path('slobodni_Aerofoni/', slobodni_Aerofoni, name="slobodni_Aerofoni"),
    path('list_objavi/', list_objavi, name="list_objavi"),
    path('add_item/', add_item, name="add_item"),
    path('add_item_to_card/', add_item_to_card, name="add_item_to_card"),
    path('payment/', payment, name="payment"),
    path('duvacki_Instrumenti/duvacki_info.html',duvacki_info, name="duvacki_Instrumenti"),
    path('index/Slobodni_Aerofoni.html',slobodni_Aerofoni, name="slobodni_Instrumenti"),
    path('index/Duvacki_Instrumenti.html',duvacki_Instrumenti, name="duvacki_Instrumenti"),
    path('index/duvacki_info.html',duvacki_info, name="duvacki_Info"),
    path('index/add_to_card.html',add_item_to_card, name="add_to_card"),
    path('index/payment.html',payment, name="payment"),
    path('index/index.html',index, name="pocetna"),
    path('index/harmonika_info.html',hamrmonika_info, name="harmonika_info"),
    path('index/registerorsingin.html',registerorsingin, name="registerorlogin"),
    path('index/register.html',register, name="register"),
    path('index/singin.html', singin, name="singin"),
    path('index/list_objavi.html', list_objavi, name="lista"),
    path('index/New_item.html', add_item, name="lista"),
    path('index/koshnicka.html', koshnicka, name="koshnicka"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
