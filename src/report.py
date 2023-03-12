from collections import defaultdict
from .parsing import AbstractParser
from .ping import AbstractPinger


def make_report(data, parser:AbstractParser, pinger:AbstractPinger):
    report = defaultdict(list)
    for site in parser.parse(data):
        if site.ports:
            for port in site.ports:
                report[site].append(pinger.ping_port(site.ip_address, port))
        else:
            report[site].append(pinger.ping_host(site.ip_address))
    return report

