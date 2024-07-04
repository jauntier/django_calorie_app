

# Create your views here.
from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodItemForm
from django.utils import timezone

def index(request):
    today = timezone.now().date()
    food_items = FoodItem.objects.filter(added_on=today)
    total_calories = sum(item.calories for item in food_items)
    return render(request, 'calorieapp/index.html', {'food_items': food_items, 'total_calories': total_calories})

def add_food_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to index.html after successfully adding item
    else:
        form = FoodItemForm()
    return render(request, 'calorieapp/add_food_item.html', {'form': form})

def delete_food_item(request, item_id):
    item = FoodItem.objects.get(id=item_id)
    item.delete()
    return redirect('index')

def reset_calories(request):
    today = timezone.now().date()
    FoodItem.objects.filter(added_on=today).delete()
    return redirect('index')