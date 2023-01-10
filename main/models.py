from django.db import models
import datetime

class Cliente(models.Model):
    WHATS = (
        ('S', 'Sim'),
        ('N', 'Não')
    )
    
    nome = models.CharField(max_length=50, blank=False, null= False)
    telefone = models.IntegerField()
    whatsapp = models.CharField(max_length=1,choices=WHATS, null=False, blank=False, default='S')

    def __str__(self):
        return self.nome

class Servico(models.Model):
    descricao = models.CharField(max_length=30)
    valor = models.IntegerField()

    def __str__(self):
        return self.descricao

class Agendamento(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_cobrado = models.IntegerField()
    data = models.DateTimeField()


    def __str__(self):
        return self.cliente