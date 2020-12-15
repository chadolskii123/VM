from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, CreateView, UpdateView, DetailView
from .forms import LoginForm, RegisterForm, UserDetailChangeForm
from .mixins import NextUrlMixin, RequestFormAttachMixin

# Create your views here.

class AccountHomeView(LoginRequiredMixin, DetailView):
    template_name = "accounts/home.html"

    def get_object(self):
        return self.request.user

# Mixin 안에 함수들을 넣어서 Form의 값을 self에 담아 줄 수 있다.!!!!!!!!!
class LoginView(NextUrlMixin, FormView):
    form_class = LoginForm
    template_name = "accounts/login.html"

    def form_valid(self, form):
        next_url = self.get_next_url()
        return redirect(next_url)
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = "로그인"
        context['button'] = "들어가기"
        return context


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

    def get_context_data(self, **kwargs) :
            context = super().get_context_data(**kwargs)
            context['title'] = "회원가입"
            context['button'] = "가입하기"
            return context


class UserDetailChangeView(LoginRequiredMixin, UpdateView):
    form_class = UserDetailChangeForm
    template_name = 'accounts/detail_update_view.html'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UserDetailChangeView, self).get_context_data(**kwargs)
        context['title'] = 'Change Your Account Details'
        return context

    def get_success_url(self):
        return reverse("accounts:home")