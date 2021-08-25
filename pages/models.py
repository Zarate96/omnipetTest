from django.db import models

# Create your models here.

class Ciudades(models.Model):
    nombre = models.CharField(max_length=30)
    unique = True

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Ciudades"

door_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    )

class Zonas(models.Model):
    min = models.IntegerField()
    max = models.IntegerField()
    categoria = models.CharField(choices=door_choices, max_length=10)
    unique = True

    def __str__(self):
        return self.categoria
    
    class Meta:
        verbose_name_plural = "Zonas"

class Distancias(models.Model):
    ciudad1 = models.ForeignKey(Ciudades, on_delete=models.CASCADE, related_name='ciudad1')
    ciudad2 = models.ForeignKey(Ciudades, on_delete=models.CASCADE, related_name='ciudad2')
    distancia = models.IntegerField()
    unique = True
    
    def __str__(self):
        return f'{self.ciudad1.nombre} a {self.ciudad2.nombre} {self.distancia}km '
    
    class Meta:
        verbose_name_plural = "Distancias"

class Proveedores(models.Model):
    nombre = models.CharField(max_length=30)
    unique = True
    
    def __str__(self):
        return f'{self.nombre}'
    
    class Meta:
        verbose_name_plural = "Proveedores"

kg_choices = (
    (1, 1),
    (5, 5),
    (10, 10),
    (15, 15),
    (20, 20),
    (25, 25),
    (30, 30),
    (35, 35),
    (40, 40),
    (45, 45),
    (50, 50),
    (60, 60),
    (70, 70),
)

class Tarifas(models.Model):
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    kg = models.IntegerField(choices=kg_choices)
    zona = models.ForeignKey(Zonas, on_delete=models.CASCADE)
    precio = models.FloatField(null=True)
    unique = True
    
    def __str__(self):
        return f'{self.kg} kg  {self.zona} zona {self.precio} $ {self.proveedor.nombre}'
    
    class Meta:
        verbose_name_plural = "Tarifas"