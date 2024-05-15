import subprocess
import re
import socket
import requests
import sys
from prettytable import PrettyTable


def resolve_hostname(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        print("Ошибка: Не удалось разрешить доменное имя в IP-адрес.")
        sys.exit(1)


def traceroute(destination):
    command = ['tracert', '-w', '100', destination]
    trace = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='cp866')

    output = ''
    try:
        while trace.poll() is None:
            line = trace.stdout.readline()
            if line:
                print(line.strip())
                output += line
    except subprocess.TimeoutExpired:
        trace.kill()
        print("Ошибка: Превышено время ожидания ответа от хоста.")
    return output


def get_as_number(ip):
    try:
        response = requests.get(f"https://api.iptoasn.com/v1/as/ip/{ip}")
        response_data = response.json()
        return response_data.get('as_number', 'Unavailable')
    except requests.exceptions.RequestException:
        print(f"Ошибка: Невозможно получить AS для IP {ip}.")
        return "Unavailable"


def parse_traceroute(output):
    ip_pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
    ips = ip_pattern.findall(output)
    return ips


def main():
    hostname = input("Введите доменное имя или IP-адрес: ")
    if not re.match(r'^\d+\.\d+\.\d+\.\d+$', hostname):
        destination = resolve_hostname(hostname)
    else:
        destination = hostname

    trace_output = traceroute(destination)
    trace_ips = parse_traceroute(trace_output)

    table = PrettyTable()
    table.field_names = ["№", "IP", "AS"]

    for idx, ip in enumerate(trace_ips, 1):
        as_number = get_as_number(ip)
        table.add_row([idx, ip, as_number])

    print(table)


if __name__ == "__main__":
    main()