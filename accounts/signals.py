from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role

@receiver(post_save, sender=Users)
def define_perm(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == "S":
            assign_role(instance, 'secretaria')
        elif instance.cargo == "M":
            assign_role(instance, 'medico')
        elif instance.cargo == "P":
            assign_role(instance, 'paciente')