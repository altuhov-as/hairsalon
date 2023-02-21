from django.shortcuts import render

from masterapp.models import Master


def index(request):
    title = 'главная'
    context = {"title": title, "master": Master.objects.get(user_id=request.user.pk)}
    return render(request, 'mainapp/index.html', context=context)


def gallery(request):
    title = 'примеры работ'

    context = {"title": title, "master": Master.objects.get(user_id=request.user.pk)}
    return render(request, 'mainapp/gallery.html', context=context)


def about(request):
    title = 'о нас'
    context = {"title": title, "master": Master.objects.get(user_id=request.user.pk)}
    return render(request, 'mainapp/about_us.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {"title": title, "master": Master.objects.get(user_id=request.user.pk)}
    return render(request, 'mainapp/contacts.html', context=context)
