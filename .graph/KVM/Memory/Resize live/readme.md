# Resize memory while a VM is Running!
**up to Max_size defined in domain**

sch: https://www.google.com/search?q=kvm+libvirt+resize+memory

## Solution:
https://www.unixarena.com/2015/12/linux-kvm-how-to-add-remove-memory-to-guest-on-fly.html/

```
vm=
size=8
virsh setmem $vm ${size}G
```
