from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Project
import os
from django.core.mail import send_mail

PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))  # To get root directory of project


# Create your views here.
def index(request):  # index page function based views
    projects = Project.objects.all().order_by('-created_at')[:4]  # sort by date (desc) and get first 4 post
    context = {
        "all_projects": projects,
    }
    return render(request, "index.html", context=context)


def full(request):  # to get all posts list
    all_projects = Project.objects.all().order_by('-created_at')
    context = {
        "full_portfolio": all_projects,
    }
    return render(request, "index.html", context=context)


def details(request, slug):  # find each post by slug field and render in new template
    each_post = get_object_or_404(Project, slug=slug)
    file = each_post.file
    context = {
        "one_post_detail": each_post,
        "file": file,

    }
    return render(request, "details.html", context=context)


def email(request):  # send email from custom HTML email form
    name = request.POST['name']
    email_to = request.POST['email']
    body = request.POST['message']
    send_mail(
        name,
        body,
        'qarashov787@gmail.com',
        [email_to],
        fail_silently=False,
    )
    return redirect(index)


def download(request, slug):  # download file related to post (one to one relation)
    each_post = get_object_or_404(Project, slug=slug)
    file = each_post.file.file
    filename = None
    context = {
        "one_post_download": each_post,
        "file": file.file

    }
    filename = str(file)
    tempname = filename.replace('/', "\\")
    temp = PROJECT_PATH + "\\" + "media" + "\\" + tempname
    target_file = open(temp, 'rb')
    response = HttpResponse(target_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response

