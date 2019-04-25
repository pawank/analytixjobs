# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext, loader

from frontend.models import Subscribe


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context = RequestContext(request, {
    })
    response = render_to_response(
        "frontend/index.html", {}, context)
    return response


def subscribe(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    message = {"id": None, "message": ""}
    if request.GET:
        name = request.GET["name"] if "name" in request.GET else None
        email = request.GET["email"] if "email" in request.GET else None
        status = Subscribe(name=name, email=email)
        status.save()
        pk = status.id
        message = {
            "id": pk, "message": "Thank you for subscribing to the newsletter."}
    print(message)
    context = RequestContext(request, {"message": message})
    response = render_to_response(
        "frontend/index.html", {}, context)
    return response
