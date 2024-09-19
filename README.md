# API de Investigación con GPT

Esta API utiliza FastAPI y GPTResearcher para generar informes basados en consultas de usuario.

## Requisitos

- Python 3.11
- Docker
- Docker Compose

## Configuración

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```

2. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
   ```
   OPENAI_API_KEY=tu_clave_api_de_openai
   TAVILY_API_KEY=tu_clave_api_de_tavily
   API_KEY=tu_clave_api_personalizada
   ```

## Ejecución con Docker

1. Construye y ejecuta el contenedor:
   ```
   docker-compose up --build -d
   ```

2. La API estará disponible en `http://localhost:5001`

## Uso

Para hacer una petición a la API:

```
curl -X GET "http://localhost:5001/report/resumen?query=Tu%20Consulta%20Aquí" \
-H "api-key: tu_clave_api_personalizada" \
-H "Content-Type: application/json"
```


Reemplaza `Tu%20Consulta%20Aquí` con tu consulta codificada en URL y `tu_clave_api_personalizada` con la clave API que configuraste en el archivo `.env`.

## Desarrollo

Para desarrollar localmente sin Docker:

1. Crea un entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```
   uvicorn main:app --reload --port 5001
   ```

## Contribuir

Si deseas contribuir a este proyecto, por favor:

1. Haz un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.