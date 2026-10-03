---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/kvm-supported-configurations.html
---

# Requirements for running AL2027 on KVM
<a name="kvm-supported-configurations"></a>

 This section describes the requirements for running Amazon Linux 2027 on KVM. The KVM images of AL2027 are available for both `aarch64` and `x86-64` architectures. These requirements are in addition to the base [AL2027 system requirements](system-requirements.md) for the KVM images.

**Topics**
+ [KVM host requirements for running AL2027 on KVM](#kvm-host-requirements)
+ [Device support for AL2027 on KVM](#kvm-devices)
+ [Boot mode (UEFI and BIOS) support for AL2027 on KVM](#kvm-boot-modes)
+ [Limitations running AL2027 on KVM](#kvm-limitations)

## KVM host requirements for running AL2027 on KVM
<a name="kvm-host-requirements"></a>

 The KVM images are currently qualified on a host running Ubuntu 22.04.3 LTS with `qemu` version 6.2\+dfsg-2ubuntu6.15, provided by this Ubuntu version, using a `q35` machine type for `x86-64` and a `virt` machine type for `aarch64`.

## Device support for AL2027 on KVM
<a name="kvm-devices"></a>

**The `qemu` device models tested for use with AL2027 KVM images (both `aarch64` and `x86-64`) are:**
+  `virtio-blk` (`virtio` block device)
+  `virtio-scsi` (`virtio` SCSI controller with disk device)
+  `virtio-net` (`virtio` network device)
+  `ahci` (for use with the virtual CD-ROM drive)
+  `usb-storage` (over `xhci`)

**Additional `qemu` device models enabled in AL2027 KVM image qualification, but not heavily exercised are:**
+  `VGA` (`qemu` VGA) on `x86-64` only
+  `virtio-rng` (virtual random number generator)
+  legacy AT keyboard and PS/2 mouse devices
+  legacy serial device

## Boot mode (UEFI and BIOS) support for AL2027 on KVM
<a name="kvm-boot-modes"></a>

 The `x86-64` image is tested with both legacy BIOS and UEFI boot modes. The `aarch64` images are tested with UEFI boot mode.

**Note**
 By default, when using UEFI boot mode, some virtual machine managers provision the virtual machine with Microsoft Secure Boot keys, which enables Secure Boot. This configuration doesn't boot AL2027 because the AL2027 boot loader isn't signed by Microsoft, so the virtual machine must be provisioned either without UEFI keys or with the AL2027 keys for Secure Boot.

**Important**
 Secure Boot support for KVM images has not been validated yet.

## Limitations running AL2027 on KVM
<a name="kvm-limitations"></a>

There are some known limitations in running AL2027 on KVM.

**Note**
 Code implementing some of the listed unsupported functionality might exist in AL2027 and function correctly. The list of unsupported functionality exists so that you can make informed decisions about what to rely on today, and what the Amazon Linux team will qualify as working as part of future updates.

**Known limitations running AL2027 on KVM**
+  The KVM guest agent is not currently packaged or supported.
+  Hot plugging and unplugging CPU, memory, or any other device type is not supported.
+  Virtual Machine (VM) hibernation is not supported.
+  VM migration is not supported.
+  Passthrough of any device such as through PCI Passthrough, or USB Passthrough is not supported.
