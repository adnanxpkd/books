from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import redirect, render



# Create your views here.


def Signout_View(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
