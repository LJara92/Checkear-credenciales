from netmiko import ConnectHandler
from paramiko import AuthenticationException, SSHException
import configparser

credenciales = "C:\Users\Lautaro\Code"

def scan_single_ip(device_ip):
    # Leer credenciales desde el archivo de configuración
    config = configparser.ConfigParser()
    config.read(credenciales)
    
    # Lista de usuarios y contraseñas a probar
    users = config.get('Credenciales', 'usuarios').split(',')
    key = config.get('Credenciales', 'passwords').split(',')

    device = {
        'device_type': 'cisco_ios',  # Cambia el tipo de dispositivo según tu caso
        'ip': device_ip,  # Cambia la dirección IP al equipo SSH
    }

    # Variable para controlar la ejecución del bucle
    credenciales_correctas = False

    # Intenta cada combinación de usuario y contraseña
    for user in users:
        for password in key:
            device['username'] = user
            device['password'] = password

            try:
                # Intenta conectar con las credenciales actuales
                with ConnectHandler(**device) as ssh_session:
                    print(f"\nConexión exitosa en la IP: {device_ip} con {user}/{password}")
                    credenciales_correctas = True
                    # Guardar las credenciales en el archivo
                    save_credentials_to_file(device_ip, user, password)
            except (AuthenticationException, SSHException) as e:
                print(f"Fallo de autenticación en la IP: {device_ip} con {user}/{password}")

            if credenciales_correctas:
                break  # Sale del bucle interno si las credenciales son correctas

        if credenciales_correctas:
            break  # Sale del bucle externo si las credenciales son correctas
    print("Prueba de credenciales completada. Se genero el archivo IPs.txt con las credenciales")

def save_credentials_to_file(ip, user, password):
    with open("IPs.txt", "a") as file:
        file.write(f"IP: {ip}\t Usuario: {user}\t Contraseña: {password}\n")

def scan_multiple_ips(device_ips):
    # Leer credenciales desde el archivo de configuración
    config = configparser.ConfigParser()
    config.read(credenciales)

    # Lista de usuarios y contraseñas a probar
    users = config.get('Credenciales', 'usuarios').split(',')
    key = config.get('Credenciales', 'passwords').split(',')

    # Intenta cada combinación de usuario y contraseña
    for ip in device_ips:
        device = {
            'device_type': 'cisco_ios',  # Cambia el tipo de dispositivo según tu caso
            'ip': ip,  # Cambia la dirección IP al equipo SSH
        }

        # Variable para controlar la ejecucion del bucle
        credenciales_correctas = False

        print("\n")
        for user in users:
            for password in key:
                device['username'] = user
                device['password'] = password

                try:
                    # Intenta conectar con las credenciales actuales
                    with ConnectHandler(**device) as ssh_session:
                        print(f"\nConexión exitosa en la IP: {ip} con {user}/{password}")
                        credenciales_correctas = True
                        # Guardar las credenciales en el archivo
                        save_credentials_to_file(ip, user, password)
                        break  # Sale del bucle interno si las credenciales son correctas
                except (AuthenticationException, SSHException) as e:
                    print(f"Fallo de autenticación en la IP: {ip} con {user}/{password}")

            if credenciales_correctas:
                break  # Sale del bucle externo si las credenciales son correctas
        if credenciales_correctas == False:
            print("\nFallo de autenticacion, ninguna credencial valida")

    print("\nPrueba de credenciales completa")

def menu():
    while True:
        print("\n----- Menú -----")
        print("1. Escanear una sola IP")
        print("2. Escanear varias IPs")
        print("0. Salir")

        choice = input("Selecciona una opción (0-2): ")

        if choice == '1':
            ip_to_scan = input("Ingresar la IP del equipo a verificar: ")
            scan_single_ip(ip_to_scan)
        elif choice == '2':
            ips_to_scan = input("Ingresar las IPs separadas por comas: ")
            ips_list = [ip.strip() for ip in ips_to_scan.split(',')]
            scan_multiple_ips(ips_list)
        elif choice == '0':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 2 o 0 para salir")

menu()