from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import redirect, render

User = get_user_model()

def signup(request):
    # si la requette est du type post on recupère les informations du formulaire
    # on crée l'utilisateur, connect au site et on redirige à la page index
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)

        login(request, user)
        return redirect('index')
    return render(request, 'new_user/signup.html')

def login_user(request):
    # les utilisateurs pourrons ce connecter via le formulaire login
    # on recupère les informations du formulaire s'incrire dans la base de donnée
    # et redirige à la page index
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user: 
            login(request, user)
            return redirect('index')
    return render(request, 'new_user/login.html')    

# fonction logout permet de se deconnecté du site
def logout_user(request):
    logout(request)
    return redirect('index')    