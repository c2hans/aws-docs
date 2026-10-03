---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/vmware-supported-configurations.html
---

# Requirements for running AL2027 on VMware
<a name="vmware-supported-configurations"></a>

 This section describes the requirements for running AL2027 on VMware. The VMware images of AL2027 are available for only the `x86-64` architecture. VMware images for `aarch64` are not available or supported. These requirements are in addition to the base [AL2027 system requirements](system-requirements.md) for the VMware images.

**Topics**
+ [VMware host requirements for running AL2027 on VMware](#vmware-host-requirements)
+ [Device support for AL2027 on VMware](#vmware-devices)
+ [Boot mode (UEFI and BIOS) support for AL2027 on VMware](#vmware-boot-modes)
+ [Limitations running AL2027 on VMware](#vmware-limitations)

## VMware host requirements for running AL2027 on VMware
<a name="vmware-host-requirements"></a>

**The AL2027 VMware OVA images are currently qualified on the following:**
+  VMware Workstation 17.5.0 running on hosts using an Intel Xeon Platinum 8124M processor
+  VMware vSphere 8.0 using an Intel Xeon Platinum 8275CL processor

 The AL2027 VMware OVA images specify a *Machine Hardware Version* of 13.

**VMware Machine Hardware Version 13 is supported by:**
+  ESXi 6.5 or later
+  VMware Workstation 14 or later

## Device support for AL2027 on VMware
<a name="vmware-devices"></a>

**The following VMware device models were tested for use with AL2027 VMware OVA images (`x86-64` only):**
+  `vmw_pvscsi` (VMware paravirtualized SCSI controller)
+  `vmxnet3` (VMware paravirtualized network device)
+  `ata_piix` (legacy IDE for use with the virtual CD-ROM drive only)

**Additional VMware device models enabled in AL2027 VMware image qualification, but not heavily exercised:**
+  `vmw_vmci` and related `vsock` interface (virtual socket transport for the VMware guest agent)
+  `vmw_balloon` memory balloon device
+  VMware `SVGA` controller
+  legacy AT keyboard and PS/2 mouse devices

 The VMware guest agent package (`open-vm-tools`) is available and installed by default in the AL2027 VMware OVA images.

## Boot mode (UEFI and BIOS) support for AL2027 on VMware
<a name="vmware-boot-modes"></a>

 As of the 2027.0.20260831 release, the AL2027 VMware OVA image has been validated in both legacy BIOS and UEFI boot modes. The OVA default configuration is still legacy BIOS but can be changed by the user.

**Important**
 Secure Boot support requires UEFI, which has not been validated for AL2027 running on VMware.

## Limitations running AL2027 on VMware
<a name="vmware-limitations"></a>

There are some known limitations in running AL2027 on VMware.

**Note**
 Code implementing some of the listed unsupported functionality might exist in AL2027 and function correctly. The list of unsupported functionality exists so that you can make informed decisions about what to rely on today, and what the Amazon Linux team will qualify as working as part of future updates.

**Known limitations running AL2027 on VMware**
+  UEFI Secure Boot is not currently validated with AL2027 on VMware.
+  Hot plugging and unplugging CPU, memory, or any other device type is not supported.
+  Virtual Machine (VM) hibernation is not supported.
+  VM migration is not supported.
+  Passthrough of any device such as through PCI Passthrough, or USB Passthrough is not supported.
