# Checkear-credenciales
Este proyecto consiste en un script de Python que realiza un escaneo de credenciales SSH en dispositivos con sistema operativo Cisco IOS. Utiliza la biblioteca `netmiko` para la conexión SSH y la biblioteca `paramiko` para manejar excepciones de autenticación.

## Requisitos

- Python 3.x
- Las bibliotecas `netmiko` y `paramiko`. Puedes instalarlas utilizando pip:

```bash
pip install netmiko paramiko
```

## Uso

1. Clona este repositorio en tu máquina local:

  ```bash
  git clone https://github.com/tu_usuario/nombre_del_repositorio.git
  ```

2. Navega al directorio del proyecto:

  ```bash
  cd nombre_del_repositorio
  ```
3. Dentro del codigo "Creck_Credenciales.py edita la ruta donde tengas tu archivo "credenciales.ini"

[!IMPORTANT]
#Modificar ruta, poner la ruta donde este el archivo con las credenciales

#Descomentar acorde a tu sistema operativo
**# Windows #** credenciales = "C:\\Users\\ljara\\Downloads\\Code\\credenciales.ini" 
**# Linux #** credenciales = "/home/ljara/code/credenciales.ini"


4. Ejecuta el script `scan_ssh_credentials.py`:

  ```bash
  python scan_ssh_credentials.py
  ```

5. Sigue las instrucciones del menú para seleccionar la opción deseada:
  - Escanear una sola IP.
  - Escanear varias IPs.

## Configuración

Antes de ejecutar el script, asegúrate de configurar las credenciales en el archivo `config.ini`. Puedes seguir el formato proporcionado en `config_example.ini`.

## Contribuir

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama con tus cambios: `git checkout -b mi_rama`.
3. Realiza tus cambios y haz commit: `git commit -am "Descripción de tus cambios"`.
4. Haz push a la rama: `git push origin mi_rama`.
5. Crea un pull request en GitHub.

## Agradecimientos

- Este proyecto utiliza la biblioteca `netmiko` desarrollada por Kirk Byers ([@ktbyers](https://github.com/ktbyers)).
