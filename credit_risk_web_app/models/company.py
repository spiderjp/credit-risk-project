# Importação do módulo models para criar os modelos com suas respectivas classes e funções
from django.db import models



# Criação do Modelo para a Tabela Empresa
class Company(models.Model):

    # Criação dos campos do Modelo que serão transformados em campos da Tabela
    id = models.AutoField(primary_key=True)  # ID único da empresa (chave primária)
    
    commercial_name = models.CharField(max_length=255)  # Nome comercial (já existente)
    
    cnpj = models.CharField(max_length=18, unique=True)  # CNPJ (formato: 00.000.000/0000-00)
    
    ipo_year = models.PositiveIntegerField(null=True, blank=True)  # Ano de estreia na bolsa
    
    employees_number = models.PositiveIntegerField(null=True, blank=True)  # Número de funcionários
    
    foundation_year = models.PositiveIntegerField(null=True, blank=True)  # Ano de fundação
    
    ticker = models.CharField(max_length=20, unique=True)  # Código de negociação na bolsa
    
    sector = models.CharField(max_length=255)  # Setor de atuação
    
    segment = models.CharField(max_length=255)  # Segmento dentro do setor

    # Definição de como a instância do modelo será representada nas impressões e Django shell
    def __str__(self):
        return self.commercial_name
    
    class Meta:
        db_table = 'company'  # Explicitando o nome da tabela
    