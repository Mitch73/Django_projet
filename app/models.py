from tabnanny import verbose
from email.mime import image
from time import timezone
from tkinter import CASCADE
from django.db import models
from django.template.defaultfilters import slugify
# from django.contrib.auth import get_user_model
from chopi.settings import AUTH_USER_MODEL
from django.urls import reverse

# class ChopiApp contient le titre du produit, le prix et la description 
class ProductApp(models.Model):
    # le titre du produit
    title = models.CharField(max_length=255, unique=True, verbose_name='Titre')
    image = models.ImageField(upload_to='product')
    # slug c'est la version du titre qui va être utiliser à l'interieur des urls 
    # blank ne n'empeche pas de créer un article
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    # prix du produit
    price = models.IntegerField()
    # la création du produit ne sera pas par default publié
    published = models.BooleanField(default=False, verbose_name='En stock')
    last_updated = models.DateTimeField(auto_now=True)
    # la description du produit
    content = models.TextField(blank=True, verbose_name='Description')

    # la methode string retourne le titre du produit au de l'indentifiant du produit
    def __str__(self):
        return self.title

    # cette methode permet d'accèder à la page de detail du produit depuis la page utilisateur (change product app)
    def get_absolute_url(self):
        # on passe le nom de la fonction et les arguments envoyer a l'url
        # après le nom de l'url on passe dans un paramètre kwargs un dictionnaire avec les different élements de l'url (slug et self)
        # c'est le même slug qu'ont retrouve dans urls.py 
         return reverse('product', kwargs={'slug': self.slug})   

# Commands utilisateur
class Order(models.Model):
    # clé étrangère permettant de relier un utilisateur a plusieur produit
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE) 
    # on relie la variable product à la classe productapp
    product = models.ForeignKey(ProductApp, on_delete=models.CASCADE)
    # la quantité du panier par default débute à 1
    quantity = models.IntegerField(default=1)
    # la valeur du produit dans le panier par default est false
    ordered = models.BooleanField(default=False)
    # date de la commande 
    ordered_date = models.DateTimeField(blank=True, null=True)
    
    # affiche dans l'interface d'administration les modèles
    def __str__(self):
        # on affiche le nom du produit ainsi que la quantite
        return f"{self.product.title} ({self.quantity})"

# Panier utilisateur
class Basket(models.Model):
    # un utilisateur ne peut avoir un seul panier
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    # manytomanyfield = plusieur produits dans un même panier
    orders = models.ManyToManyField(Order)
    

    def __str__(self):
        # nom de l'utilisateur associate au panier
        return self.user.username

    # supprime les articles du panier
    def delete(self, *args, **kwargs):
        for order in self.order.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        # clear detache les articles du panier
        self.orders.clear()
        super().delete(*args, **kwargs)

