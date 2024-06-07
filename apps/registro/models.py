from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



class Planta(models.Model):
    planta = models.IntegerField()
    #tipomaquina
    #numeromaquina
    class Meta:
        verbose_name = "Planta"
        verbose_name_plural = "Plantas"

    def __str__(self):
        return str(self.planta)


class Perfil(models.Model):
    choices = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('PA', 'Pasaporte'),
        
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    type_document = models.CharField(max_length=2,blank=True, null=True,choices=choices,default="CC")
    nuip = models.CharField(unique=True, null=True,blank=True,max_length=11)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, null=True, blank=True)
    telefono = models.CharField(blank=True,max_length=10)

    class Meta:
        verbose_name = ("Perfil")
        verbose_name_plural = ("Perfiles")
        
    def __str__(self):
        return f"{self.user} {self.user.username}"


class Reporte(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    
    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
        
    def __str__(self):
        return f"Reporte de {self.perfil.user.username} para {self.planta.planta} el {self.fecha_reporte.strftime('%Y-%m-%d %H:%M:%S')}"
    # models.py


class SolicitudMantenimiento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    maquina = models.CharField(max_length=100)
    averia = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.maquina} - {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}"


    
    
    
    
    

        






























































@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    if instance:
        if Perfil.objects.filter(user=instance.id).exists():
            instance.perfil.save()
        else:
            created = Perfil.objects.create(user=instance)
            created.save()