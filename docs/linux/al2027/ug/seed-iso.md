---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/seed-iso.html
---

# NoCloud (`seed.iso`) `cloud-init` configuration for Amazon Linux 2027 on KVM and VMware
<a name="seed-iso"></a>

 This section covers how to create and use a `seed.iso` image to configure Amazon Linux 2027 running on KVM or VMware. Because KVM and VMware environments do not have [Amazon EC2 Instance Metadata Service (IMDS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service), an alternate method of configuring Amazon Linux 2027 is required, and providing a `seed.iso` image is one of those methods.

 The `seed.iso` boot image includes the initial configuration information that is needed to boot and configure your new virtual machine, such as the network configuration, host name, and user data.

**Note**
 The `seed.iso` image includes only the configuration information required to boot the VM. It does not include the Amazon Linux 2027 operating system files.

 To generate the `seed.iso` image, you need at least two configuration files, sometimes three:

** `meta-data` **
 This file typically includes the hostname for the virtual machine.

** `user-data` **
 This file typically configures user accounts, their passwords, SSH key pairs, or other access mechanisms. By default, the Amazon Linux 2027 KVM and VMware images create an `ec2-user` user account. You can use the `user-data` configuration file to set the password, SSH keys, or both for this default user account.

** `network-config` (optional) **
 This file typically provides a network configuration for the virtual machine that overrides the default configuration. The default configuration is to use DHCP on the first available network interface.

**Create the `seed.iso` disk image**

1. On a Linux or macOS computer, create a new folder named `seedconfig` and navigate into it.
**Note**
 If you're using Windows or another operating system, you can complete these steps, but you must find an equivalent tool to `mkisofs` to create the `seed.iso` image.

1. Create the `meta-data` configuration file.

   1. Create a new file named `meta-data`.

   1.  Open the `meta-data` file using your preferred editor and add the following, replacing {{vm-hostname}} with the host name for the VM:

      ```
      #cloud-config
      local-hostname: {{vm-hostname}}
      ```

   1. Save and close the `meta-data` configuration file.

1. Create the `user-data` configuration file.

   1. Create a new file named `user-data`.

   1.  Open the `user-data` file using your preferred editor and add the following, making substitutions as needed:

      ```
      #cloud-config
      #vim:syntax=yaml
      users:
      # A user by the name 'ec2-user' is created in the image by default.
        - default
        - name: ec2-user
          ssh_authorized_keys:
            - ssh-rsa {{ssh-key}}
      # In the above line, replace {{ssh key}} with the content of your ssh public key.
      ```

   1.  You can optionally add more user accounts to the `user-data` configuration file.

       You can specify additional user accounts, their access mechanisms, passwords, and key pairs. For more information about the supported directives, see the [upstream `cloud-init` documentation](https://docs.cloud-init.io/en/26.1/explanation/format/index.html).

   1. Save and close the `user-data` configuration file.

1. (Optional) Create the `network-config` configuration file.

   1. Create a new file named `network-config`.

   1.  Open the `network-config` file using your preferred editor and add the following, replacing the various IP addresses with the appropriate ones for your setup.

      ```
      #cloud-config
      version: 2
      ethernets:
        enp1s0:
          addresses:
            - {{192.168.122.161/24}}
          gateway4: {{192.168.122.1}}
          nameservers:
            addresses: {{192.168.122.1}}
      ```
**Note**
 `cloud-init` network configuration provides mechanisms to match against the MAC address of the interface instead of specifying the interface name which can change depending on the VM configuration. This (and more) `cloud-init` features for network configuration are described in more detail in the [upstream `cloud-init` Network Config Version 2 documentation](https://docs.cloud-init.io/en/26.1/reference/network-config-format-v2.html).

   1. Save and close the `network-config` configuration file.

1.  Create the `seed.iso` disk image using the `meta-data`, `user-data`, and optional `network-config` configuration files created in the previous steps.

    Do one of the following, depending on the operating system you're using to create the `seed.iso` disk image:
   +  On Linux systems, use a tool such as **mkisofs** or **genisoimage** to create the completed `seed.iso` file. Navigate into the `seedconfig` folder, and run the following command:

     ```
     $ mkisofs -output seed.iso -volid cidata -joliet -rock user-data meta-data
     ```
   +  (Optional) If you created a `network-config` file, include it in the invocation of **mkisofs**:

     ```
     $ mkisofs -output seed.iso -volid cidata -joliet -rock user-data meta-data network-config
     ```
   +  On macOS systems, you can use a tool such as **hdiutil** to generate the finished `seed.iso` file. Since **hdiutil** takes a pathname rather than a list of files, the same invocation can be used regardless of if a `network-config` configuration file has been created or not.

     ```
     $ hdiutil makehybrid -o seed.iso -hfs -joliet -iso -default-volume-name cidata seedconfig/
     ```

1.  The resulting `seed.iso` file can now be attached to your new Amazon Linux 2027 virtual machine using a virtual CD-ROM drive for `cloud-init` to find on first boot and apply the configuration to the system.
