---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/installing-gnome-al2023.html
---

# Tutorial: Install the GNOME desktop environment on AL2023
<a name="installing-gnome-al2023"></a>

 The [GNOME desktop environment](https://www.gnome.org/) is available as an optional graphical user interface for AL2023 as of release 2023.7 or later.

 The following procedures help you install the GNOME desktop environment on your AL2023 instance. You can use this graphical interface to interact with your Linux system using a familiar desktop environment instead of just the command line interface.

**Topics**
+ [Prerequisites](#installing-gnome-prereqs-2023)
+ [Installation](#gnome-install-2023)
+ [Related topics](#gnome-more-info-2023)

## Prerequisites
<a name="installing-gnome-prereqs-2023"></a>
+ The desktop environment requires at least 2.4 GB of memory. Therefore, an instance of type `t2.medium` or better is recommended to ensure adequate performance. Examples of instance types with insufficient memory include `t2.nano`, `t2.micro`, and `t2.small`. This restriction also applies to `t3` and `t4` instances of this size, as well as any other instance type that doesn't meet the memory requirement.
+ This tutorial assumes that you have already launched an instance using AL2023 running release 2023.7 or later. For more information, see the [AL2023 on Amazon EC2](ec2.md) and [Updating AL2023](updating.md) pages.

## Installation
<a name="gnome-install-2023"></a>
+ Install the GNOME desktop environment and related packages.

  ```
  [ec2-user ~]$ sudo dnf groupinstall "Desktop" -y
  ```
**Note**
 To access the graphical desktop environment, you'll need to install and configure additional software such as Amazon DCV or VNC. These tools allow you to connect to and interact with the graphical user interface over the network.

## Related topics
<a name="gnome-more-info-2023"></a>

For more information about the graphical desktop environment, see the following documentation:
+ [What Is Amazon DCV?](https://docs.aws.amazon.com/dcv/latest/adminguide/what-is-dcv.html) in the * Amazon DCV Administrator Guide*
+  [Tutorial: Configure TigerVNC server on AL2023](vnc-configuration-al2023.md)
