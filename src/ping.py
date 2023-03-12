import socket
import time
from datetime import datetime
import errno
import icmplib
from .models import PingResponse


class AbstractPinger:
    def ping_host(self, address) -> PingResponse:
        ...
    def ping_port(self, address, port) -> PingResponse:
        ...

class DefaultPinger(AbstractPinger):
    def ping_host(self, host) -> PingResponse:
        result = icmplib.ping(address=host, count=5, interval=0.2, privileged=False)
        return PingResponse(
                    is_alive=result.is_alive,
                    rtt=result.avg_rtt,
                    date=datetime.now(),
        )
    def ping_port(self, host, port, timeout=2):
        s = socket.socket()
        s.settimeout(timeout)
        try:
            start = time.time()
            s.connect((host, port))
            s.close()
            return PingResponse(
                        is_alive=True,
                        rtt=round(1000*(time.time() - start),2),
                        date=datetime.now(),
            )
        except Exception as e:
            if e == errno.ECONNREFUSED:
                return PingResponse(
                        is_alive=True,
                        rtt=round(1000*(time.time() - start), 2),
                        date=datetime.now(),
                )
            else:
                return PingResponse(
                        is_alive=False,
                        rtt=round(1000*(time.time() - start), 2),
                        date=datetime.now(),
                )

