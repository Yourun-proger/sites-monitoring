import socket
from .errors import IncorrectDataError


def get_ip_address(domain):
    try:
        return socket.gethostbyname(domain)
    except:
        raise IncorrectDataError('DNS-server not returning ip address by domain!')

def get_type_of_port(result):
    if result.is_alive:
        return "Opened"
    else:
        return "Not opened"

def format_date(date):
    return date.isoformat().replace('T', ' ')

def format_site_without_ports(site, result):
    result = result[0]
    return f"{format_date(result.date)} | {site.domain} | {site.ip_address} | {result.rtt} ms | -1 | ???"

def format_site_with_ports(site, result):
    formatted_result = []
    for ind, resp in enumerate(result):
        formatted_result.append(
                f"{format_date(resp.date)} | {site.domain} | {site.ip_address} | {resp.rtt} ms | {site.ports[ind]} | {get_type_of_port(resp)}"
        )
    return formatted_result

