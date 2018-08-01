# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import Box
#from .serializers import BoxSerializer
from django.template import loader
# Create your views here.

import sys
sys.path.append('/usr/lib/freecad/lib')
import FreeCAD
import Part
import importWebGL

def index(request):
    version = FreeCAD.Version()
    return HttpResponse("<h1>this is app1 homepage " + str(version))