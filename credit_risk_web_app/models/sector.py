# Importação do módulo models para criar os modelos com suas respectivas classes e funções
from django.db import models
    
 
 
# Criação do Modelo para a Tabela Setor
class Sector(models.Model):

    # Criação do campo do Modelo que será transformado em campo da Tabela
    id = models.AutoField(primary_key=True)  # ID único do setor

    name = models.CharField(max_length=255) # Nome do setor

    # Definição de como a instância do modelo será representada nas impressões e Django shell
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'sector'  # Explicitando o nome da tabela