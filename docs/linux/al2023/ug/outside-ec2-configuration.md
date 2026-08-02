---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/outside-ec2-configuration.html
---

# Amazon Linux 2023 Set up and `cloud-init` configuration when used outside Amazon EC2
<a name="outside-ec2-configuration"></a>

 This section covers how to set up and configure a Amazon Linux 2023 virtual machine when not run directly on Amazon EC2, such as when on KVM, VMware, or Hyper-V.

 By default, an Amazon Linux 2023 virtual machine images don’t come provisioned with any user password or ssh key and will obtain its network configuration via DHCP on the first discovered network interface. This means that by default, without additional configuration, there is no way to connect to the resulting virtual machine.

 Thus, some form of configuration needs to be provided to the virtual machine. The standard mechanism to do this for Amazon Linux is via `cloud-init` data sources.

Amazon Linux 2023 has been qualified with the following data sources:

** NoCloud **
 This is the traditional method of configuring on-premises images via a virtual CD-ROM containing a seed ISO9660 image with `cloud-init` configuration files.

** VMware **
 Amazon Linux 2023 additionally supports configuring VMware images running on vSphere via the VMware specific data source via VMware `guestinfo.userdata` and `guestinfo.metadata`.

**Note**
 The configuration of the data sources can differ from Amazon Linux 2. More specifically, Amazon Linux 2023 uses `systemd-networkd` for its configuration and requires the use of `cloud-init` "Networking Config Version 2" as documented in [the `cloud-init` network configuration documentation](https://cloudinit.readthedocs.io/en/22.2/topics/network-config.html).

 The complete documentation for `cloud-init` configuration mechanisms for the version of `cloud-init` packaged in Amazon Linux 2023 can be found in the [upstream `cloud-init` documentation](https://cloudinit.readthedocs.io/en/22.2/).
