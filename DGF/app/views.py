# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import Box
#from .serializers import BoxSerializer
from django.template import loader
# Create your views here.

import sys
#sys.path.append('/usr/lib/freecad/lib')
import FreeCAD
import Part
import importWebGL

def index(request):
    version = FreeCAD.Version()
    return HttpResponse("<h1>this is app1 homepage " + str(version))

def createCube(request):
    doc = FreeCAD.newDocument("Unnamed1")
    doc.addObject("Part::Box", "Box")
    doc.ActiveObject.Label = "Cube"
    doc.recompute()
    FreeCAD.getDocument("Unnamed1").getObject("Box").Length = 100
    FreeCAD.getDocument("Unnamed1").getObject("Box").Width = 200
    FreeCAD.getDocument("Unnamed1").getObject("Box").Height = 100
    doc.recompute()
    __objs__ = []
    __objs__.append(FreeCAD.getDocument("Unnamed1").getObject("Box"))
    importWebGL.export(__objs__, u"/DGF/app/templates/cube1.html")

    return render(request, u"/DGF/app/templates/cube1.html")
