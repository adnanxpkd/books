from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from django.shortcuts import get_object_or_404, redirect, render
from . models import Audiobook, Ebook
from home.forms import AudioBookForm, ConatctForm, EbookForm

@login_required
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})

def signout(request):
    # if request.method == 'POST':
    #     logout(request)
    #     return redirect('signin')        
    logout(request)            # log the user out
    return redirect('signin')

def index(request):
    return render(request, 'index.html')

def ebook_list(request):
    books = Ebook.objects.all()
    return render(request, 'book_list.html', {'books': books})

def audiobook_list(request):
    audiobooks = Audiobook.objects.all()
    return render(request, 'audiobook_list.html', {'audiobooks': audiobooks})

def ebook_add(request):
    if request.method == 'POST':
        form = EbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
    else:
        form = EbookForm()

    return render(request, 'book_form.html',{'frm':form})

def ebookupdate(request, pk):
    book = get_object_or_404(Ebook,pk=pk)
    if request.method == 'POST':
        form = EbookForm(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect('ebook_list')
    else:
        form = EbookForm(instance=book)
    return render(request, 'book_form.html',{'frm':form})

def ebookdelete(request,pk):
    book = get_object_or_404(Ebook,pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('ebook_list')
    return render(request, 'delete.html',{'book':book})

def audiobook_add(request):
    if request.method == 'POST':
        form = AudioBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('audiobook_list')
    else:
        form = AudioBookForm()
    return render(request, 'audiobook_form.html',{'frm': form})

def audiobookupdate(request, pk):
    audiobook = get_object_or_404(Audiobook, pk=pk)
    if request.method == 'POST':
        form = AudioBookForm(request.POST, instance=audiobook)
        if form.is_valid():
            form.save()
            return redirect('audiobook_list')
    else:
        form = AudioBookForm(instance=audiobook)
    return render(request, 'audiobook_form.html',{'frm': form})

def about(request):
    return render(request, 'about.html')

def social_media(request):
    return render(request, 'social_media.html')

def contacts(request):
    if request.method == 'POST':
        form = ConatctForm(request.POST)
        if form.is_valid():
            return redirect('success_page')
    else:
        form = ConatctForm()
    return render(request, 'contacts.html', {'form': form})
