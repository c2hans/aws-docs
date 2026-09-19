---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/virtualization.html
---

# Virtualization on Amazon Linux 2023
<a name="virtualization"></a>

Amazon Linux 2023 includes a scoped virtualization stack for development, testing, and continuous integration workloads. You can run virtual machines on any Amazon EC2 instance. Hardware acceleration through KVM is faster but optional, and requires either a bare metal instance or a virtual instance with nested virtualization enabled. The stack comprises QEMU (system and userspace emulation for `x86-64` and `aarch64`), libvirt for virtual machine lifecycle management, and boot firmware (SeaBIOS and EDK2 UEFI).

These packages are available from the AL2023 core repository as of release version `2023.12.20260831` or later.

**Important**
This is not a production hypervisor, and it is not intended for running trusted workloads. The stack is intended for short-lived, disposable workloads such as kernel debugging and integration testing. Features that a production hypervisor requires, including live migration, saving and restoring a virtual machine across QEMU versions, and UEFI Secure Boot in guests, are not supported. For production virtualization workloads, use Amazon EC2.
AL2023 tracks upstream QEMU releases, so the emulated machine is not guaranteed to be identical across updates. Treat guests as disposable. We do not guarantee version stability with updates.

**Note**
None of the virtualization packages are installed in any AL2023 AMI or container image, and none of their services are enabled by default. Virtualization is opt-in. Installing the packages does not change the behavior of an existing workload.

If instead you want to run AL2023 itself as a guest on another hypervisor, see [Using Amazon Linux 2023 outside of Amazon EC2](outside-ec2.md).

**Topics**
+ [Virtualization packages](#virtualization-packages)
+ [Supported architectures, machines, and devices](#virtualization-scope)
+ [Limitations and unsupported functionality](#virtualization-limitations)
+ [Support and updates](#virtualization-support)
+ [Related topics](#virtualization-more-info)
+ [Get started with virtualization on Amazon Linux 2023](virtualization-getting-started.md)
+ [Manage virtual machines with virsh on Amazon Linux 2023](virtualization-virsh.md)

## Virtualization packages
<a name="virtualization-packages"></a>

The following packages make up the virtualization stack. All of them are part of the AL2023 core repository.

**AL2023 virtualization packages**

| Package | Description |
| --- | --- |
| qemu-kvm | The QEMU machine emulator, using the Kernel-based Virtual Machine (KVM) hypervisor for hardware-accelerated virtualization. The per-architecture packages are qemu-system-x86 and qemu-system-aarch64. |
| qemu-img | Tooling to create, convert, and inspect virtual machine disk images. |
| qemu-user, qemu-user-static | Userspace (linux-user) emulation, which runs a single binary built for the other architecture without booting a guest. The -static variants have no shared library dependencies. |
| qemu-user-binfmt | Registers the userspace emulators as binfmt\_misc handlers, so the kernel runs different architecture binaries transparently. |
| qemu-guest-agent | The guest agent, for installation inside a guest so that the host can query and coordinate with it. |
| libvirt, libvirt-client | The libvirt management daemons and API, and the virsh command line client. |
| python3-libvirt | Python bindings for the libvirt API. |
| edk2-ovmf, edk2-aarch64 | EDK2 UEFI guest firmware for x86-64 and aarch64 respectively. |
| seabios | SeaBIOS legacy BIOS guest firmware, the default for x86-64 guests. |
| passt | User-mode networking for guests. |
| nbdkit | A Network Block Device server and plugins, for serving disk images to guests. |
| virt-what | A utility to detect whether the system it runs on is itself a virtual machine. |

## Supported architectures, machines, and devices
<a name="virtualization-scope"></a>

To keep the security exposure small, the QEMU build shipped in AL2023 is deliberately narrower than upstream. The following sections describe what is supported in the QEMU build.

### Architectures
<a name="virtualization-scope-arch"></a>

Only `x86-64` and `aarch64` are supported, for both system emulation and userspace emulation. Emulators for other architectures, such as PowerPC, RISC-V, MIPS, and s390, are not built and not shipped.

### Machine types
<a name="virtualization-scope-machines"></a>

One machine type is available per architecture:
+ `x86-64` — `q35` only.
+ `aarch64` — `virt` only.

**Important**
The legacy `pc` (i440FX) machine type is not built. If you are migrating a QEMU command line from AL2 that relied on the default machine type, you must specify `-machine q35` explicitly. Other AL2 machine types, including `isapc` and `microvm`, are also unavailable.

### Devices
<a name="virtualization-scope-devices"></a>

The device model is virtio-first. Modern paravirtualized virtio devices are the intended way to attach storage, networking, and other resources to a guest: `virtio-blk`, `virtio-net`, `virtio-scsi`, `virtio-serial`, `virtio-rng`, `virtio-balloon`, and `virtio-input`.

A small number of non-virtio devices are also enabled, because guest firmware and installers need them:
+ Standard PCI VGA, used by firmware, GRUB, and the early kernel framebuffer.
+ AHCI (SATA) and NVMe storage controllers.
+ `e1000` and `e1000e` network adapters.
+ xHCI USB controllers and USB HID devices.

Most legacy device emulation is removed. The following are not available:
+ Legacy network adapters, including `rtl8139`, `ne2k`, `pcnet`, and `vmxnet3`.
+ IDE storage controllers and floppy disk controllers.
+ Legacy and vendor display adapters, including `cirrus-vga`, `qxl`, and `vmware-svga`. Note that `virtio-gpu` and `virtio-vga` are also not built; standard VGA is the only emulated display adapter.
+ Audio devices. No emulated sound hardware is available, and the build has no host audio backend.
+ Trusted Platform Module (TPM) devices, in any form.
+ VFIO, and therefore PCI device passthrough.

### Display and networking backends
<a name="virtualization-scope-display-net"></a>

For guest console access, the serial console and VNC are available. The GTK, SDL, SPICE, curses, and D-Bus display frontends are not built, so QEMU cannot open a local graphical window on the host.

For guest networking, `passt` provides user-mode networking, and bridged or tap networking is available for privileged setups. The older SLIRP user-mode backend is not built, so `-netdev user` is unavailable; use `-netdev passt` instead.

## Limitations and unsupported functionality
<a name="virtualization-limitations"></a>

**Unsupported functionality**
+ **Live migration**: migrating a running guest between hosts is not supported.
+ **Saving and restoring a guest across QEMU versions**: suspending a guest and resuming it under a different QEMU version is not supported.
+ **UEFI Secure Boot in guests**: the EDK2 firmware shipped in `edk2-ovmf` and `edk2-aarch64` is built without Secure Boot support, and no Secure Boot enabled firmware variant is shipped. Secure Boot must be left disabled in the guest configuration.
+ **Virtual TPM and measured boot**: QEMU is built without TPM support, and no software TPM emulator is shipped. Guest functionality that requires a TPM, including measured boot and TPM-backed disk encryption, is not available.
+ **Device passthrough**: VFIO is not built, so PCI and USB device passthrough into a guest are not available.
+ **Graphical management tools**: `virt-manager`, `virt-install`, and `virt-viewer` are not shipped. Manage guests with `virsh` and libvirt domain XML, or with the libvirt API through `python3-libvirt`.
+ **Guest filesystem tooling**: `libguestfs` and its utilities, such as `guestfish` and `virt-customize`, are not shipped. Use `qemu-img` and `nbdkit` for disk image work.
+ **Guest operating systems**: the software you run inside a guest is outside the scope of the virtualization packages.

## Support and updates
<a name="virtualization-support"></a>

The virtualization packages are part of the AL2023 core repository, so they receive the same support as the rest of core AL2023, including AWS CVE security tracking and security updates for the supported life of Amazon Linux 2023.

Updates follow the normal AL2023 deterministic upgrade model, so a new package version is only applied when you move to a new release version. For more information, see [Deterministic upgrades through versioned repositories on AL2023](deterministic-upgrades.md). Because the stack tracks upstream QEMU releases rather than backporting individual patches, a new AL2023 release version can bring a new upstream QEMU version.

## Related topics
<a name="virtualization-more-info"></a>
+ [Get started with virtualization on Amazon Linux 2023](virtualization-getting-started.md)
+ [Manage virtual machines with virsh on Amazon Linux 2023](virtualization-virsh.md)
+ [Using Amazon Linux 2023 outside of Amazon EC2](outside-ec2.md) — running AL2023 itself as a guest on KVM, VMware, or Hyper-V.
+ [AL2023 system requirements](system-requirements.md)
