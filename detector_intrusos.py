try:
    import nmap
except ImportError:
    raise ImportError('Modulo nmap no instalado, prueba: pip install python-nmap')


nm = nmap.PortScanner()

ip_range = raw_input("Inserta rango de IPs, por defecto 192.168.1.0/24\n>")

if ip_range == "":
    ip_range = '192.168.1.0/24'

print("Realizando scan, puede tomar un momento...\n")

nm.scan(hosts = ip_range, arguments = '-PT -T5')

print('\nMostrando los dispositivos conectados a su red:\n')

result = str(nm.all_hosts())
print(result)



while True:

    opt = raw_input("\nOpciones:\n[1]\tGuardar en fichero\n[2]\tComparar con IPs guardadas\n[3]\tSalir\n>")
    
    
    if opt == "1":
        fich = raw_input("Inserta nombre del fichero:\n>")
        
        fich_esc = open(fich, 'w')

        fich_esc.write(result)

        fich_esc.close()

    elif opt == "2":
        fich = raw_input("Inserta nombre del fichero:\n>")

        fich_lec = open(fich, 'r')

        print("\nEstos son sus dispositivos guardados, si hay una IP que desconoce \ncon respecto al resultado anterior puede tratarse de un intruso en su red:\n")
        print(fich_lec.readlines())

        fich_lec.close()

    elif opt == "3":
        exit()
    


