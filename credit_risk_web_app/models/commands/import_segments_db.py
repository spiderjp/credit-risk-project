import csv
import psycopg2
from dotenv import load_dotenv
import os

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

# Abrir o arquivo CSV com os dados dos setores e segmentos
with open('../../csv/setores_segmentos.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Para cada linha no CSV
    for row in reader:
        sector_name = row['setor'].strip()  # Remover espaços extras
        segment_name = row['segmento'].strip()  # Remover espaços extras
        
        if sector_name and segment_name:
            try:
                # Verificar se o setor já existe
                cursor.execute("SELECT id FROM sector WHERE name = %s", (sector_name,))
                sector = cursor.fetchone()
                
                if sector:
                    # Se o setor existe, insira o segmento
                    cursor.execute(
                        """
                        INSERT INTO segment (name, sector_id)
                        VALUES (%s, %s)
                        ON CONFLICT (name, sector_id) DO NOTHING;
                        """, 
                        (segment_name, sector[0])
                    )
                    conn.commit()
                    print(f'Segmento "{segment_name}" do setor "{sector_name}" importado com sucesso!')
                else:
                    print(f'Setor "{sector_name}" não encontrado no banco de dados!')
            except Exception as e:
                conn.rollback()
                print(f'Erro ao importar o segmento "{segment_name}" do setor "{sector_name}": {e}')

# Fechar a conexão
cursor.close()
conn.close()
