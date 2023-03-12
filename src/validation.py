import re


class AbstractValidator:
    def validate_domain_name(self, domain):
        ...
    def validate_ip_address(self, ip_address):
        ...

class DefaultValidator(AbstractValidator):
    pattern = re.compile(
        r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
        r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
        r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
        r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
    )

    def validate_domain_name(self, domain):
        return self.pattern.match(domain) or domain == 'localhost'

    def validate_ip_address(self, ip_address):
        if ip_address.count('.') == 3:
            ip_address = ip_address.split('.')
            n = 0
            for i in ip_address:
                if i.isdigit():
                    if 0 <= int(i) <= 255:
                        n += 1
            if n == 4:
                return True
            else:
                return False
        else:
            return False

def is_valid(value, validator:AbstractValidator):
    return validator.validate_domain_name(value) or validator.validate_ip_address(value)

