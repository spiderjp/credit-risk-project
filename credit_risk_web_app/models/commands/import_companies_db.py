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

# Certifique-se de que o índice único existe para a coluna 'name' nas tabelas sector e segment
cursor.execute("""
    CREATE UNIQUE INDEX IF NOT EXISTS unique_sector_name ON sector(name);
    CREATE UNIQUE INDEX IF NOT EXISTS unique_segment_name ON segment(name, sector_id);
""")
conn.commit()

# Função para tratar valores vazios
def clean_value(value):
    if value.strip() == '':
        return None
    return value.strip()

# Abra o CSV com os dados das empresas
with open('../../csv/dados_consolidados_empresas.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Para cada linha no CSV (cada empresa)
    for row in reader:
        company_name = clean_value(row['nome_empresa'])  # Remover espaços extras
        cnpj = clean_value(row['cnpj'])
        ipo_year = clean_value(row['ano_estreia_bolsa'])
        foundation_year = clean_value(row['ano_fundacao'])
        ticker = clean_value(row['ticker'])
        sector_name = clean_value(row['setor'])
        segment_name = clean_value(row['segmento'])
        
        # Tratar o campo de número de funcionários
        employees_number = row['numero_funcionarios'].replace('.', '').replace(',', '').strip()

        # Verificar se o campo é vazio ou não numérico
        if employees_number == '' or not employees_number.isdigit():
            employees_number = None  # Ou outro valor padrão, se necessário
        else:
            employees_number = int(employees_number)

        # Verifique se o nome do setor não está vazio antes de tentar inserir
        if sector_name:
            cursor.execute("SELECT id FROM sector WHERE name = %s", (sector_name,))
            sector_id = cursor.fetchone()

            if not sector_id:
                # Se o setor não existe, insira "Sem Setor definido"
                cursor.execute("INSERT INTO sector (name) VALUES (%s) RETURNING id", ('Sem Setor definido',))
                sector_id = cursor.fetchone()[0]
                conn.commit()
                print(f'Setor "Sem Setor definido" inserido com sucesso!')
            else:
                sector_id = sector_id[0]  # Caso o setor já exista, use o ID existente
        else:
            # Se não houver setor, insira "Sem Setor definido"
            cursor.execute("SELECT id FROM sector WHERE name = %s", ('Sem Setor definido',))
            sector_id = cursor.fetchone()[0]  # Garantir que 'Sem Setor definido' seja inserido corretamente
            conn.commit()
            print(f'Setor "Sem Setor definido" utilizado!')

        # Verifique se o nome do segmento não está vazio antes de tentar inserir
        if segment_name:
            cursor.execute("SELECT id FROM segment WHERE name = %s AND sector_id = %s", (segment_name, sector_id))
            segment_id = cursor.fetchone()

            if not segment_id:
                # Se o segmento não existe, insira "Sem Segmento definido"
                cursor.execute("INSERT INTO segment (name, sector_id) VALUES (%s, %s) RETURNING id", ('Sem Segmento definido', sector_id))
                segment_id = cursor.fetchone()[0]
                conn.commit()
                print(f'Segmento "Sem Segmento definido" inserido com sucesso!')
            else:
                segment_id = segment_id[0]  # Caso o segmento já exista, use o ID existente
        else:
            # Se não houver segmento, insira "Sem Segmento definido"
            cursor.execute("SELECT id FROM segment WHERE name = %s AND sector_id = %s", ('Sem Segmento definido', sector_id))
            segment_id = cursor.fetchone()[0]  # Garantir que 'Sem Segmento definido' seja inserido corretamente
            conn.commit()
            print(f'Segmento "Sem Segmento definido" utilizado!')

        # Agora insira a empresa na tabela company com os IDs de setor e segmento
        cursor.execute("""
            INSERT INTO company (commercial_name, cnpj, ipo_year, employees_number, foundation_year, ticker, sector, segment)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (cnpj) DO NOTHING;  -- Evita duplicação de CNPJ
        """, (company_name, cnpj, ipo_year, employees_number, foundation_year, ticker, sector_id, segment_id))
        
        conn.commit()
        print(f'Empresa "{company_name}" inserida com sucesso!')

# Feche a conexão
cursor.close()
conn.close()
