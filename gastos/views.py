from django.shortcuts import render, redirect
from .models import Gasto
from .forms import GastoForm
import json
from datetime import datetime

def obtener_datos_gastos():
    gastos = Gasto.objects.all()
    return json.dumps([{"nombre": g.nombre, "monto": float(g.monto)} for g in gastos])

def index(request):
    query = request.GET.get("q", "")
    fecha_inicio = request.GET.get("fecha_inicio", "")
    fecha_fin = request.GET.get("fecha_fin", "")

    gastos = Gasto.objects.all()

    if query:
        gastos = gastos.filter(nombre__icontains=query)

    if fecha_inicio and fecha_fin:
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        gastos = gastos.filter(fecha__range=[fecha_inicio, fecha_fin])

    gastos_json = obtener_datos_gastos()

    return render(
        request, "gastosp/index.html", 
        {"form": GastoForm(), "gastos": gastos, "gastos_json": gastos_json, "query": query}
    )
