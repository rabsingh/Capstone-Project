from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import Item
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.added_by = request.user
            item.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'shopping_list_app/add_item.html', {'form': form})

def item_list(request):
    items = Item.objects.all().order_by('-date_added')
    return render(request, 'shopping_list_app/item_list.html', {'items': items})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.user == item.added_by or request.user.is_staff:
        item.delete()
        messages.success(request, 'Item deleted successfully')
    else:
        messages.error(request, 'You can only delete your own items')
    return redirect('item_list')