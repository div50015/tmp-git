import nmap


nm = nmap.PortScanner()
# nm.scan(hosts="10.30.92.0/24", arguments='-min-rtt-timeout 100ms -sP')
#
# for host in nm.all_hosts():
#     print(host)


try:
    nm.scan(hosts='10.30.92.0/24', arguments='-sP')
    [print(host) for host in nm.all_hosts()]
    print("********************\r\n")
except Exception as e:
    print(type(e))

