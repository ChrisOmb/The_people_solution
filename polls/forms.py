from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Choice
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']

ChoiceFormSet = forms.inlineformset_factory(
    Question, Choice, fields=['choice_text'], extra=3, can_delete=False
)
