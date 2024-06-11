from django.urls import path
from .views import recipe_list, recipe_detail, recipe_create, home, user_login, user_signup, recipe_update, recipe_delete, user_logout, search_results, user_profile

urlpatterns = [
    path('', home, name='home'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipes/create/', recipe_create, name='recipe_create'),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('recipes/<int:pk>/update/', recipe_update, name='recipe_update'),
    path('recipes/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
    path('myrecipes/', user_profile, name='my_recipes')
]
