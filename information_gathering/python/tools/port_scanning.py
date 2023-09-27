import socket


target_host = input("Masukkan alamat IP target: ")
spam = input('Apa anda mau spam aja? : ')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    while True:
        if spam.lower() in ('n', 'no'):
            target_port = int(input("Masukkan port target: "))
            result = client.connect_ex((target_host, target_port))
            if result == 0:
                print(f"Port {target_port} terbuka pada {target_host}")
            else:
                print(f"Port {target_port} tertutup pada {target_host}")
            break
        elif spam.lower() in ('y', 'yes'):
            min_port = int(input("Masukkan min port target: "))
            max_port = int(input("Masukkan max port target: "))

            port_range = range(min_port, max_port)
            # timeout = 2
            for port in port_range:
                result = client.connect_ex((target_host, port))
                if result == 0:
                    print(f"Port {port} terbuka pada {target_host}")
                else:
                    print(f"Port {port} tertutup pada {target_host}")

            break
        else:
            print("ketik y/n")

