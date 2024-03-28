from django.shortcuts import render, redirect, get_object_or_404
from .models import Usersys, Game, LearningResource, Progress, PerformanceReport
from .forms import UsersysForm,GameForm


def index(request):
    # Retrieve the list of available games
    games = Game.objects.all()
    # Pass the games to the template context
    context = {'games': games}
    # Render the index.html template with the games data
    return render(request, 'index.html', context)


def usersys_list(request):
    users = Usersys.objects.all()
    return render(request, 'usersys_list.html', {'users': users})

def usersys_detail(request, pk):
    user = get_object_or_404(Usersys, pk=pk)
    return render(request, 'usersys_detail.html', {'user': user})

def usersys_create(request):
    if request.method == 'POST':
        form = UsersysForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('usersys_detail', pk=user.pk)
    else:
        form = UsersysForm()
    return render(request, 'usersys_form.html', {'form': form})

def usersys_update(request, pk):
    user = get_object_or_404(Usersys, pk=pk)
    if request.method == 'POST':
        form = UsersysForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('usersys_detail', pk=user.pk)
    else:
        form = UsersysForm(instance=user)
    return render(request, 'usersys_form.html', {'form': form})

def usersys_delete(request, pk):
    user = get_object_or_404(Usersys, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('usersys_list')
    return render(request, 'usersys_confirm_delete.html', {'user': user})

# Views for Game model
def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game_detail.html', {'game': game})

def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('game_detail', pk=game.pk)
    else:
        form = GameForm()
    return render(request, 'game_form.html', {'form': form})

def game_update(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save()
            return redirect('game_detail', pk=game.pk)
    else:
        form = GameForm(instance=game)
    return render(request, 'game_form.html', {'form': form})

def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'game_confirm_delete.html', {'game': game})

# Views for LearningResource model (similar structure as Game model)

# Views for Progress model (similar structure as Game model)

# Views for PerformanceReport model (similar structure as Game model)
