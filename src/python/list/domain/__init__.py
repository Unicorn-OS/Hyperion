import connect

def inactive():
    conn = connect.init()
    domainNames = conn.listDefinedDomains()
    conn.close()
    return domainNames


def all():
    conn = connect.init()
    domains = conn.listAllDomains(0)
    domain_arr = []
    if len(domains) != 0:
        for domain in domains:
            domain_arr.append(domain.name())

    conn.close()
    return domain_arr

# https://libvirt.org/docs/libvirt-appdev-guide-python/en-US/html/libvirt_application_development_guide_using_python-Guest_Domains-Listing_Domains.html