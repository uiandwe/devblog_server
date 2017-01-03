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


def BlogListView(request):

    return render(request, "blog/blog_list.html", {})


def BlogDetail(request):

    return render(request, "blog/blog_detail.html", {})


def BlogCreate(request):

    return render(request, "blog/create.html", {})
