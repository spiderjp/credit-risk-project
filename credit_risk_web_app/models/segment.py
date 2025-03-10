# Importação do módulo models para criar os modelos com suas respectivas classes e funções
from django.db import models
from .sector import Sector



# Criação do Modelo para a Tabela Subsetor
class Segment(models.Model):

    # Criação dos campos do Modelo que serão transformados em campos da Tabela

    # Uso de Chave Estrangeira para relacionar os modelos (tabelas) Subsector e Sector
    # on_delete define o comportamento do subsector quando o sector é excluído (todos os subsectores associados são excluídos)
    # related_name é o nome da relação reversa entre os dois modelos (tabelas)

    id = models.AutoField(primary_key=True)  # ID único do setor

    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='segments') # Setor do segmento

    name = models.CharField(max_length=255) # Nome do segmento

    # Definição de como a instância do modelo será representada nas impressões e Django shell
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'segment'  # Explicitando o nome da tabela