from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# from .models import Post
# from .forms import PostForm
# from .decorators import check_draft


class PostListView(ListView):
    # model = Post
    template_name = "blog/blog_list.html"