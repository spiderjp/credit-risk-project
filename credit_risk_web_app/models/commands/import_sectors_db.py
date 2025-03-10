import psycopg2
from dotenv import load_dotenv
import os
import csv

# Carregue as variáveis de ambiente do arquivo .env
load_dotenv()

# Conecte-se ao banco de dados PostgreSQL diretamente
conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'), 
    user=os.getenv('DB_USER'), 
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)
cursor = conn.cursor()

# Certifique-se de que o índice único existe para a coluna 'name'
cursor.execute("""
    CREATE UNIQUE INDEX IF NOT EXISTS unique_sector_name ON sector(name);
""")
conn.commit()

# Abra o CSV com os dados dos setores
with open('../../csv/setores_unicos.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Para cada setor no CSV
    for row in reader:
        sector_name = row['setor'].strip()  # Remover espaços extras
        
        if sector_name:  # Verifica se o setor não está vazio
            try:
                # Insira o setor no banco de dados diretamente
                cursor.execute(
                    "INSERT INTO sector (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;", 
                    (sector_name,)
                )
                conn.commit()
                print(f'Setor "{sector_name}" importado com sucesso!')
            except Exception as e:
                # Em caso de erro, faz o rollback da transação e imprime o erro
                conn.rollback()
                print(f'Erro ao importar o setor "{sector_name}": {e}')

# Feche a conexão
cursor.close()
conn.close()
