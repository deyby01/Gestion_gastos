from django.db import models

# Create your models here.
class Gasto(models.Model):
    CATEGORIAS = [
        ("Alimentación", "Alimentación"),
        ("Transporte", "Transporte"),
        ("Entretenimiento", "Entretenimiento"),
        ("Salud", "Salud"),
        ("Otros", "Otros"),
    ]
    
    nombre = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default="Otros")

    def __str__(self):
        return f"{self.nombre} (${self.monto}) - {self.categoria}"
