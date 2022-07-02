from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import GuestBook
from webapp.forms import GuestForm


# Create your views here.

def index_view(request):
    guest = GuestBook.objects.order_by('-create_time').filter(status='active')
    context = {'guests': guest}
    return render(request, 'index.html', context)


def create_view(request, **kwargs):
    if request.method == 'GET':
        form = GuestForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = GuestForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            guest = GuestBook.objects.create(name=name, email=email, text=text)
            guest.save()
            return redirect('index')
        else:
            return render(request, 'create.html', {'form': form})


def update_view(request, pk):
    list = get_object_or_404(GuestBook, pk=pk)
    if request.method == "GET":
        form = GuestForm(initial={
            'name': list.name,
            'email': list.email,
            'text': list.text,
        })
        return render(request, 'update.html', {'form': form})
    else:
        form = GuestForm(data=request.POST)
        if form.is_valid():
            list.name = form.cleaned_data.get('name')
            list.email = form.cleaned_data.get('email')
            list.text = form.cleaned_data.get('text')
            list.save()
            return redirect('index')
        return render(request, 'update.html', {'form': form})


def delete_view(request, pk):
    list = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', {'list': list})
    else:
        list.delete()
        return redirect('index')
