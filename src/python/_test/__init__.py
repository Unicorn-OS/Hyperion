import list.domain
from instance import *

def getSingle():
    uuid = getUUID(7)
    print(uuid)
    domain = getByID(7)
    print(domain.info(), domain.OSType())


print("Off ", list.domain.inactive())
print("all ", list.domain.all())