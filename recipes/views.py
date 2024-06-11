from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipes
from .forms import RecipeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q


######### Search Functionality #########
def search_results(request):
    query = request.GET.get('q')
    recipes = Recipes.objects.filter(name__icontains=query)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

######### User Authentication #########
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authentication successful
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page or any desired page after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')        
    else:
        form = AuthenticationForm()

    # If GET request or authentication fails, display the login form with errors
    return render(request, 'registration/login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after signup
            return redirect('home')  # Redirect to the home page or any desired page after signup

    # If GET request or form submission fails, display the signup form
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  


######### CRUD Functionality #########

def home(request):
    return render(request, 'base.html')

def recipe_list(request):
    query = request.GET.get('q')
    if query:
        recipes = Recipes.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(ingredients__icontains=query) |
            Q(steps__icontains=query) |
            Q(youtube_url__icontains=query) |
            Q(user__username__icontains=query)
        )
        return render(request, 'recipes/recipe_list_only.html', {'recipes': recipes})
    else:
        recipes = Recipes.objects.all()
        return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user  # Set the user to the current logged-in user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    
    # Check if the logged-in user is the owner of the recipe
    if request.user != recipe.user:
        return redirect('recipe_detail', pk=pk)
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    
    # Check if the logged-in user is the owner of the recipe
    if request.user == recipe.user:
        recipe.delete()
    
    return redirect('recipe_list')

# user profile page will show all recipes created by the user
@login_required
def user_profile(request):
    recipes = Recipes.objects.filter(user=request.user)
    return render(request, 'recipes/user_profile.html', {'recipes': recipes})