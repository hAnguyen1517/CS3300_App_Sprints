from django.shortcuts import render, redirect, get_object_or_404
from .models import Usersys, Game, LearningResource, Progress, PerformanceReport
from .forms import UsersysForm,GameForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView

# def index(request):
#     # Retrieve the list of available games
#     games = Game.objects.all()
#     # Pass the games to the template context
#     context = {'games': games}
#     # Render the index.html template with the games data
#     return render(request, 'index.html', context)

class IndexView(ListView):
    template_name = 'index.html'  # Specify the template to use
    queryset = Game.objects.all()  # Specify the queryset to fetch games
    context_object_name = 'games'  # Specify the context variable name for games list


# def usersys_list(request):
#     users = Usersys.objects.all()
#     return render(request, 'usersys_list.html', {'users': users})

class UsersysListView(ListView):
    template_name = 'usersys_list.html'  # Specify the template to use
    queryset = Usersys.objects.all()  # Specify the queryset to fetch users
    context_object_name = 'users'  # Specify the context variable name for users list


# def usersys_detail(request, pk):
#     user = get_object_or_404(Usersys, pk=pk)
#     return render(request, 'usersys_detail.html', {'user': user})

class UsersysDetailView(DetailView):
    model = Usersys  # Specify the model for the detail view
    template_name = 'usersys_detail.html'  # Specify the template to use
    context_object_name = 'user'  # Specify the context variable name for the user object


class UsersysCreateView(CreateView):
    model = Usersys  # Specify the model for the create view
    form_class = UsersysForm  # Specify the form class to use
    template_name = 'usersys_form.html'  # Specify the template to use

    def form_valid(self, form):
        user = form.save()
        return redirect('usersys_detail', pk=user.pk)
    


# def usersys_update(request, pk):
#     user = get_object_or_404(Usersys, pk=pk)
#     if request.method == 'POST':
#         form = UsersysForm(request.POST, instance=user)
#         if form.is_valid():
#             user = form.save()
#             return redirect('usersys_detail', pk=user.pk)
#     else:
#         form = UsersysForm(instance=user)
#     return render(request, 'usersys_form.html', {'form': form})

class UsersysUpdateView(UpdateView):
    model = Usersys  # Specify the model for the update view
    form_class = UsersysForm  # Specify the form class to use
    template_name = 'usersys_form.html'  # Specify the template to use

    def form_valid(self, form):
        user = form.save()
        return redirect('usersys_detail', pk=user.pk)

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
def learning_resource_list(request):
    learning_resources = LearningResource.objects.all()
    return render(request, 'learning_resource_list.html', {'learning_resources': learning_resources})

def learning_resource_detail(request, pk):
    learning_resource = get_object_or_404(LearningResource, pk=pk)
    return render(request, 'learning_resource_detail.html', {'learning_resource': learning_resource})

def learning_resource_create(request):
    if request.method == 'POST':
        form = LearningResourceForm(request.POST)
        if form.is_valid():
            learning_resource = form.save()
            return redirect('learning_resource_detail', pk=learning_resource.pk)
    else:
        form = LearningResourceForm()
    return render(request, 'learning_resource_form.html', {'form': form})

def learning_resource_update(request, pk):
    learning_resource = get_object_or_404(LearningResource, pk=pk)
    if request.method == 'POST':
        form = LearningResourceForm(request.POST, instance=learning_resource)
        if form.is_valid():
            learning_resource = form.save()
            return redirect('learning_resource_detail', pk=learning_resource.pk)
    else:
        form = LearningResourceForm(instance=learning_resource)
    return render(request, 'learning_resource_form.html', {'form': form})

def learning_resource_delete(request, pk):
    learning_resource = get_object_or_404(LearningResource, pk=pk)
    if request.method == 'POST':
        learning_resource.delete()
        return redirect('learning_resource_list')
    return render(request, 'learning_resource_confirm_delete.html', {'learning_resource': learning_resource})
# Views for Progress model (similar structure as Game model)

# Views for PerformanceReport model (similar structure as Game model)
