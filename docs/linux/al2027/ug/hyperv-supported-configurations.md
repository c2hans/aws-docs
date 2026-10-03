---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/hyperv-supported-configurations.html
---

# Requirements for running Amazon Linux 2027 on Hyper-V
<a name="hyperv-supported-configurations"></a>

 This section covers the requirements for running Amazon Linux 2027 on Hyper-V. The Hyper-V images of AL2027 are available only for the `x86-64` architecture. Hyper-V images for `aarch64` are not available or supported.

 This section covers additional requirements on top of the base [AL2027 system requirements](system-requirements.md) for the Hyper-V images.

**Topics**
+ [Hyper-V host requirements for running Amazon Linux 2027 on Hyper-V](#hyperv-host-requirements)
+ [Device support for Amazon Linux 2027 on Hyper-V](#hyperv-devices)
+ [Limitations running Amazon Linux 2027 on Hyper-V](#hyperv-limitations)

## Hyper-V host requirements for running Amazon Linux 2027 on Hyper-V
<a name="hyperv-host-requirements"></a>

 The main qualification of Amazon Linux 2027 on Hyper-V happens on Windows Server 2022 running on an Amazon EC2 `c5.metal` instance.

## Device support for Amazon Linux 2027 on Hyper-V
<a name="hyperv-devices"></a>

 Amazon Linux 2027 is tested on both *Generation 1* and *Generation 2* Hyper-V virtual machines with the following set of virtualized hardware:
+  Generation 1 (legacy BIOS boot) VM
+  Generation 2 (UEFI boot - No secure boot) VM
+  The following device models are tested for use with AL2027 Hyper-V images:
  +  Hyper-V virtual storage `hv_storvsc` for the root disk and the emulated CD-ROM drive on *Generation 2* VMs
  +  Emulated PIIX IDE `ata_piix` for the virtual CD-ROM drive on *Generation 1* VMs
  +  Hyper-V virtual ethernet `hv_netvsc`
+  The following device models are enabled but lightly tested:
  +  Legacy VGA text mode on *Generation 1* VMs
  +  UEFI Firmware based framebuffer `simpledrmfb` on *Generation 2* VMs
  +  Hyper-V Balloon `hv_balloon`
  +  Hyper-V HID/Mouse `hid_hyperv`
+  The following device models are *not* enabled in AL2027 at this time:
  +  Hyper-V PCI pass-through
  +  Hyper-V DRM Graphics

**Important**
 For *Generation 2* virtual machines, Secure Boot is not supported and must be disabled before launching the virtual machine for a successful boot of Amazon Linux 2027. Hyper-V currently only supports Secure Boot with software components signed by Microsoft keys while the Amazon Linux bootloader is signed by an Amazon private key. Hyper-V doesn't currently support importing third-party keys.

## Limitations running Amazon Linux 2027 on Hyper-V
<a name="hyperv-limitations"></a>

The following are some known limitations in running Amazon Linux 2027 on Hyper-V:

**Note**
 Code implementing some of the listed unsupported functionality might exist in AL2027 and function correctly. The list of unsupported functionality exists so that you can make informed decisions about what to rely on today, and what the Amazon Linux team will qualify as working as part of future updates.

**Known limitations running AL2027 on Hyper-V**
+  UEFI Secure Boot mode is not currently supported or functional with AL2027 on Hyper-V
+  Hot plugging and unplugging CPU, memory, or any other device type is not supported.
+  Virtual Machine (VM) hibernation is not supported.
+  Virtual Machine (VM) migration is not supported.
+  Passthrough of any device such as through PCI Passthrough, or USB Passthrough is not supported.
