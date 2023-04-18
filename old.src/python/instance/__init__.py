import connect

def getByID(id):
    domain = ''
    conn = connect.init()
    domainIDs = conn.listDomainsID()
    for domainID in domainIDs:
        domain = conn.lookupByID(id)
    conn.close()
    return domain

def getUUID(id):
    domain = getByID(id)
    uuid = domain.UUIDString()
    return uuid