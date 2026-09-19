---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/virtualization-getting-started.html
---

# Get started with virtualization on Amazon Linux 2023
<a name="virtualization-getting-started"></a>

This page covers what an instance needs before it can run virtual machines, how to install and enable the virtualization packages, and an example that runs a virtual machine with QEMU. To manage guests with libvirt instead of running QEMU by hand, see [Manage virtual machines with virsh on Amazon Linux 2023](virtualization-virsh.md). For what the stack does and does not support, see [Virtualization on Amazon Linux 2023](virtualization.md).

**Topics**
+ [Enable hardware virtualization](#virtualization-requirements)
+ [Install and enable the virtualization packages](#virtualization-install)
+ [Example: run a virtual machine with QEMU](#virtualization-example-vm)
+ [Things to remember](#virtualization-gotchas)

## Enable hardware virtualization
<a name="virtualization-requirements"></a>

Enabling hardware virtualization is optional: without it QEMU emulates the guest processor in software, which works on any instance type. Kernel-based Virtual Machine (KVM) is the kernel component that lets QEMU use the processor's own virtualization extensions, which is what makes a guest run at close to native speed. The kernel exposes it as the device node `/dev/kvm`. Without that node, QEMU can still run a guest by translating every instruction in software, but it will be several times slower.

An Amazon EC2 instance only sees those processor extensions if the instance is bare metal, or if it is a virtual instance with *nested virtualization* turned on. Nested virtualization is not on by default. You opt into it, either when you launch the instance or by changing a stopped instance.

1. Check that your intended instance type supports nested virtualization.

   ```
   [ec2-user ~]$ aws ec2 describe-instance-types \
     --instance-types m8i.xlarge \
     --query "InstanceTypes[].ProcessorInfo.SupportedFeatures"
   ```

   The output includes `nested-virtualization` when the type supports it. To list every supported family in a Region, filter on the same feature:

   ```
   [ec2-user ~]$ aws ec2 describe-instance-types \
     --filters "Name=processor-info.supported-features,Values=nested-virtualization" \
     --query "InstanceTypes[].InstanceType" --output text | tr '\t' '\n' | cut -d. -f1 | sort -u
   ```

1. Turn nested virtualization on. For a new instance, pass it at launch:

   ```
   [ec2-user ~]$ aws ec2 run-instances \
     --image-id ami-0abcdef1234567890 \
     --instance-type m8i.xlarge \
     --cpu-options "NestedVirtualization=enabled" \
     --key-name my-key-pair
   ```

   For an instance that already exists, stop it first, then change its CPU options and start it again:

   ```
   [ec2-user ~]$ aws ec2 modify-instance-cpu-options \
     --instance-id i-1234567890abcdef0 \
     --nested-virtualization enabled
   ```

1. On the instance, confirm the extensions arrived and the device node exists.

   ```
   [ec2-user ~]$ grep -o -m1 -E 'vmx|svm' /proc/cpuinfo
   [ec2-user ~]$ ls -l /dev/kvm
   ```

   You should see the processor flag (`vmx` on Intel, `svm` on AMD) and a character device:

   ```
   crw-rw-rw-. 1 root kvm 10, 232 /dev/kvm
   ```

   The node is world-accessible, so you do not need to join a group to use KVM itself.

1. Confirm that QEMU can see the accelerator.

   ```
   [ec2-user ~]$ qemu-system-x86_64 -accel help
   ```

   Both `tcg` (software emulation) and `kvm` should be listed.

**Note**
If `/dev/kvm` is missing, the most likely cause is that nested virtualization was never enabled on the instance, rather than anything wrong with the packages. Everything on this page except KVM acceleration still works without it, using software emulation instead.

## Install and enable the virtualization packages
<a name="virtualization-install"></a>

1. Install QEMU, libvirt, and the `virsh` client. Add `edk2-ovmf` (or `edk2-aarch64` on `aarch64`) if you intend to boot guests with UEFI firmware rather than the default SeaBIOS legacy BIOS.

   ```
   [ec2-user ~]$ sudo dnf install -y qemu-kvm qemu-img libvirt libvirt-client edk2-ovmf
   ```

1. Enable and start the libvirt QEMU daemon socket. No libvirt service is enabled by default, so this step is required before `virsh` can manage guests.

   ```
   [ec2-user ~]$ sudo systemctl enable --now virtqemud.socket
   ```
**Note**
AL2023 ships the modular libvirt daemons, so the daemon that serves the QEMU driver is `virtqemud`. The older monolithic `libvirtd.service` unit is not shipped at all. If you are migrating scripts from AL2, replace references to `libvirtd` with `virtqemud`. Supporting daemons such as `virtlogd` are socket-activated on demand, so you do not need to enable them yourself.

1. Verify that the client can reach the daemon.

   ```
   [ec2-user ~]$ sudo virsh version
   ```

   The last line reports the emulator libvirt found:

   ```
   Running hypervisor: QEMU 11.0.0
   ```

## Example: run a virtual machine with QEMU
<a name="virtualization-example-vm"></a>

This example boots a guest directly with QEMU, using the `q35` machine type, KVM acceleration, virtio storage, user-mode networking, and the serial console. It is the quickest way to confirm the stack works end to end.

1. Create a disk image, or download a ready-made one. For the AL2023 KVM images, see [Download Amazon Linux 2023 images for use with KVM, VMware, and Hyper-V](outside-ec2-download.md). The KVM images require additional configuration to log in, as described in [NoCloud (`seed.iso`) `cloud-init` configuration for Amazon Linux 2023 on KVM and VMware](seed-iso.md).

   ```
   [ec2-user ~]$ qemu-img create -f qcow2 guest.qcow2 10G
   ```

1. Boot the guest.

   ```
   [ec2-user ~]$ sudo qemu-system-x86_64 \
     -machine q35,accel=kvm \
     -cpu host \
     -smp 2 \
     -m 2048 \
     -drive file=guest.qcow2,format=qcow2,if=virtio \
     -netdev passt,id=net0 \
     -device virtio-net-pci,netdev=net0 \
     -nographic
   ```

   `-nographic` redirects the guest serial console to your terminal, so you can watch the firmware, bootloader, and kernel and then log in. To leave the guest, press `Ctrl+a` then `x`.

**Note**
If `/dev/kvm` is not available, drop `accel=kvm` and replace `-cpu host` with `-cpu max`. `-cpu host` requires KVM and fails with `CPU model 'host' requires KVM or HVF` without it. `-cpu max` is also necessary because the CPU model QEMU emulates by default is older than AL2023 userspace requires: a guest booted under emulation without it panics early in start-up with `Attempted to kill init`.

On `aarch64`, use `qemu-system-aarch64` with `-machine virt`. The `virt` machine has no legacy BIOS, so a guest requires the UEFI firmware from `edk2-aarch64`.

## Things to remember
<a name="virtualization-gotchas"></a>

The AL2023 virtualization stack is deliberately narrower than an upstream QEMU build, and most surprises come from that. The following list collects the differences you are most likely to trip over, especially when moving a working setup from AL2.
+ **Enable nested virtualization, or you get no KVM.** On a virtual instance this is opt-in. A missing `/dev/kvm` almost always means this step was skipped.
+ **Always specify `-machine q35`.** The legacy `pc` (i440FX) machine is not built, and it was the default on AL2. A command line that relied on the default fails outright with `unsupported machine type: "pc"`.
+ **Use `-netdev passt`, not `-netdev user`.** The SLIRP backend is not built. In libvirt domain XML the equivalent is `<interface type='user'><backend type='passt'/>`.
+ **The daemon is `virtqemud`, not `libvirtd`.** No `libvirtd.service` unit exists, and nothing is enabled until you enable it.
+ **Run `virsh` with `sudo`.** Without a polkit agent an unprivileged `virsh` cannot reach `qemu:///system`.
+ **The `default` NAT network needs `virtnetworkd.socket` enabled.** Until then every network command fails on a missing `virtnetworkd-sock`.
+ **There is no graphical console.** The GTK, SDL and SPICE frontends are not built. Use the serial console, or VNC.
+ **Display is standard VGA.** `virtio-gpu` and `virtio-vga` are not built.
+ **Treat guests as disposable.** Saving a guest and restoring it under a different QEMU version is not supported, and a new AL2023 release version can bring a new upstream QEMU. Do not build a workflow that depends on the emulated machine staying identical across updates.
+ **No Secure Boot, no vTPM, no device passthrough.** See [Limitations and unsupported functionality](virtualization.md#virtualization-limitations).
