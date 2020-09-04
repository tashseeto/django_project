from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm
from django.views.generic.detail import DetailView
from django.views import generic


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ChangeAccountView(CreateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('login')
    template_name = 'users/changeAccount.html'

class MyAccountView(DetailView):
    template_name = 'users/myAccount.html'
    model = CustomUser
    context_object_text = 'user'

class AuthorView(generic.DetailView):
    template_name = 'users/authorStories.html'
    model = CustomUser
    context_object_text = 'author'