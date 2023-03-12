from .helpers import (
                        format_site_without_ports,
                        format_site_with_ports
                    )


DEFAULT_FORMAT_RULES = {
    'site_without_ports': format_site_without_ports,
    'site_with_ports': format_site_with_ports,
}

def formatting(report, format_rules):
    output = []
    for site, result in report.items():
        output.append([site.domain, [site.ip_address], site.ports])
        if site.ports:
            output.extend(format_rules['site_with_ports'](site, result))
        else:
            output.append(format_rules['site_without_ports'](site, result))
        output.append('\n')
    return output

