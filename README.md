# ETL_API
Proceso de ETL desde una API a una base de datos.


## Tecnologias usadas:
-DLT
-Duckdb

## Flujo de datos:

Extracción (Extract):

GitHub (github_source):
Se conecta a la API de GitHub usando un token de acceso (si está disponible).
Extrae datos de los issues abiertos y sus comentarios asociados.
Implementa carga incremental para los issues usando el campo updated_at.
PokéAPI (pokemon_source):
Se conecta a la API de Pokémon.
Extrae datos de recursos como pokemon, berry, y location.
Soporta paginación automática si la API lo requiere.

Transformación (Transform):

Se configuran parámetros como primary_key, write_disposition (para definir si se fusionan o reemplazan datos), y relaciones entre recursos (por ejemplo, comentarios vinculados a issues).

Carga (Load):

Los datos extraídos y transformados se cargan en DuckDB, una base de datos embebida, usando pipelines de DLT.
Cada API tiene su propio pipeline: rest_api_github y rest_api_pokemon.

Validación de Conexiones (Opcional):

Se verifica la conectividad de la API de Pokémon mediante check_connection antes de la carga.
Este flujo permite automatizar la ingesta de datos desde APIs REST hacia un entorno analítico, facilitando el manejo de actualizaciones incrementales y relaciones entre recursos.
