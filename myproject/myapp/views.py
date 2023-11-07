from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm
from .models import Menu
# Create your views here.
def drinks(request, drink_name):
    options = {
        'mocha':'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }

    choice_of_drink = options[drink_name]

    return HttpResponse(f"<h2>{drink_name}</h2>" + choice_of_drink)

def home(request):
    return HttpResponse('<h1>Welcome to Little Lemon</h1>')

def about(request):
    about_content = "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."
    return render(request, 'about.html', {'content': about_content})
    

def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {"menu": menu_items}
    return render(request, 'menu.html', items_dict)

def book(request):
    return HttpResponse('<h1>Make a Booking</h1>')

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)