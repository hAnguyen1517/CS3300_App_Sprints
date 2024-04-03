from django import forms
from .models import Game, Usersys, LearningResource, Progress, PerformanceReport


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        # Specify the model to use for the form
        fields = ["Title", "Description", "Category", "Difficulty_Level"]
        # Specify the fields to include in the form


class UsersysForm(forms.ModelForm):
    class Meta:
        model = Usersys
        # Specify the model to use for the form
        fields = ["Username", "Password", "Email", "Role"]
        # Specify the fields to include in the form


class LearningResourceForm(forms.ModelForm):
    class Meta:
        model = LearningResource
        # Specify the model to use for the form
        fields = ["Title", "Type", "Description", "Content", "Age_Appropriateness"]
        # Specify the fields to include in the form


class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        # Specify the model to use for the form
        fields = ["UserID", "ResourceID", "CompletionStatus", "Grade", "TimeSpent"]
        # Specify the fields to include in the form


class PerformanceReportForm(forms.ModelForm):
    class Meta:
        model = PerformanceReport
        # Specify the model to use for the form
        fields = ["UserID", "TasksCompleted", "AverageGrade", "AreasForDevelopment"]
        # Specify the fields to include in the form
