---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/installing-gnome.html
---

# Tutorial: Install the GNOME desktop environment
<a name="installing-gnome"></a>

The [GNOME desktop environment](https://www.gnome.org/) is an optional graphical user interface for Amazon Linux 2027 (AL2027). The `Desktop` package group installs GNOME along with its supporting components.

In this tutorial, you install the GNOME desktop environment on your AL2027 instance so you can use a graphical interface instead of the command line. This is useful for workloads such as data visualization, computer-aided design (CAD), or scientific applications.

This tutorial takes approximately 15–20 minutes to complete.

**Note**
Completing this tutorial requires a running Amazon EC2 instance, which might result in charges to your AWS account for the instance, Amazon Elastic Block Store (Amazon EBS) storage, and associated resources. For pricing details, see [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/). To avoid ongoing charges, stop or terminate the instance when you are finished.

**Topics**
+ [Prerequisites](#installing-gnome-prereqs)
+ [Step 1: Install the GNOME desktop environment](#gnome-install)
+ [Step 2: Start the desktop](#gnome-start)
+ [Step 3: Clean up resources](#gnome-remove)
+ [Related topics](#gnome-more-info)

## Prerequisites
<a name="installing-gnome-prereqs"></a>

Before you install the desktop environment, make sure your instance meets the following requirements.

### Memory (RAM)
<a name="installing-gnome-prereqs-memory"></a>

The GNOME desktop environment requires **at least 2 GB of memory to start**, and **4 GB or more is recommended** for comfortable interactive use. Choose an instance type with sufficient memory, such as `t3.medium` (4 GB) or larger. Smaller types like `t3.nano`, `t3.micro`, and `t3.small` do not have enough memory for a responsive desktop.

### Base system
<a name="installing-gnome-prereqs-base"></a>

This tutorial assumes that you have already launched an instance running a current release of AL2027 and that the system is up to date. For more information, see the [AL2027 on Amazon EC2](ec2.md) and [Updating AL2027](updating.md) pages. Update your packages before installing the desktop so that dependencies resolve against the latest versions:

```
[ec2-user ~]$ sudo dnf update -y
```

## Step 1: Install the GNOME desktop environment
<a name="gnome-install"></a>

1. Install the GNOME desktop environment and related packages.

   ```
   [ec2-user ~]$ sudo dnf groupinstall "Desktop" -y
   ```

   You can confirm what the group contains at any time with:

   ```
   [ec2-user ~]$ dnf group info "Desktop"
   ```

1. (Optional) Verify that the group is installed.

   ```
   [ec2-user ~]$ dnf group list --installed
   ```

**Note**
To access the graphical desktop environment, you need to install and configure additional software such as Amazon DCV or VNC. These tools allow you to connect to and interact with the graphical user interface over the network.

## Step 2: Start the desktop
<a name="gnome-start"></a>

The `Desktop` group installs the **GDM** display manager but does not start it automatically. Enable and start it so the graphical login is available now and on every boot:

```
[ec2-user ~]$ sudo systemctl enable --now gdm
```

To make the system boot into the graphical interface by default:

```
[ec2-user ~]$ sudo systemctl set-default graphical.target
```

You can verify the service and default target with:

```
[ec2-user ~]$ systemctl is-active gdm
[ec2-user ~]$ systemctl get-default
```

## Step 3: Clean up resources
<a name="gnome-remove"></a>

To avoid ongoing charges, clean up the resources you created for this tutorial when you are finished with them.

1. If you no longer need the instance, stop or terminate it. Stopping the instance ends compute charges but retains the Amazon EBS volume; terminating it removes the instance and its associated resources. For more information, see the [AL2027 on Amazon EC2](ec2.md) page.

1. If you want to keep the instance but no longer need the graphical desktop, stop the graphical login and prevent it from starting on boot.

   ```
   [ec2-user ~]$ sudo systemctl disable --now gdm
   ```

1. Restore the default boot target to the multiuser (non-graphical) target.

   ```
   [ec2-user ~]$ sudo systemctl set-default multi-user.target
   ```

1. (Optional) Uninstall the desktop packages.

   ```
   [ec2-user ~]$ sudo dnf groupremove "Desktop" -y
   ```

## Related topics
<a name="gnome-more-info"></a>

For more information about the graphical desktop environment, see the following documentation:
+ [What Is Amazon DCV?](https://docs.aws.amazon.com/dcv/latest/adminguide/what-is-dcv.html) in the *Amazon DCV Administrator Guide*
