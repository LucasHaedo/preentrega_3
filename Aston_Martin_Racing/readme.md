Este es un proyecto Django que incluye las siguientes características:

- Modelos para `Car`, `Customer` y `Sale`
- Herencia HTML usando una plantilla `base.html`
- Formularios para crear objetos `Car`, `Customer` y `Sale` y para buscar en la base de datos
- Vistas para mostrar los formularios y manejar el envío de formularios

Para configurar y probar este proyecto, sigue estos pasos:

1. Instala las dependencias requeridas ejecutando `pip install -r requirements.txt`.
2. Ejecuta las migraciones de la base de datos ejecutando `python manage.py migrate`.
3. Inicia el servidor de desarrollo ejecutando `python manage.py runserver`.
4. Abre tu navegador web y navega a `http://localhost:8000/` para acceder al sitio.
5. Prueba las diferentes funcionalidades siguiendo los enlaces y rellenando los formularios.

El orden en el que se deben probar las cosas es el siguiente:

1. Crea un objeto `Car` navegando a `/car/create/` y rellenando el formulario.
2. Crea un objeto `Customer` navegando a `/customer/create/` y rellenando el formulario.
3. Crea un objeto `Sale` navegando a `/sale/create/` y rellenando el formulario.
4. Busca en la base de datos navegando a `/search/` y rellenando el formulario.

Las diferentes funcionalidades se encuentran en las siguientes URLs:

- `/car/create/`: Crear un objeto `Car`
- `/customer/create/`: Crear un objeto `Customer`
- `/sale/create/`: Crear un objeto `Sale`
- `/search/`: Buscar en la base de datos
