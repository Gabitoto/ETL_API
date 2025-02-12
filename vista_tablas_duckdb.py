import duckdb
con = duckdb.connect('c:/projects/ETL_API/rest_api_pokemon.duckdb', read_only=True)

try:
    tables = con.execute("""
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_type = 'BASE TABLE';
    """).fetchall()
    print("Tablas encontradas:", tables)
except Exception as e:
    print("Error al listar tablas desde information_schema:", e)

for schema, table in tables:
    try:
        print(f"\nMostrando datos de {schema}.{table}:")
        data = con.execute(f'SELECT * FROM "{schema}"."{table}" LIMIT 5').fetchdf()
        print(data)
    except Exception as e:
        print(f"Error al consultar {schema}.{table}:", e)

for schema, table in tables:
    try:
        export_path = f'c:/projects/ETL_API/backup_{schema}_{table}.csv'
        con.execute(f'''
            COPY (SELECT * FROM "{schema}"."{table}") 
            TO '{export_path}' 
            (HEADER, DELIMITER ',');
        ''')
        print(f"Datos de {schema}.{table} exportados a {export_path}")
    except Exception as e:
        print(f"Error al exportar {schema}.{table}:", e)