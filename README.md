# User Authentication Branch

Este branch está dedicado a implementar la autenticación de usuario en el proyecto. Se incluirán características como el registro de usuarios, inicio de sesión y autenticación por token para la API.

## Características

1. **Registro de usuarios**: Permitir a nuevos usuarios registrarse en la plataforma con validación de datos.
2. **Inicio de sesión**: Autenticación de usuario y manejo de sesiones.
3. **Autenticación por token**: Habilitar autenticación basada en tokens para la API (para integrarse con aplicaciones móviles o clientes externos).

## Tecnologías

- **Django**: Framework principal para el desarrollo.
- **Django REST Framework**: Para la creación de endpoints de autenticación en la API.
- **Simple JWT** (opcional): Paquetes para manejar autenticación basada en tokens.

## Configuración e Instalación

1. **Clona el repositorio y cambia al branch de autenticación**:

    ```bash
    git clone <URL-del-repositorio>
    cd <nombre-del-proyecto>
    git checkout user-auth
    ```

2. **Crea y activa el entorno virtual**:

    ```bash
    python -m venv venv
    venv\Scripts\activate     # Windows
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configura las variables de entorno**:

    Crea un archivo `.env` en la raíz del proyecto e incluye tus claves secretas, configuraciones de base de datos y otros valores sensibles. Asegúrate de agregar al menos:

    ```plaintext
    SECRET_KEY=<tu-clave-secreta>
    DEBUG=True
    ```

5. **Ejecuta las migraciones** para crear la estructura de base de datos necesaria:

    ```bash
    python manage.py migrate
    ```

6. **Inicia el servidor de desarrollo**:

    ```bash
    python manage.py runserver
    ```

## Endpoints de Autenticación (API)

- **Registro de usuario**: `POST /api/auth/register/`
- **Inicio de sesión**: `POST /api/auth/login/`
- **Cierre de sesión**: `POST /api/auth/logout/`
- **Restablecimiento de contraseña**: `POST /api/auth/password-reset/`
- **Autenticación por token**: `POST /api/auth/token/`

## Testing

Para asegurarse de que los endpoints de autenticación funcionen correctamente, ejecuta las pruebas de la aplicación con el siguiente comando:

```bash
python manage.py test

