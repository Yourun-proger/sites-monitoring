import csv
import typing as t
from .models import Site
from .validation import is_valid, AbstractValidator
from .errors import IncorrectDataError
from .helpers import get_ip_address


class AbstractParser():
    def parse(value, validator):
        ...

class DefaultParser(AbstractParser):
    def __init__(self, validator:AbstractValidator):
        self.validator = validator
    def parse(self, csv_file):
        relevant_data = csv.reader(csv_file, delimiter=';')
        processed_data = []
        for i in relevant_data:
            if i != ['Host', 'Ports']:
                if is_valid(i[0], self.validator):
                    domain = i[0] if self.validator.validate_domain_name(i[0]) else '???'
                    ip_address = i[0] if self.validator.validate_ip_address(i[0]) else get_ip_address(i[0])
                    ports = tuple(map(int, filter(lambda port: port.isdigit(), i[1].split(','))))
                    site = Site(domain=domain, ip_address=ip_address, ports=ports)
                    processed_data.append(site)
                else:
                    raise IncorrectDataError("Bad IP address, Domain or Port value!")
        return processed_data

