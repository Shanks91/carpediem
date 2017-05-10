from django.shortcuts import render, redirect, get_object_or_404
from .forms import NgoForm, HappeningForm, GalleryForm, HapCommentsForm, NgoRatingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Ngo, Happening, Gallery, HapComments


@login_required()
def createngo(request):
    if request.method == 'POST':
        form = NgoForm(request.POST, request.FILES)
        if form.is_valid():
            ngo = form.save(commit=False)
            ngo.moderator = request.user
            ngo.save()
            key = ngo.get_live_id()
            return redirect('ngo_profile', pk=key)
        else:
            return render(request, 'ordinem/create.html', {'form': form})
    else:
        form = NgoForm()
    return render(request, 'ordinem/create.html', {'form': form})


def ngolist(request):
    ngo_list = Ngo.objects.all()
    return render(request, 'ordinem/index.html', {'ngo_list': ngo_list})


def ngoprofile(request, pk):
    ngo = get_object_or_404(Ngo, id=pk)
    happenings = Happening.objects.filter(author=ngo).order_by('-id')
    comments = HapComments.objects.filter(comment_on__in=happenings)
    return render(request, 'ordinem/detail2.html', {'ngo': ngo, 'happenings': happenings, 'comments': comments})


@login_required()
def post_happening(request, pk):
    ngo = get_object_or_404(Ngo, id=pk)
    if request.method == 'POST':
        form = HappeningForm(request.POST)
        if form.is_valid():
            happening = form.save(commit=False)
            happening.author = ngo
            happening.save()
            return redirect('ngo_profile', pk=pk)
        else:
            return render(request, 'ordinem/post_h.html', {'form': form})
    else:
        form = HappeningForm()
        return render(request, 'ordinem/post_h.html', {'form': form})


@login_required()
def follow_ngo(request, npk, upk):
    user = get_object_or_404(User, id=upk)
    ngo = get_object_or_404(Ngo, id=npk)
    user.profile.follows.add(ngo)
    return redirect('ngo_profile', pk=npk)


@login_required()
def post_gallery(request, pk):
    ngo = get_object_or_404(Ngo, id=pk)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.owner = ngo
            gallery.save()
            return redirect('gallery', pk=pk)
        else:
            return render(request, 'ordinem/post_g.html', {'form': form})
    else:
        form = GalleryForm()
        return render(request, 'ordinem/post_g.html', {'form': form})


def gallery_view(request, pk):
    ngo = get_object_or_404(Ngo, id=pk)
    galleries = Gallery.objects.filter(owner=ngo)
    return render(request, 'ordinem/gallery.html', {'ngo': ngo, 'galleries': galleries})


def ngo_like(request, pk):
    ngo = get_object_or_404(Ngo, id=pk)
    ngo.like()
    return redirect('ngo_profile', pk=pk)


@login_required()
def post_comment(request, pk):
    happening = get_object_or_404(Happening, id=pk)
    user = request.user
    if request.method == 'POST':
        form = HapCommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = user
            comment.comment_on = happening
            comment.save()
            return redirect('ngo_list')
        else:
            return render(request, 'ordinem/comment.html', {'form': form})
    else:
        form = HapCommentsForm()
        return render(request, 'ordinem/comment.html', {'form': form})


@login_required()
def rate_ngo(request, pk):
    ngo = get_object_or_404(Ngo, id=pk)
    user = request.user
    if request.method == 'POST':
        form = NgoRatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = user
            rating.ngo = ngo
            rating.save()
            ngo.calculate_ratings()
            return redirect('ngo_profile', pk=pk)
        else:
            return render(request, 'ordinem/rating_form.html', {'form': form})
    else:
        form = NgoRatingForm()
        return render(request, 'ordinem/rating_form.html', {'form': form})