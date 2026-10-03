---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/outside-ec2-configuration.html
---

# Amazon Linux 2027 Set up and `cloud-init` configuration when used outside Amazon EC2
<a name="outside-ec2-configuration"></a>

 This section covers how to set up and configure a Amazon Linux 2027 virtual machine when not run directly on Amazon EC2, such as when on KVM, VMware, or Hyper-V.

 By default, Amazon Linux 2027 virtual machine images don't come provisioned with any user password or SSH key and will get their network configuration through DHCP on the first discovered network interface. This means that by default, without additional configuration, there is no way to connect to the resulting virtual machine.

 Thus, some form of configuration needs to be provided to the virtual machine. The standard mechanism to do this for Amazon Linux is via `cloud-init` data sources.

Amazon Linux 2027 has been qualified with the following data sources:

** NoCloud **
 This is the traditional method of configuring on-premises images via a virtual CD-ROM containing a seed ISO9660 image with `cloud-init` configuration files.

** VMware **
 Amazon Linux 2027 additionally supports configuring VMware images running on vSphere via the VMware-specific data source via VMware `guestinfo.userdata` and `guestinfo.metadata`.

**Note**
 The configuration of the data sources may differ from Amazon Linux 2023. While Amazon Linux 2027 continues to use `systemd-networkd` and `cloud-init` for its configuration, `cloud-init v26` has some changes as documented in its [network configuration documentation](https://docs.cloud-init.io/en/26.1/reference/network-config.html).

 The complete documentation for `cloud-init` configuration mechanisms for the version of `cloud-init` packaged in Amazon Linux 2027 can be found in the [upstream `cloud-init` documentation](https://docs.cloud-init.io/en/26.1/index.html).
