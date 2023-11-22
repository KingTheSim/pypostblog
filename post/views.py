from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    return render(request, "post/post_list.html", {"posts": posts})


def update_post(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_list")

    else:
        form = PostForm(instance=post)

    return render(request, "post/update_post.html", {"form": form, "post": post})


def create_post(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")

    else:
        form = PostForm()

    return render(request, "post/create_post.html", {"form": form})


def delete_post(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_id)
    post_title = post.title
    post_deleted = False

    if request.method == "POST":
        post.delete()
        post_deleted = True
        return redirect("post_list")

    return render(
        request,
        "post/delete_post_confirm.html",
        {"post": post, "post_deleted": post_deleted, "post_title": post_title}
    )
