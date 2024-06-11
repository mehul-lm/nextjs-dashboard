'''
Next
  
'''

import subprocess
import json
import platform
import socket
import os
from netifaces import *


class lmutil:

    command = "lmutil"
    card_type = "card"
    card_format = "--json"
    card_options = None

    def compose(self, card_id, command):
        if type(command) is not list:
            command = [command]
        base = [self.command, self.card_format]
        if self.card_options != None and self.card_options != "":
            base.append(self.card_options)
        if card_id is None:
            pass
        else:
            base.extend([self.card_type, str(card_id)])
        base.extend(command)

        return (base)

    def send(self, card_id, command):
        try:
            out_data = subprocess.check_output(self.compose(card_id, command))
            return (0, json.loads(out_data))
        except FileNotFoundError as e:
            return (-1, (f'Error: {self.command} not found'))
        except subprocess.CalledProcessError as e:
            return (-2, (f'{self.command} returned {e.returncode}, {e.output.decode()}'))

    def __init__(self):
        os_name = platform.system()
        if os_name == 'Linux':
            self.command = "./lmutil"
            self.card_options = "--dbga"
        elif os_name == 'Darwin':
            self.command = "./lmutil"
            self.card_options = "--dbga"
        elif os_name == 'Windows':
            print("Windows not supported")
            exit(1)
        else:
            print(f'Unknown OS {os_name}')
            exit(1)


    def hostname(self):
        hostname = platform.node()
        hostname = socket.gethostname()
        return (hostname)

    def hostIPs(self):
        ips = {}
        for ifaceName in interfaces():
            addrs = ifaddresses(ifaceName)
            # AF_INET=2, AF_LINK=18, AF_INET6=30)
            if AF_INET in addrs:
                addr = ifaddresses(ifaceName).setdefault(AF_INET)[0]['addr']
                if not addr.startswith(("127.0", "169.254")):
                    ips[ifaceName] = addr
        return (ips)

    def hostMACs(self):
        macs = {}
        for ifaceName in interfaces():
            addrs = ifaddresses(ifaceName)
            if AF_LINK in addrs:
                mac = ifaddresses(ifaceName).setdefault(AF_LINK, 'Unknown')[0]['addr']
                if AF_INET in addrs:
                    addr = ifaddresses(ifaceName).setdefault(AF_INET, 'None')[0]['addr']
                else:
                    addr = 'None'
                macs[mac] = addr
        return (macs)

    def cards(self):
        rc, json_data = self.send(None, "cards")
        return rc, json_data

    def time_get(self, card_id):
        rc, json_data = self.send(card_id, ["time", "get"])
        return rc, json_data

    def logging_get(self, card_id):
        rc, json_data = self.send(card_id, ["logging", "get"])
        return rc, json_data

    def alerts(self, card_id):
        rc, json_data = self.send(card_id, "alerts")
        return rc, json_data

    def version(self, card_id):
        rc, json_data = self.send(card_id, "version")
        return rc, json_data

    def fru_get(self, card_id):
        rc, json_data = self.send(card_id, ["fru", "get"])
        return rc, json_data
    
    def test_point(self, card_id):
        rc, json_data = self.send(card_id, ["test_point", "get"])
        return rc, json_data
    
    def cst_get(self, card_id):
        rc, json_data = self.send(card_id, ["cst", "get"])
        return rc, json_data

    def datastore_system(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "system"])
        return rc, json_data

    def datastore_io_0(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "envise", "0"])
        return rc, json_data

    def datastore_io_1(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "envise", "1"])
        return rc, json_data

    def datastore_temp(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "temp"])
        return rc, json_data

    def datastore_power(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "power"])
        return rc, json_data

    def datastore_laser(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "laser", "all", "config"])
        return rc, json_data
    
    def datastore_laser_0_telemetry(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "laser", "0", "telemetry"])
        return rc, json_data
    
    def datastore_laser_1_telemetry(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "laser", "1", "telemetry"])
        return rc, json_data
    
    def datastore_laser_2_telemetry(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "laser", "2", "telemetry"])
        return rc, json_data
    
    def datastore_laser_3_telemetry(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "laser", "3", "telemetry"])
        return rc, json_data
    
    def datastore_laser_0_version(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "laser", "0", "version"])
        return rc, json_data
    
    def datastore_laser_1_version(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "laser", "1", "version"])
        return rc, json_data
    
    def datastore_laser_2_version(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "laser", "2", "version"])
        return rc, json_data
    
    def datastore_laser_3_version(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "laser", "3", "version"])
        return rc, json_data

    def datastore_perf(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "perf"])
        return rc, json_data
    
    def datastore_pcie(self, card_id):
        rc, json_data = self.send(card_id, ["datastore", "pcie"])
        return rc, json_data
    
    def datastore_lmdb_b(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "b"])
        return rc, json_data
    
    def datastore_lmdb_c(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "c"])
        return rc, json_data

    def datastore_lmdb_d(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "d"])
        return rc, json_data
    
    def datastore_lmdb_e(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "e"])
        return rc, json_data
    
    def datastore_lmdb_f(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "f"])
        return rc, json_data
    
    def datastore_lmdb_h(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "h"])
        return rc, json_data
    
    def datastore_lmdb_l(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "l"])
        return rc, json_data
    
    def datastore_lmdb_m(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "m"])
        return rc, json_data
    
    def datastore_lmdb_p(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "p"])
        return rc, json_data
    
    def datastore_lmdb_s(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "s"])
        return rc, json_data
    
    def datastore_lmdb_t(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "t"])
        return rc, json_data
    
    def datastore_lmdb_u(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "u"])
        return rc, json_data
    
    def datastore_lmdb_v(self, card_id):
        rc, json_data = self.send(card_id, ["lmdb", "v"])
        return rc, json_data

def test():

    lm = lmutil()

    hostname = lm.hostname()
    hostIP = lm.hostIPs()
    hostMACs = lm.hostMACs()

    print(f'hostname="{hostname}"')
    print(f'hostIP={hostIP}')
    # for mac in hostMACs:
    #     print(f'MAC={mac}, IP={hostMACs[mac]}')
    print(f'hostMACs={hostMACs}')

    rc, data = lm.cards()
    print(rc, data)

    rc, data = lm.time_get(0)
    print(rc, data)

    rc, data = lm.logging_get(0)
    print(rc, data)

    rc, data = lm.alerts(0)
    print(rc, data)

    rc, data = lm.version(0)
    print(rc, data)

    rc, data = lm.fru_get(0)
    print(rc, data)

    rc, data = lm.test_point(0)
    print(rc, data)

    rc, data = lm.cst_get(0)
    print(rc, data)

    rc, data = lm.datastore_system(0)
    print(rc, data)

    rc, data = lm.datastore_io_0(0)
    print(rc, data)

    rc, data = lm.datastore_io_1(0)
    print(rc, data)

    rc, data = lm.datastore_temp(0)
    print(rc, data)

    rc, data = lm.datastore_laser(0)
    print(rc, data)

    rc, data = lm.datastore_laser_0_telemetry(0)
    print(rc, data)

    rc, data = lm.datastore_laser_1_telemetry(0)
    print(rc, data)

    rc, data = lm.datastore_laser_2_telemetry(0)
    print(rc, data)

    rc, data = lm.datastore_laser_3_telemetry(0)
    print(rc, data)

    rc, data = lm.datastore_laser_0_version(0)
    print(rc, data)

    rc, data = lm.datastore_laser_1_version(0)
    print(rc, data)

    rc, data = lm.datastore_laser_2_version(0)
    print(rc, data)

    rc, data = lm.datastore_laser_3_version(0)
    print(rc, data)

    rc, data = lm.datastore_power(0)
    print(rc, data)

    rc, data = lm.datastore_perf(0)
    print(rc, data)

    rc, data = lm.datastore_pcie(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_b(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_c(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_d(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_e(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_f(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_h(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_l(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_m(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_p(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_s(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_t(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_u(0)
    print(rc, data)

    rc, data = lm.datastore_lmdb_v(0)
    print(rc, data) 

if __name__ == "__main__":
    test()
