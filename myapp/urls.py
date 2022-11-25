from django.contrib import admin
from django.urls import path, include
from todo.views import home, addTodo, deleteTodo, mark_as_complete
from django.contrib.auth import views as auth_views
from users import views as users_views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("", home, name="home"),
    path("users/", include('users.urls')),
    
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    path("addTodo/", addTodo, name="addTodo"),
    path("delete/<int:item_id>/", deleteTodo, name="addTodo"),
    path("completed/",mark_as_complete, name="completed")
]