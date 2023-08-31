import socket
import argparse


def add_arg():
    parser = argparse.ArgumentParser(description="-----Help untuk ip_checker-----")

    parser.add_argument(
        "-u", "--url", action="store", help="Opsi untuk menambahkan url atau domain"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="Opsi untuk melihat version",
        version="Versi dari IP Checker ini : 0.1",
    )

    args = parser.parse_args()

    if args.url == None:
        print(
            "Anda harus menambahkan domain dengan cara -u <DOMAIN> atau --url <DOMAIN>, \natau tampilkan HELP dengan menambahkan -h"
        )
    else:
        ip_checker(args.url)


def ip_checker(domain):
    ipv4 = socket.gethostbyname(domain)
    print(f"domain : {domain}")
    print(f"ipv4 : {ipv4}")


if __name__ == "__main__":
    add_arg()
