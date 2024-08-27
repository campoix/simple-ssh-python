import paramiko
import time

def ssh_exec_command(hostname, port, username, password, command, frequency):
    # Cria uma instância SSHClient
    client = paramiko.SSHClient()
    # Carrega as chaves do sistema
    client.load_system_host_keys()
    # Adiciona a chave do host se ausente
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conecta ao servidor SSH
        client.connect(hostname, port=port, username=username, password=password)

        while True:
            # Solicita a frequência de execução
            frequency = int(input("Quantas vezes por segundo o comando deve ser executado? "))

            # Executa o comando no servidor remoto
            stdin, stdout, stderr = client.exec_command(command)
            print("Saída do comando:")
            print(stdout.read().decode())

            # Aguarda o intervalo de tempo especificado
            time.sleep(1 / frequency)

    except paramiko.AuthenticationException:
        print("Falha na autenticação. Verifique suas credenciais.")
    except paramiko.SSHException as e:
        print(f"Falha na conexão SSH: {e}")
    finally:
        # Fecha a conexão SSH
        client.close()

# Substitua os valores abaixo pelos seus próprios dados
hostname = 'host'
port = 22  # porta padrão SSH
username = 'user'
password = 'pass'
command = 'ls'  
frequency = 1   

# Chama a função
ssh_exec_command(hostname, port, username, password, command, frequency)
