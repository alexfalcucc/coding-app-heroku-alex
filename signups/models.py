from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class SignUp(models.Model):
    para_voce = models.BooleanField(default=True, verbose_name="Voce quem fez a compra? Se sim, marque a caixa:")
    nome = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    horario = models.DateTimeField(auto_now_add=True, auto_now=False)
    atualizado = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.email)