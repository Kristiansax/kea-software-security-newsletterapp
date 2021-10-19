from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewsLetterForm
from .models import SignupDetail

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the signup index.")

def newsletter_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewsLetterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            detail = SignupDetail()
            detail.username = form.cleaned_data['username']
            detail.first_name = form.cleaned_data['first_name']
            detail.last_name = form.cleaned_data['last_name']
            detail.email_adress = form.cleaned_data['email_address']
            detail.save()

            return render(request, 'thanks.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewsLetterForm()

    return render(request, 'signup.html', {'form': form})
