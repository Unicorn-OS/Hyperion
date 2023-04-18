import libvirt


def connect():
    conn = libvirt.open('qemu:///system')
    return conn
