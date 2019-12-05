import requests
import sys


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


def port_scanner(self):
    '''Port Scanner'''
    import socket
    from functools import partial
    from multiprocessing import Pool
    from multiprocessing.pool import ThreadPool
    from errno import ECONNREFUSED
    from datetime import datetime

    NUM_CORES = 2 #TODO: Add multiprocessing
    t1 = datetime.now()
    if len(self) != 1:
        return 0
    else:
        ip = socket.gethostbyname(self[0])
        try:
            with open('./src/ports.txt', 'r') as f:
                reader = f.readlines()
                for port in reader:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((ip, int(port)))
                    if result == 0:
                        print(f'Port {int(port)} is Open')
                    sock.close()

        except KeyboardInterrupt:
            print('You stopped the scan')
        except socket.gaierror:
            print('Some problem in this fucker')
            sys.exit()
        except socket.error:
            print(f'{ip} can\'t be resolved')

        t2 = datetime.now()
        total = t2 - t1

        print(f'Scan completed in: {total}')


def submarine(self):
    '''Subdomain BruteForcer'''
    with open('./src/subdomain.txt', 'r') as f:
        reader = f.readlines()
        try:
            for subdomain in reader:
                test_url = f'http://{subdomain.strip()}.{self[0]}'
                get_response = request(test_url)
                if get_response:
                    print(f'[-] Discovered subdomain {test_url}')
        except:
            return 0

def boat(self):
    '''Directory BruteForcer'''
    found = []
    with open('./src/dirb.txt', 'r') as f:
        reader = f.readlines()
        try:
            for dirs in reader:
                test_url = f'http://{self[0]}/{dirs.strip()}'
                get_response = request(test_url)
                if get_response:
                    print(f'[-] Discovered dir {test_url}')
                    found.append(test_url)
            found.remove(found[0])
            if len(found) != 1:
                for url in found:
                    boat(url)

            # TODO: add multi-threading
        except:
            return 0

def social(self):
    '''IP Scanner'''
    import socket
    from datetime import datetime


    def get_ip_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()

    def ping(host):
        try:

            if socket.gethostbyaddr(host):
                return True
            else:
                return False

        except:
            return False

    t1 = datetime.now()
    if len(self) != 0:
        return 0
    else:
        print(f'Hello {socket.gethostname()}, let\'s find your neighbours!')
        try:
            ip = get_ip_address()[0]
            for i in range(0, 255):
                try:
                    check = '.'.join(ip.split('.')[:-1]) + f'.{i}'
                    if ping(check):
                        print(f'[+] Hostname: {socket.gethostbyaddr(check)[0]}, IP: {check}')

                except Exception:
                    pass
            t2 = datetime.now()
            total = t2 - t1

            print(f'Scan completed in: {total}')
            
        except Exception as err:
            print(err)
