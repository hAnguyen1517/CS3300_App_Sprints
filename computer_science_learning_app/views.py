from django.shortcuts import render, redirect, get_object_or_404
from .models import Usersys, Game, LearningResource, Progress, PerformanceReport
from .forms import (
    UsersysForm,
    GameForm,
    LearningResourceForm,
    ProgressForm,
    PerformanceReportForm,
    SignupForm,
    LoginForm
    
)
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseForbidden

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             password = form.cleaned_data.get('password')
#             user.set_password(password)
#             # check if password is sent raw we can login
#             # user.password = password
#             user.save()
#             login(request, user)
#             return redirect('index')  
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, Username=username, password=password)
#             print(username)
#             print(password)
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return redirect('index')  
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

def registerPage(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('Username')
            email = form.cleaned_data.get('Email')
            user.set_password(password)
            # check if password is sent raw we can login
            # user.password = password
            user.save()
            # Mirror user creation to auth_user table
            auth_user = User(username=username, email=email)  # Set username explicitly
            auth_user.set_password(password)
            auth_user.save()

            return redirect('login')  
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})

def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, Username=username, password=password)
            print(username)
            print(password)
            print(user)
            
            if user is not None:
                messages.success(request, "Welcome.{uername}")
                login(request, user)
                # return redirect('index')  
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def logoutPage(request):   
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have been logged out successfully.")
    return redirect('login')

class IndexView(LoginRequiredMixin,ListView):
    # Display a list of games on the index page
    template_name = "index.html"
    queryset = Game.objects.all()
    context_object_name = "games"

#ListView for displaying a list of users
# Retrieves all Usersys objects from the database
# and sends them to the template specified in 'template_name'
# The context variable 'users' is used to access the list of users in the template
class UsersysListView(LoginRequiredMixin, ListView):
    template_name = "usersys_list.html"
    context_object_name = "users"

    def dispatch(self, request, *args, **kwargs):
        # Check if the user is logged in and has the role of "teacher"
        if not request.user.is_authenticated or request.user.Role != 'teacher':
            return HttpResponseForbidden("You are not allowed to access this page.")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # Return the queryset of all users
        return Usersys.objects.all()
# DetailView for displaying detailed information about each user
# Retrieves a single Usersys object from the database based on the provided URL parameter (usually user's primary key)
# and sends it to the template specified in 'template_name'
# The context variable 'user' is used to access the user object in the template
class UsersysDetailView(LoginRequiredMixin, DetailView):
    # Display details of a user
    model = Usersys
    template_name = "usersys_detail.html"
    context_object_name = "user"

# CreateView for creating a new user
# Uses the UsersysForm form to display the form for creating a new user
# When the form is submitted and valid, the new user is saved to the database
# The user is then redirected to their details page using the URL named 'usersys_detail' with the user's primary key as a parameter
class UsersysCreateView(LoginRequiredMixin, CreateView):
    # Create a new user
    model = Usersys
    form_class = UsersysForm
    template_name = "usersys_form.html"

    def form_valid(self, form):
        # Save the user and redirect to their details page
        user = form.save()
        return redirect("usersys_detail", pk=user.pk)

# UpdateView for updating of an existing user
# Uses the UsersysForm form to display the form for updating an existing user
# When the form is submitted and valid, the updated user is saved to the database
# The user is then redirected to their details page using the URL named 'usersys_detail' with the user's primary key as a parameter
class UsersysUpdateView(LoginRequiredMixin, UpdateView):
    # Update an existing user
    model = Usersys
    form_class = UsersysForm
    template_name = "usersys_form.html"

    def form_valid(self, form):
        user = form.save()
        return redirect("usersys_detail", pk=user.pk)

# Function for deleting an existing user
# Retrieves the user object with the given primary key (pk) from the database
def usersys_delete(request, pk):
    # Delete an existing user
    user = get_object_or_404(Usersys, pk=pk)
    # If the request method is POST (usually from a form submission),
    # delete the user from the database
    if request.method == "POST":
        user.delete()
        return redirect("usersys_list")
    # If the request method is not POST (GET request),
    # render a confirmation page for deleting the user
    return render(request, "usersys_confirm_delete.html", {"user": user})


# Views for Game model
# ListView for displaying a list of games
# Retrieves all Game objects from the database
# and sends them to the template specified in 'template_name'
# The context variable 'games' is used to access the list of games in the template
class GameListView(LoginRequiredMixin,ListView):
    # Display a list of games on the games list page
    model = Game
    template_name = "game_list.html"
    context_object_name = "games"

# DetailView for showing detailed information about a game
# Retrieves a single Game object from the database based on the provided URL parameter (usually game's primary key)
# and sends it to the template specified in 'template_name'
# The context variable 'game' is used to access the game object in the template
class GameDetailView(LoginRequiredMixin,DetailView):
    # Display details of the game
    model = Game
    template_name = "game_detail.html"
    context_object_name = "game"

# CreateView for handling the creation of a new game
# Eses the GameForm form to display the form for creating a new game
# When the form is submitted and valid, the new game is saved to the database
# The user is then redirected to the game's details page using the URL named 'game_detail' with the game's primary key as a parameter
    model = Game
class GameCreateView(LoginRequiredMixin,CreateView):
    # Create a new game
    model = Game
    form_class = GameForm
    template_name = "game_form.html"
    # Function saves the game and redirects to its details page after successful submission.
    def form_valid(self, form):
        game = form.save()
        return redirect("game_detail", pk=game.pk)

# UpdateView for handling the updating of an existing game
# Uses the GameForm form to display the form for updating an existing game
# When the form is submitted and valid, the updated game is saved to the database
# The user is then redirected to the game's details page using the URL named 'game_detail' with the game's primary key as a parameter
class GameUpdateView(LoginRequiredMixin,UpdateView):
    # Update an existing game
    model = Game
    form_class = GameForm
    template_name = "game_form.html"
    # Func saves the updated game and redirect to its details page
    def form_valid(self, form):
        game = form.save()
        return redirect("game_detail", pk=game.pk)

# Function for handling the deletion of an existing game
# Retrieves the game object with the given primary key (pk) from the database
def game_delete(request, pk):
    # Delete an existing game
    game = get_object_or_404(Game, pk=pk)
    # If the request method is POST (usually from a form submission),
    # delete the game from the database
    if request.method == "POST":
        game.delete()
        # Redirect the user to the game_list page after deletion
        return redirect("game_list")
    # If the request method is not POST (GET request),
    # render a confirmation page for deleting the game
    return render(request, "game_confirm_delete.html", {"game": game})


# Views for LearningResource model
class LearningResourceListView(LoginRequiredMixin,ListView):
    # Display a list of learning resources on the resources page
    model = LearningResource
    template_name = "learning_resource_list.html"
    context_object_name = "learning_resources"

class LearningResourceDetailView(LoginRequiredMixin,DetailView):
    # Display details of a learning resource
    model = LearningResource
    template_name = "learning_resource_detail.html"
    context_object_name = "learning_resource"

class LearningResourceCreateView(LoginRequiredMixin,CreateView):
    # Create a new learning resource
    model = LearningResource
    form_class = LearningResourceForm
    template_name = "learning_resource_form.html"

    def form_valid(self, form):
        learning_resource = form.save()
        return redirect("learning_resource_detail", pk=learning_resource.pk)

class LearningResourceUpdateView(LoginRequiredMixin,UpdateView):
    # Update an existing learning resource
    model = LearningResource
    form_class = LearningResourceForm
    template_name = "learning_resource_form.html"

    def form_valid(self, form):
        learning_resource = form.save()
        return redirect("learning_resource_detail", pk=learning_resource.pk)

def learning_resource_delete(request, pk):
    # Delete an existing learning resource
    learning_resource = get_object_or_404(LearningResource, pk=pk)
    if request.method == "POST":
        learning_resource.delete()
        return redirect("learning_resource_list")
    return render(
        request,
        "learning_resource_confirm_delete.html",
        {"learning_resource": learning_resource},
    )


# Views for Progress model (similar structure as Game model)
class ProgressListView(LoginRequiredMixin,ListView):
    # Display a list of Progress on the progress page
    model = Progress
    template_name = "progress_list.html"
    context_object_name = "progresses"

    def get_queryset(self):
        queryset = super().get_queryset()
        for progress in queryset:
            user = Usersys.objects.get(pk=progress.UserID_id)
            progress.username = user.Username
        return queryset

class ProgressDetailView(LoginRequiredMixin,DetailView):
    # Display details of a progress record
    model = Progress
    template_name = "progress_detail.html"
    context_object_name = "progress"

class ProgressCreateView(LoginRequiredMixin,CreateView):
    # Create a new progress record
    model = Progress
    form_class = ProgressForm
    template_name = "progress_form.html"

    def form_valid(self, form):
        progress = form.save()
        return redirect("progress_detail", pk=progress.pk)

class ProgressUpdateView(LoginRequiredMixin,UpdateView):
    # Update an existing progress record
    model = Progress
    form_class = ProgressForm
    template_name = "progress_form.html"

    def form_valid(self, form):
        progress = form.save()
        return redirect("progress_detail", pk=progress.pk)

def progress_delete(request, pk):
    # Delete an existing progress record
    progress = get_object_or_404(Progress, pk=pk)
    if request.method == "POST":
        progress.delete()
        return redirect("progress_list")
    return render(request, "progress_confirm_delete.html", {"progress": progress})


# Views for PerformanceReport model
class PerformanceReportListView(LoginRequiredMixin, ListView):
    # Display a list of performance report records
    model = PerformanceReport
    template_name = "performance_report_list.html"
    context_object_name = "reports"

    def dispatch(self, request, *args, **kwargs):
        # Check if the user is logged in and has the role of "teacher"
        if not request.user.is_authenticated or request.user.Role != 'teacher':
            return HttpResponseForbidden("You are not allowed to access this page.")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        for report in queryset:
            user = Usersys.objects.get(pk=report.UserID_id)
            report.username = user.Username
        return queryset
class PerformanceReportDetailView(LoginRequiredMixin,DetailView):
    # Display details of a performance report
    model = PerformanceReport
    template_name = "performance_report_detail.html"
    context_object_name = "report"

class PerformanceReportCreateView(LoginRequiredMixin,CreateView):
    # Create a new performance report
    model = PerformanceReport
    form_class = PerformanceReportForm
    template_name = "performance_report_form.html"

    def form_valid(self, form):
        report = form.save()
        return redirect("performance_report_detail", pk=report.pk)

class PerformanceReportUpdateView(LoginRequiredMixin,UpdateView):
    # Update an existing performance report
    model = PerformanceReport
    form_class = PerformanceReportForm
    template_name = "performance_report_form.html"

    def form_valid(self, form):
        report = form.save()
        return redirect("performance_report_detail", pk=report.pk)


def performance_report_delete(request, pk):
    # Delete an exiting performance report
    report = get_object_or_404(PerformanceReport, pk=pk)
    if request.method == "POST":
        report.delete()
        return redirect("performance_report_list")
    return render(request, "performance_report_confirm_delete.html", {"report": report})
