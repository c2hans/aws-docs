---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/nvidia-drivers.html
---

# NVIDIA drivers
<a name="nvidia-drivers"></a>

 Amazon Linux 2023 provides NVIDIA GPU drivers and CUDA Toolkit packages through a dedicated repository. AWS maintains this repository and provides security advisories through the [Amazon Linux Security Center (ALAS)](https://alas.aws.amazon.com).

**Topics**
+ [About the NVIDIA repository](#nvidia-drivers-about)
+ [Enabling the NVIDIA repository](#nvidia-drivers-install-repo)
+ [Installing NVIDIA drivers](#nvidia-drivers-install-driver)
+ [Installing CUDA Toolkit](#nvidia-drivers-install-cuda)
+ [Removing the NVIDIA repository](#nvidia-drivers-uninstall)

## About the NVIDIA repository
<a name="nvidia-drivers-about"></a>

 The AL2023 NVIDIA repository mirrors packages from [the official NVIDIA CUDA repository for AL2023](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#amazon-installation). AWS qualifies this NVIDIA software with AL2023 release candidates before redistributing, and provides security advisories for the packages in this repository.

 AWS mirrors NVIDIA Production Branch and Long Term Support Branch drivers to this repository. New Feature Branch (NFB) drivers are not mirrored, because they do not receive long-term security support. For more information about NVIDIA driver branches, see [NVIDIA driver lifecycle](https://docs.nvidia.com/datacenter/tesla/drivers/driver-lifecycle.html).

 The repository is available in all AWS Commercial Regions, as well as the AWS GovCloud (US) Regions and AWS China Regions.

 The repository provides NVIDIA Tesla (data center compute) and graphics drivers for x86\_64 architectures. GRID drivers, used for virtual display and remote workstation capabilities, are not included. For GRID driver installation, see [NVIDIA drivers for your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html) in the *Amazon EC2 User Guide*.

## Enabling the NVIDIA repository
<a name="nvidia-drivers-install-repo"></a>

 To enable the NVIDIA repository on your AL2023 instance, install the `nvidia-release` package. This adds the repository configuration and GPG keys to your system.

```
[ec2-user ~]$ sudo dnf install nvidia-release -y
```

Verify the repository was added:

```
[ec2-user ~]$ dnf repolist
```

You should see the `amazonlinux-nvidia` repository in the list.

```
repo id                    repo name                                                status
amazonlinux                Amazon Linux 2023 repository                             enabled
amazonlinux-nvidia         Amazon Linux 2023 NVIDIA repository                      enabled
```

## Installing NVIDIA drivers
<a name="nvidia-drivers-install-driver"></a>

 After enabling the repository, you can install NVIDIA driver packages using `dnf`.

1. Install the kernel headers and development packages for your running kernel:

   ```
   [ec2-user ~]$ sudo dnf install kernel-devel-$(uname -r) kernel-headers-$(uname -r) -y
   ```

1. Install the NVIDIA driver:

   ```
   [ec2-user ~]$ sudo dnf install nvidia-driver-cuda -y
   ```

1. Reboot the instance:

   ```
   [ec2-user ~]$ sudo reboot
   ```

1. After rebooting, verify the driver is loaded:

   ```
   [ec2-user ~]$ nvidia-smi
   ```

**Note**
 For GPU instances that require NVIDIA Fabric Manager (such as P4d, P5, and P6 instance types), install and enable the additional packages:

```
[ec2-user ~]$ DRV_BRANCH="$(modinfo nvidia | grep "^version:" | tr -s ' ' | cut -d ' ' -f 2)"
[ec2-user ~]$ sudo dnf install nvidia-fabricmanager-${DRV_BRANCH} -y
[ec2-user ~]$ sudo systemctl enable --now nvidia-fabricmanager
[ec2-user ~]$ sudo systemctl enable --now nvidia-persistenced
```
Verify that Fabric Manager is running and the GPUs are connected through NVSwitch:

```
[ec2-user ~]$ sudo systemctl status nvidia-fabricmanager
[ec2-user ~]$ nvidia-smi topo -m
```
In the topology matrix, connections between GPUs should show `NV` links, indicating active NVSwitch connectivity.

## Installing CUDA Toolkit
<a name="nvidia-drivers-install-cuda"></a>

 After installing the NVIDIA driver, you can install CUDA Toolkit:

```
[ec2-user ~]$ sudo dnf install cuda-toolkit -y
```

## Removing the NVIDIA repository
<a name="nvidia-drivers-uninstall"></a>

 To remove the NVIDIA repository configuration from your system:

```
[ec2-user ~]$ sudo dnf remove nvidia-release -y
```

**Important**
 Removing the repository configuration does not remove any NVIDIA packages already installed on the system.
