---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/virtualization-virsh.html
---

# Manage virtual machines with virsh on Amazon Linux 2023
<a name="virtualization-virsh"></a>

Running `qemu-system-x86_64` by hand is convenient for a one-off guest, but it means re-typing a long command line every time and managing the process yourself. libvirt solves that: you describe the guest once in an XML document called a *domain*, and the libvirt daemon builds the QEMU command line, starts and stops the guest, and keeps track of it. `virsh` is the command line client that talks to that daemon.

This page walks through the full lifecycle of one guest. It assumes you have already installed the packages and enabled the daemon as described in [Get started with virtualization on Amazon Linux 2023](virtualization-getting-started.md).

**Important**
Run `virsh` with `sudo`. The system libvirt instance (`qemu:///system`) authorizes non-root callers through polkit, and a non-interactive shell has no polkit agent, so an unprivileged `virsh` fails with `authentication unavailable: no polkit agent available to authenticate action 'org.libvirt.unix.manage'`. Either use `sudo`, or add your user to the `libvirt` group and start a new login session. Unprivileged users can alternatively use the per-user instance, `virsh -c qemu:///session`, which needs no privileges but cannot use the shared networks described below.

**Topics**
+ [Write the domain XML](#virtualization-virsh-xml)
+ [Define, start, and connect to the guest](#virtualization-virsh-lifecycle)
+ [Choose a networking mode](#virtualization-virsh-networking)
+ [Related topics](#virtualization-virsh-more-info)

## Write the domain XML
<a name="virtualization-virsh-xml"></a>

Save the following as `al2023-demo.xml`. It describes a guest with two vCPUs, 2 GiB of memory, a virtio disk, user-mode networking, and a serial console. Point `source file` at a disk image you have already created, for example a copy of the AL2023 Kernel-based Virtual Machine (KVM) image, or a blank image from `qemu-img create`.

```
<domain type='kvm'>
  <name>al2023-demo</name>
  <memory unit='MiB'>2048</memory>
  <vcpu>2</vcpu>
  <os>
    <type arch='x86_64' machine='q35'>hvm</type>
    <boot dev='hd'/>
  </os>
  <features>
    <acpi/>
    <apic/>
  </features>
  <cpu mode='host-passthrough'/>
  <clock offset='utc'/>
  <devices>
    <emulator>/usr/bin/qemu-system-x86_64</emulator>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='/var/lib/libvirt/images/al2023-demo.qcow2'/>
      <target dev='vda' bus='virtio'/>
    </disk>
    <interface type='user'>
      <backend type='passt'/>
      <model type='virtio'/>
    </interface>
    <serial type='pty'>
      <target port='0'/>
    </serial>
    <console type='pty'>
      <target type='serial' port='0'/>
    </console>
    <memballoon model='virtio'/>
  </devices>
</domain>
```

Three details in this document are specific to AL2023:
+ `machine='q35'` is required, because the legacy `pc` machine type is not built. libvirt expands this to a versioned machine such as `pc-q35-11.0`, which you can see with `virsh dumpxml`.
+ `<backend type='passt'/>` selects `passt` for user-mode networking. The older SLIRP backend is not built, so a plain `<interface type='user'/>` with no backend will not work.
+ `<cpu mode='host-passthrough'/>` passes the host CPU through to the guest. This requires KVM. If you are running under emulation without `/dev/kvm`, use `<domain type='qemu'>` instead of `<domain type='kvm'>` and set `<cpu mode='maximum'/>`.

## Define, start, and connect to the guest
<a name="virtualization-virsh-lifecycle"></a>

1. Register the domain with libvirt. This only stores the definition; it does not start anything.

   ```
   [ec2-user ~]$ sudo virsh define al2023-demo.xml
   ```

1. Start the guest, then confirm it is running.

   ```
   [ec2-user ~]$ sudo virsh start al2023-demo
   [ec2-user ~]$ sudo virsh list --all
   ```

   The output shows the running domain and the id libvirt assigned it:

   ```
    Id   Name          State
   -----------------------------
    1    al2023-demo   running
   ```

1. Attach to the guest's serial console. Press `Ctrl+]` to detach again without stopping the guest.

   ```
   [ec2-user ~]$ sudo virsh console al2023-demo
   ```

   The console attaches, and the guest boot messages end at a login prompt:

   ```
   Connected to domain 'al2023-demo'
   Escape character is ^] (Ctrl + ])
   [    2.865210] fuse: init (API version 7.38)
   [    2.869015] systemd[1]: Finished kmod-static-nodes.service - Create List of Static Device Nodes.
   [    2.870267] systemd[1]: Started systemd-journald.service - Journal Service.
   ...
   [    3.848629] virtio_net virtio0 enp1s0: renamed from eth0
   [    4.758537] IPv6: ADDRCONF(NETDEV_CHANGE): enp1s0: link becomes ready

   Amazon Linux 2023.12.20260909
   Kernel 6.1.182-227.379.amzn2023.x86_64 on an x86_64 (-)

   localhost login:
   ```

   Because the guest boots with a serial console, you see the firmware, the bootloader, the kernel, and finally a login prompt.

1. Inspect the guest without attaching to it.

   ```
   [ec2-user ~]$ sudo virsh dominfo al2023-demo
   [ec2-user ~]$ sudo virsh domstate al2023-demo
   [ec2-user ~]$ sudo virsh dumpxml al2023-demo
   ```

   `dumpxml` shows the definition after libvirt has filled in its defaults, which is the quickest way to see what QEMU is actually being asked to build.

1. Ask the guest to shut down cleanly, wait for it to stop, then remove the definition.

   ```
   [ec2-user ~]$ sudo virsh shutdown al2023-demo
   [ec2-user ~]$ sudo virsh domstate al2023-demo
   [ec2-user ~]$ sudo virsh undefine al2023-demo
   ```
**Note**
`shutdown` sends an ACPI power button event and depends on the guest responding to it. If the guest is unresponsive, `sudo virsh destroy al2023-demo` stops it immediately, which is the equivalent of pulling the power and can lose unwritten data. `undefine` removes the definition but does not delete the disk image — delete that yourself if you no longer need it.

## Choose a networking mode
<a name="virtualization-virsh-networking"></a>

Two guest networking modes are practical on AL2023, and they differ in what you have to enable.

### User-mode networking with passt
<a name="virtualization-virsh-net-passt"></a>

This is the mode used in the domain XML above. It gives the guest outbound access without a bridge, needs no additional daemon, and is the simplest option for a short-lived test guest.

```
<interface type='user'>
  <backend type='passt'/>
  <model type='virtio'/>
</interface>
```

Because there is no shared bridge, libvirt has no DHCP lease to report, so `virsh domifaddr` returns nothing useful for this mode. Read the address from inside the guest instead.

### The default NAT network
<a name="virtualization-virsh-net-nat"></a>

libvirt also ships a NAT network called `default`, which puts guests on a host bridge (`virbr0`, `192.168.122.0/24`) with DHCP. Guests on it can reach each other and the host can reach them, which user-mode networking does not provide.

**Important**
The `default` network is managed by a separate daemon, `virtnetworkd`, which is not enabled by default. Until you enable it, any network command fails with `Failed to connect socket to '/var/run/libvirt/virtnetworkd-sock': No such file or directory`, even though the `libvirt-daemon-config-network` package is installed.

1. Enable the network daemon socket and confirm the network is available.

   ```
   [ec2-user ~]$ sudo systemctl enable --now virtnetworkd.socket
   [ec2-user ~]$ sudo virsh net-list --all
   ```

1. Start the network, and mark it to start automatically in future.

   ```
   [ec2-user ~]$ sudo virsh net-start default
   [ec2-user ~]$ sudo virsh net-autostart default
   ```

   If the network is already running, `net-start` reports `network is already active`, which is harmless.

1. Replace the interface in your domain XML, then redefine and start the guest.

   ```
   <interface type='network'>
     <source network='default'/>
     <model type='virtio'/>
   </interface>
   ```

1. Once the guest has booted and requested an address, libvirt can report it.

   ```
   [ec2-user ~]$ sudo virsh domifaddr al2023-demo --source lease
   [ec2-user ~]$ sudo virsh domiflist al2023-demo
   ```

   The lease output gives the guest's address on the NAT network:

   ```
    Name       MAC address          Protocol     Address
   -------------------------------------------------------------
    vnet0      52:54:00:c1:69:b8    ipv4         192.168.122.130/24
   ```

## Related topics
<a name="virtualization-virsh-more-info"></a>
+ [Get started with virtualization on Amazon Linux 2023](virtualization-getting-started.md)
+ [Virtualization on Amazon Linux 2023](virtualization.md) — what the stack does and does not support.
