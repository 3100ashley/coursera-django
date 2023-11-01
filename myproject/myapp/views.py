from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm
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
    return HttpResponse('<h1>About Us</h1>')

def menu(request):
    return HttpResponse('<h1>Menu</h1>')

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