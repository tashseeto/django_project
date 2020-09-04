from django.urls import path
from .views import CreateAccountView
from .views import ChangeAccountView
from .views import MyAccountView
from .views import AuthorView


app_name = 'users'
urlpatterns = [
    path('create-account/',CreateAccountView.as_view(), name='createAccount'),
    path('change-account/',ChangeAccountView.as_view(), name='changeAccount'),
    path('my-account/<int:pk>',MyAccountView.as_view(), name='myAccount'),
    path('author/<int:pk>/authorStories', AuthorView.as_view(), name='authorStories'),
]