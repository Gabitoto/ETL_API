import requests 
from bs4 import BeautifulSoup

API_KEY = "TU_API_KEY"
URL = "https://boxrec.com/en/ratings"  # Reemplazá con la URL real

# Construimos la URL de la API con la página objetivo
api_url = f"https://api.webscraping.ai/html?api_key={API_KEY}&url={URL}"

# Hacemos la petición GET
response = requests.get(api_url)

# Verificamos si la respuesta es válida
if response.status_code == 200:
    html_content = response.text  # Obtenemos el HTML
    print(html_content)  # Podemos inspeccionar el contenido
else:
    print(f"Error: {response.status_code}")

# Analizar el contenido HTML de la página
soup = BeautifulSoup(response.content, 'html.parser')

# Aquí podrías buscar la tabla, por ejemplo:
table = soup.find('table')  # Ajusta el selector según sea necesario

# Imprimir el contenido de la tabla
print(table)