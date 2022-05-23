import socket


def scan_ip(site, exibir_portas_fechas=False, velocidade_scan=2):

    portas = [20, 21, 22, 23, 42, 43, 43, 69, 80, 109, 110,
              115, 118, 143,156, 220, 389, 443, 465, 513, 514,
              530, 547, 587, 636, 873,989, 990, 992, 993, 995,
              1433, 1521, 2049, 2081, 2083, 2086,3306, 3389, 5432,
              5500, 5800]

    for porta in portas:
        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(velocidade_scan)
            resultado = cliente.connect_ex((site,porta))
        except Exception as erro:
            print(f'Ocorreu um erro: {erro}')
            break
        else:
            if exibir_portas_fechas:
                if resultado == 0:
                    print(porta, "OPEN")
                else:
                    print(porta, "CLOSE")
            else:
                if resultado == 0:
                    print(porta, "OPEN")


if __name__ == '__main__':

    print('=' * 40)
    print('Scanner de Porta'.center(40))
    print('=' * 40,'\n')
    while True:
        try:
            site = str(input("Site: "))
        except KeyboardInterrupt:
            print('\nusuario interronpeu o programa')
            quit()
        except:
            print('Erro tente novamente...')
        else:
            break
    while True:
        try:
            exibir = str(input("Deseja ver portas fechadas [S/N]: ")).upper()
        except KeyboardInterrupt:
            print('\nusuario interronpeu o programa')
            quit()
        except:
            print('Erro tente novamente...')
        else:
            break
    while True:
        try:
            velocidade = float(input("Digite a velocidade do scan: "))
        except KeyboardInterrupt:
            print('\nusuario interronpeu o programa')
            quit()
        except:
            print('Erro tente novamente...')
        else:
            break
    print('=' * 40)
    if exibir == 'S':
        scan_ip(site,True,velocidade)
    elif exibir == 'N':
        scan_ip(site,False,velocidade)
    else:
        scan_ip(site, False, velocidade)
