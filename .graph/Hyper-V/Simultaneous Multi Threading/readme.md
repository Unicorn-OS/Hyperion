# Doc:
https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/manage/manage-hyper-v-scheduler-types#virtual-machine-cpu-resource-controls-and-the-root-scheduler

example:
```
$vmname = 'WindowsMiner'
Set-VMProcessor -VMName $vmname -HwThreadCountPerCore 2
```

## [Understanding how Hyper-V virtualizes processors](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/manage/manage-hyper-v-scheduler-types#understanding-how-hyper-v-virtualizes-processors)
