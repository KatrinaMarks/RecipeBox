from django.urls import path
from . import views
from .views import SearchResultsView

# All pages of the website
urlpatterns = [
    path("", views.home, name="home"),
    path("search/",  SearchResultsView.as_view(), name="search_results"),
    path("recipe/<str:title>/edit", views.edit_recipe, name="edit_recipe"),
    path("recipe/<str:title>/", views.individual_recipe, name="individual_recipe"),
    path("recipe/", views.new_recipe, name="new_recipe"),
    path("all_recipes/", views.all_recipes, name="all_recipes"),
    path("section/<str:title>/", views.individual_section, name="individual_section"),
    path("section/", views.new_section, name="new_section"),
    path("account/", views.account, name="account"),
    path("create_account/", views.create_account, name="create_account"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("change_password/", views.change_password, name='change_password'),
    path("edit_profile/", views.edit_profile, name="edit_profile")
]
