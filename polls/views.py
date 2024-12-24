from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from .forms import QuestionForm, ChoiceFormSet
from django.contrib.auth.decorators import login_required


# from django.http import HttpResponse

def home(request):
    return render (request, "polls/home.html")
def landing_page(request):
    return render (request, "polls/landing.html")

def about(request):
    return render(request , "polls/about.html")

def contact(request):
    return render(request, 'polls/contact.html')

def register(request):
    if request.method =='POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Welcome account created sucessfully")
            return redirect('home')
        else:
            messages.error(request, 'sorry there was an error in registration.')
    else:
        form = UserCreationForm()
    return render(request, 'polls/register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Login the user
            return redirect('home')  # Redirect to a page after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  # Stay on login page in case of failure
    else:
        form = AuthenticationForm()  # Use the AuthenticationForm for login
        return render(request, 'polls/login.html', {'form': form})




def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        try:
            send_mail(
                f"Message from {name}",
                message,
                email,
                ['your_email@example.com'],  # Replace with your email
            )
            messages.success(request, "Your message has been sent!")
        except Exception:
            messages.error(request, "Failed to send the message. Please try again.")
        return redirect('contact')
    return render(request, 'polls/contact.html')



@login_required
def create_poll(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        choice_formset = ChoiceFormSet(request.POST)
        if question_form.is_valid() and choice_formset.is_valid():
            question = question_form.save()
            choices = choice_formset.save(commit=False)
            for choice in choices:
                choice.question = question
                choice.save()
            return redirect('polls:poll_list')  # Redirect to the list of polls
    else:
        question_form = QuestionForm()
        choice_formset = ChoiceFormSet()
    return render(request, 'polls/create_poll.html', {
        'question_form': question_form,
        'choice_formset': choice_formset,
    })



