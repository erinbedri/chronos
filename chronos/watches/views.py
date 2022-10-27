import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from chronos.watches.forms import CreateWatchForm, WatchCommentForm, EditWatchForm, DeleteWatchForm
from chronos.watches.models import Watch, WatchComment

WATCH_ADD_SUCCESS_MESSAGE = 'The watches was successfully added!'

WATCH_EDIT_SUCCESS_MESSAGE = 'The watches was successfully updated!'

WATCH_DELETE_SUCCESS_MESSAGE = 'The watches was successfully deleted!'

WATCHES_PER_PAGE = 8


def show_all_watches(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    watches_list = Watch.objects \
        .filter(
            Q(brand__icontains=q) |
            Q(model__icontains=q) |
            Q(style__icontains=q) |
            Q(year__icontains=q) |
            Q(condition__icontains=q) |
            Q(description__icontains=q) |
            Q(owner__username=q)) \
        .order_by('-created_at')

    brands = {watch.brand for watch in Watch.objects.all()}
    styles = {watch.style for watch in Watch.objects.all()}

    paginator = Paginator(watches_list, WATCHES_PER_PAGE)

    page_number = request.GET.get('page')

    try:
        watches = paginator.page(page_number)
    except PageNotAnInteger:
        watches = paginator.page(1)
    except EmptyPage:
        watches = paginator.page(paginator.num_pages)

    context = {
        'watches': watches,
        'brands': brands,
        'styles': styles,
    }

    return render(request, 'watches/show_all.html', context)


def show_my_watches(request):
    watches = Watch.objects.filter(owner_id=request.user.id).order_by('created_at')
    total_price_paid = sum([watch.price_paid if watch.price_paid is not None else 0 for watch in watches])

    context = {
        'watches': watches,
        'total_price_paid': total_price_paid,
    }

    return render(request, 'watches/show_collection.html', context)


@login_required
def add_watch(request):
    if request.method == 'POST':
        form = CreateWatchForm(request.POST, request.FILES)
        if form.is_valid():
            watch = form.save(commit=False)
            watch.owner = request.user
            watch.save()
            messages.success(request, WATCH_ADD_SUCCESS_MESSAGE)
            return redirect('watches:show_all_watches')
        else:
            messages.error(request, form.errors)
    else:
        form = CreateWatchForm()

    context = {
        'form': form,
    }

    return render(request, 'watches/add.html', context)


def show_watch(request, pk):
    watch = get_object_or_404(Watch, pk=pk)
    comments = WatchComment.objects.filter(watch_id=pk).order_by('created_on')
    comment_count = WatchComment.objects.filter(watch_id=pk).count()
    like_count = Watch.like_count(watch)

    liked = False
    if watch.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == 'POST':
        form = WatchCommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.watch = watch
            new_comment.author = request.user
            new_comment.save()
            return redirect('watches:show_watch', pk)
    else:
        form = WatchCommentForm()

    context = {
        'watch': watch,
        'comment_form': form,
        'comments': comments,
        'comment_count': comment_count,
        'like_count': like_count,
        'liked': liked,
    }
    return render(request, 'watches/details.html', context)


@login_required
def edit_watch(request, pk):
    watch = get_object_or_404(Watch, pk=pk)

    if request.user != watch.owner:
        return render(request, '403.html')

    if request.method == 'POST':
        form = EditWatchForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            form.save()
            messages.success(request, WATCH_EDIT_SUCCESS_MESSAGE)
            return redirect('watches:show_watch', pk)
    else:
        form = EditWatchForm(instance=watch)

    context = {
        'watch': watch,
        'form': form
    }

    return render(request, 'watches/edit.html', context)


@login_required
def delete_watch(request, pk):
    watch = get_object_or_404(Watch, pk=pk)

    if request.user != watch.owner:
        return render(request, '403.html')

    if request.method == 'POST':
        form = DeleteWatchForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            if watch.image:
                image_path = watch.image.path
                os.remove(image_path)
            watch.delete()
            messages.success(request, WATCH_DELETE_SUCCESS_MESSAGE)
            return redirect('watches:show_all_watches')
    else:
        form = DeleteWatchForm(instance=watch)

    context = {
        'watch': watch,
        'form': form
    }

    return render(request, 'watches/delete.html', context)


@login_required
def like_watch(request, pk):
    watch = get_object_or_404(Watch, pk=pk)
    liked = False

    if watch.likes.filter(id=request.user.id).exists():
        watch.likes.remove(request.user)
        liked = False
    else:
        watch.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('watches:show_watch', args=[str(pk)]))
