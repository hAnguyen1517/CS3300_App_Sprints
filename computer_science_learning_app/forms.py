from django import forms
from .models import Game, Usersys, LearningResource, Progress, PerformanceReport

# Class function for the login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# Class function for the sign upform
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usersys
        fields = ["Username", "Email", "password", "Role"]
        
# Form for viewing/ creating/ updating/ deleting a Game instance
class GameForm(forms.ModelForm):
    # configures the form based on the corresponding model, 
    #controlling how it behaves and what data it collects
    class Meta:
         # Specify the model to use for the form
        model = Game
        # Specify the fields to include in the form
        fields = ["Title", "Description", "Category", "Difficulty_Level"]
        

# Form for viewing/ creating/ updating/ deleting a Usersys instance
class UsersysForm(forms.ModelForm):
    class Meta:
        # Specify the model to use for the form
        model = Usersys
        # Specify the fields to include in the form
        fields = ["Username", "Email", "Role"]
        

# Form for viewing/ creating/ updating/ deleting a LearningResource instance
class LearningResourceForm(forms.ModelForm):
    class Meta:
         # Specify the model to use for the form
        model = LearningResource
         # Specify the fields to include in the form
        fields = ["Title", "Type", "Description", "Content", "Age_Appropriateness"]
       

# Form for creating a Progress instance
class ProgressForm(forms.ModelForm):
    class Meta:
         # Specify the model to use for the form
        model = Progress
         # Specify the fields to include in the form
        fields = ["UserID", "ResourceID", "CompletionStatus", "Grade", "TimeSpent"]
       

# Form for creating a PerformanceReport instance
class PerformanceReportForm(forms.ModelForm):
    class Meta:
        # Specify the model to use for the form
        model = PerformanceReport
        # Specify the fields to include in the form
        fields = ["UserID", "TasksCompleted", "AverageGrade", "AreasForDevelopment"]
 