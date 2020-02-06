def ping(address):
    import os
    while True:
        response = os.system('ping -n 1 {} | find /c "ms"'.format(address))
        if response == 0:
            print('Connected')
            break
            
address = '192.168.1.2' #example
ping(address)
