from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LogoutView

class PostView(View):
    def get(self, request):
        posts = Post.objects.all
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        form = CommentsForm()
        return render(request, 'blog/blog_detail.html', {'post': post,
                                                         'form': form})

class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f'/{pk}')


# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'blog/login.html'

class RegisterUser(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

class LogoutUser(LogoutView):
    pass

