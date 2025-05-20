from django.shortcuts import render, redirect
from .models import Gasto
from .forms import GastoForm
import json
from datetime import datetime
from collections import defaultdict
import json
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def obtener_datos_por_categoria():
    gastos = Gasto.objects.all()
    categorias = {}

    for gasto in gastos:
        if gasto.categoria in categorias:
            categorias[gasto.categoria] += float(gasto.monto)
        else:
            categorias[gasto.categoria] = float(gasto.monto)

    return json.dumps([{"categoria": c, "total": categorias[c]} for c in categorias])

def debug_data(request):
    datos = obtener_datos_por_categoria()
    return JsonResponse(datos, safe=False)

def obtener_datos_gastos():
    gastos = Gasto.objects.all()
    return json.dumps([{"nombre": g.nombre, "monto": float(g.monto)} for g in gastos])

def eliminar_gasto(request, gasto_id):
    gasto = get_object_or_404(Gasto, id=gasto_id)
    gasto.delete()
    messages.success(request, "¡Gasto eliminado correctamente!")
    return redirect("index")



@login_required(login_url="login")
def index(request):
    query = request.GET.get("q", "")
    fecha_inicio = request.GET.get("fecha_inicio", "")
    fecha_fin = request.GET.get("fecha_fin", "")

    if request.method == "POST":
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Gasto agregado exitosamente!")
            return redirect("index")

    form = GastoForm()
    gastos = Gasto.objects.all()

    if query:
        gastos = gastos.filter(nombre__icontains=query)
    if fecha_inicio and fecha_fin:
        gastos = gastos.filter(fecha__range=[fecha_inicio, fecha_fin])

    gastos_por_categoria_json = obtener_datos_por_categoria()

    return render(request, "gastosp/index.html", {
        "form": form,
        "gastos": gastos,
        "gastos_por_categoria_json": gastos_por_categoria_json
    })

