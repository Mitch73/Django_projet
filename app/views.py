from itertools import product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
# on import le modèl depuis l'app
from app.models import ProductApp, Basket, Order
from django.urls import reverse 

def index(request):
    # all permet de recuperer tous les produits
    products = ProductApp.objects.all()
    # on a une clé products qu'on passe à la variable products qui est égale à tous les products qu'on va recupere
    return render(request, "app/index.html", context={"products": products})

def product_detail(request, slug):
    product = get_object_or_404(ProductApp, slug=slug)
    return render(request, 'app/details.html', context={'product': product})

def add_to_basket(request, slug):
    # recupères l'utilisateur
    user = request.user
    # recupères le produit s'il exists on lui passe le slug
    product = get_object_or_404(ProductApp, slug=slug)
    # recupères le panier associer à l'utilisateur s'il exist sinon on le créer
    # _ variable non utilisable par la suite
    basket, _ = Basket.objects.get_or_create(user=user)
    # recupères les commands de chaque utilisateurs s'il exist sinon on le créer
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)

    # si la commande n'existe pas on la créer et on l'ajoute au panier
    if created:
        # orders = ManyToManyFields
        basket.orders.add(order)
        basket.save()
        # si elle existe on increment 1
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse('product', kwargs={'slug': slug}))

# recupères le panier de l'utilisateur
def basket(request):
    # si l'objet existe on l'associe a la variable basket
    basket = get_object_or_404(Basket, user=request.user)

    return render(request, 'app/basket.html', context={'orders': basket.orders.all()})

def delete_basket(request):
    # recupères l'élement s'il existe et on le supprime
    basket = request.user.basket
    if basket:
        basket.delete()

    return redirect('index')

def style(request):
    return render(request, 'index.html')
