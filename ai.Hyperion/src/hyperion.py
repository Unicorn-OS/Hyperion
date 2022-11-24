import subprocess


def pci_info():
    out = subprocess.call(["lspci", "-nnk"])
    return "See PCI devices"
