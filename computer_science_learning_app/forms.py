from django import forms
from .models import Game, Usersys

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        # Specify the model to use for the form
        fields = ['Title', 'Description', 'Category', 'Difficulty_Level']
        # Specify the fields to include in the form

class UsersysForm(forms.ModelForm):
    class Meta:
        model = Usersys
        # Specify the model to use for the form
        fields = ['Username', 'Password', 'Email', 'Role']
        # Specify the fields to include in the form
    