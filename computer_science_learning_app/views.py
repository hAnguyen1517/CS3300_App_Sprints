from django.shortcuts import render, redirect, get_object_or_404
from .models import Usersys, Game, LearningResource, Progress, PerformanceReport
from .forms import (
    UsersysForm,
    GameForm,
    LearningResourceForm,
    ProgressForm,
    PerformanceReportForm,
)
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class IndexView(ListView):
    # Display a list of games on the index page
    template_name = "index.html"
    queryset = Game.objects.all()
    context_object_name = "games"


class UsersysListView(ListView):
    # Display a list of users
    template_name = "usersys_list.html"
    queryset = Usersys.objects.all()
    context_object_name = "users"


class UsersysDetailView(DetailView):
    # Display details of a user
    model = Usersys
    template_name = "usersys_detail.html"
    context_object_name = "user"


class UsersysCreateView(CreateView):
    # Create a new user
    model = Usersys
    form_class = UsersysForm
    template_name = "usersys_form.html"

    def form_valid(self, form):
        # Save the user and redirect to their details page
        user = form.save()
        return redirect("usersys_detail", pk=user.pk)


class UsersysUpdateView(UpdateView):
    # Update an existing user
    model = Usersys
    form_class = UsersysForm
    template_name = "usersys_form.html"

    def form_valid(self, form):
        user = form.save()
        return redirect("usersys_detail", pk=user.pk)


def usersys_delete(request, pk):
    # Delete an existing user
    user = get_object_or_404(Usersys, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect("usersys_list")
    return render(request, "usersys_confirm_delete.html", {"user": user})


# Views for Game model
class GameListView(ListView):
    # Display a list of games on the games list page
    model = Game
    template_name = "game_list.html"
    context_object_name = "games"


class GameDetailView(DetailView):
    # Display details of the game
    model = Game
    template_name = "game_detail.html"
    context_object_name = "game"


class GameCreateView(CreateView):
    # Create a new game
    model = Game
    form_class = GameForm
    template_name = "game_form.html"

    def form_valid(self, form):
        game = form.save()
        return redirect("game_detail", pk=game.pk)


class GameUpdateView(UpdateView):
    # Update an existing game
    model = Game
    form_class = GameForm
    template_name = "game_form.html"

    def form_valid(self, form):
        game = form.save()
        return redirect("game_detail", pk=game.pk)


def game_delete(request, pk):
    # Delete an existing game
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        game.delete()
        return redirect("game_list")
    return render(request, "game_confirm_delete.html", {"game": game})


# Views for LearningResource model
class LearningResourceListView(ListView):
    # Display a list of learning resources on the resources page
    model = LearningResource
    template_name = "learning_resource_list.html"
    context_object_name = "learning_resources"

class LearningResourceDetailView(DetailView):
    # Display details of a learning resource
    model = LearningResource
    template_name = "learning_resource_detail.html"
    context_object_name = "learning_resource"

class LearningResourceCreateView(CreateView):
    # Create a new learning resource
    model = LearningResource
    form_class = LearningResourceForm
    template_name = "learning_resource_form.html"

    def form_valid(self, form):
        learning_resource = form.save()
        return redirect("learning_resource_detail", pk=learning_resource.pk)

class LearningResourceUpdateView(UpdateView):
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
class ProgressListView(ListView):
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

class ProgressDetailView(DetailView):
    # Display details of a progress record
    model = Progress
    template_name = "progress_detail.html"
    context_object_name = "progress"

class ProgressCreateView(CreateView):
    # Create a new progress record
    model = Progress
    form_class = ProgressForm
    template_name = "progress_form.html"

    def form_valid(self, form):
        progress = form.save()
        return redirect("progress_detail", pk=progress.pk)

class ProgressUpdateView(UpdateView):
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
class PerformanceReportListView(ListView):
    # Display a list of performance report records
    model = PerformanceReport
    template_name = "performance_report_list.html"
    context_object_name = "reports"

    def get_queryset(self):
        queryset = super().get_queryset()
        for report in queryset:
            user = Usersys.objects.get(pk=report.UserID_id)
            report.username = user.Username
        return queryset

class PerformanceReportDetailView(DetailView):
    # Display details of a performance report
    model = PerformanceReport
    template_name = "performance_report_detail.html"
    context_object_name = "report"

class PerformanceReportCreateView(CreateView):
    # Create a new performance report
    model = PerformanceReport
    form_class = PerformanceReportForm
    template_name = "performance_report_form.html"

    def form_valid(self, form):
        report = form.save()
        return redirect("performance_report_detail", pk=report.pk)

class PerformanceReportUpdateView(UpdateView):
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
