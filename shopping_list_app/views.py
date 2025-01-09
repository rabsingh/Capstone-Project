from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import Item
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ItemFilterForm
from datetime import datetime, timedelta

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    # Check if user is authorized to edit this item
    if request.user != item.added_by and not request.user.is_superuser:
        messages.error(request, 'You can only edit your own items')
        return redirect('item_list')
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated successfully')
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'shopping_list_app/edit_item.html', {'form': form, 'item': item})

# Show item list with filter feature
@login_required
def item_list(request):
    items = Item.objects.all().order_by('-week_beginning')
    filter_form = ItemFilterForm(request.GET)
    
    if filter_form.is_valid():
        # Filter by week beginning
        if filter_form.cleaned_data.get('week_beginning'):
            items = items.filter(week_beginning=filter_form.cleaned_data['week_beginning'])
        
        # Filter by user
        if filter_form.cleaned_data.get('added_by'):
            items = items.filter(added_by=filter_form.cleaned_data['added_by'])
        
        # Filter by authorization status
        if filter_form.cleaned_data.get('authorised') in ['True', 'False']:
            authorized = filter_form.cleaned_data['authorised'] == 'True'
            items = items.filter(authorised=authorized)

    context = {
        'items': items,
        'filter_form': filter_form
    }
    return render(request, 'shopping_list_app/item_list.html', context)

# Add an item
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

# Delete an item
@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.user == item.added_by or request.user.is_staff:
        item.delete()
        messages.success(request, 'Item deleted successfully')
    else:
        messages.error(request, 'You can only delete your own items')
    return redirect('item_list')

# Register
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


# To authorise items
@staff_member_required
def update_authorised_status(request, item_id):
    """Allow superusers to toggle the 'authorised' status of an item."""
    item = get_object_or_404(Item, id=item_id)
    if request.user.is_superuser:
        item.authorised = not item.authorised  # Toggle the status
        item.save()
        status = "authorised" if item.authorised else "pending"
        messages.success(request, f'Item "{item.item_name}" is now marked as {status}.')
    else:
        messages.error(request, 'You do not have permission to change the status of this item.')
    return redirect('item_list')


    