# server.py
from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from socketserver import ThreadingMixIn
import socket
import threading

class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    """Multithreaded XML-RPC Server"""

class MathService:
    def __init__(self):
        self._add_cnt      = 0
        self._sub_cnt      = 0
        self._min_cnt      = 0
        self._max_cnt      = 0
        self._tot_cnt      = 0
        self._lock         = threading.Lock()

    def magicAdd(self, a, b):
        with self._lock:
            self._add_cnt += 1
            self._tot_cnt += 1
        return a + b

    def magicSubtract(self, a, b):
        with self._lock:
            self._sub_cnt += 1
            self._tot_cnt += 1
        return a - b

    def magicFindMin(self, x, y, z):
        with self._lock:
            self._min_cnt += 1
            self._tot_cnt += 1
        return min(x, y, z)

    def magicFindMax(self, x, y, z):
        with self._lock:
            self._max_cnt += 1
            self._tot_cnt += 1
        return max(x, y, z)

    # Getters for counters
    def getAddCount(self):
        return self._add_cnt

    def getSubtractCount(self):
        return self._sub_cnt

    def getMinCount(self):
        return self._min_cnt

    def getMaxCount(self):
        return self._max_cnt
        
    def getTotCount(self):
        return self._tot_cnt

if __name__ == "__main__":
    while(True):
        try:
            PORT = int(input("Enter Port number (1 to 65535) to run Math Server: "))
            if (PORT < 1) or (PORT > 65535):
                raise ValueError
        except KeyboardInterrupt:
            print("")
            break
        except:
            print("Enter valid Port number between 1 to 65535")
        else:
            HOST = "0.0.0.0"
            server = ThreadedXMLRPCServer((HOST, PORT), allow_none=True)
            server.register_instance(MathService())
            HOST = socket.gethostbyname(socket.gethostname())
            print(f"Math RPC server listening on {HOST}:{PORT} …")
            server.serve_forever()
