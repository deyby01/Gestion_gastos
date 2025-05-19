from django.shortcuts import render, redirect
from .models import Gasto
from .forms import GastoForm

def index(request):
    if request.method == "POST":
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # Redirige a la página principal después de guardar

    else:
        form = GastoForm()

    gastos = Gasto.objects.all()  # Obtiene todos los gastos guardados
    return render(request, "index.html", {"form": form, "gastos": gastos})