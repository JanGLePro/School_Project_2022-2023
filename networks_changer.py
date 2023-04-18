import os
os.system('chcp 1251')

def out_all_networks():
    mas = []
    output = os.popen('netsh wlan show profiles').read()
    for item in output.split('\n'):
        item = list(item.split(': '))
        if len(item) == 1:
            continue
        title = item[-1]
        mas.append(title)
    return mas


def connect_network(title):
    os.system(f'netsh wlan connect name="{title}"')
connect_network(out_all_networks()[2])
