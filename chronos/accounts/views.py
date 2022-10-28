from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from chronos.accounts.forms import RegisterUserForm, CustomAuthenticationForm, EditUserForm, DeleteUserForm
from chronos.watches.models import Watch

REGISTRATION_SUCCESS_MESSAGE = 'Registration successful!'

LOGIN_SUCCESS_MESSAGE = 'You are successfully logged in '
LOGIN_ERROR_MESSAGE = 'Invalid username or password!'

LOGOUT_SUCCESS_MESSAGE = 'You are successfully logged out.'

PROFILE_EDIT_SUCCESS_MESSAGE = 'You successfully updated your profile information!'

PROFILE_DELETE_SUCCESS_MESSAGE = 'You successfully deleted your profile information!'


def register_account(request):
    if request.user.is_authenticated:
        return redirect('web:show_homepage')

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, REGISTRATION_SUCCESS_MESSAGE)
            return redirect('watches:show_all_watches')
        else:
            messages.error(request, form.errors)
    else:
        form = RegisterUserForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('web:homepage')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            user = authenticate(username=username, password=password)
            if user is not None:
                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified = True
                login(request, user)
                messages.success(request, LOGIN_SUCCESS_MESSAGE + f'as {username}!')
                return redirect('watches:show_all_watches')
            else:
                messages.error(request, LOGIN_ERROR_MESSAGE)
        else:
            messages.error(request, LOGIN_ERROR_MESSAGE)
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, LOGOUT_SUCCESS_MESSAGE)
    return redirect('web:show_homepage')


@login_required
def show_account(request):
    watch_count = Watch.objects.filter(owner=request.user).count()
    total_paid = sum(
        [watch.price_paid if watch.price_paid is not None else 0
         for watch in Watch.objects.filter(owner=request.user)])

    context = {
        'watch_count': watch_count,
        'total_paid': total_paid,
    }

    return render(request, 'accounts/details.html', context)


@login_required
def edit_account(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, PROFILE_EDIT_SUCCESS_MESSAGE)
            return redirect('accounts:show_account')
        else:
            messages.error(request, form.errors)
    else:
        form = EditUserForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'accounts/edit.html', context)


@login_required
def delete_account(request):
    if request.method == 'POST':
        form = DeleteUserForm(request.POST, instance=request.user)
        if form.is_valid():
            request.user.delete()
            messages.success(request, PROFILE_DELETE_SUCCESS_MESSAGE)
            return redirect('web:show_homepage')
    else:
        form = DeleteUserForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'accounts/delete.html', context)
