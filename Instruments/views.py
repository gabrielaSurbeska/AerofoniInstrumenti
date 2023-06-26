from django.shortcuts import render

from Instruments.form1 import Slobodni_AerofoniForm
from Instruments.form3 import RegisterForm
from Instruments.models import Slobodni_Aerofoni, Duvacki_Instrumenti, Register


# Create your views here.
def index(request):
    return render(request, "index.html")

def registerorsingin(request):
    return render(request, "registerorsingin.html")

def add_item(request):
    queryset = Slobodni_Aerofoni.objects.all()
    context = {"aerofoni": queryset, "slobodni": Slobodni_AerofoniForm}
    return render(request, "New_item.html",context=context)

def add_item_to_card(request):
    return render(request, "add_to_card.html")

def payment(request):
    return render(request, "payment.html")

def register(request):
    queryset = Register.objects.all()
    context = {"register": queryset, "registerform": RegisterForm}
    return render(request, "register.html", context=context)

def singin(request):
    return render(request, "singin.html")

def koshnicka(request):
    return render(request, "koshnicka.html")


def list_objavi(request):
    return render(request, "list_objavi.html")

def hamrmonika_info(request):
    queryset = Slobodni_Aerofoni.objects.all()
    context = {"harmonika": queryset}
    return render(request, "harmonika_info.html", context=context)

def duvacki_info(request):
    queryset = Duvacki_Instrumenti.objects.all()
    context = {"duv": queryset}
    return render(request, "duvacki_info.html", context=context)

def duvacki_Instrumenti(request):
    queryset = Duvacki_Instrumenti.objects.all()
    context = {"duvacki": queryset, "formi": Duvacki_Instrumenti}
    return render(request, "Duvacki_Instrumenti.html", context=context)

def slobodni_Aerofoni(request):
    queryset = Slobodni_Aerofoni.objects.all()
    context = {"aerofoni": queryset,"Aero": Slobodni_AerofoniForm}
    return render(request, "Slobodni_Aerofoni.html", context=context)