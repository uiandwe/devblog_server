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

    return render(request, "blog/list.html", {
        'user': request.user.is_anonymous
    })


def BlogDetail(request, id):
    return render(request, "blog/detail.html", {})


def BlogCreate(request):

    if request.user.is_anonymous:
        return render(request, "blog/list.html", {
            'user': request.user.is_anonymous
        })

    return render(request, "blog/create.html", {
        'userId': request.user.id
    })
