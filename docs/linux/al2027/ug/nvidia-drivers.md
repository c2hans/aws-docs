---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/nvidia-drivers.html
---

# NVIDIA drivers
<a name="nvidia-drivers"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 Amazon Linux 2027 provides NVIDIA GPU drivers and CUDA Toolkit packages through dedicated repositories. AWS maintains these repositories and provides security advisories through the [Amazon Linux Security Center (ALAS)](https://alas.aws.amazon.com/alas2027.html).

**Topics**
+ [About the NVIDIA repositories](#nvidia-drivers-about)
+ [AL2027 Public Preview limitations](#nvidia-drivers-preview-limitations)
+ [Choosing an NVIDIA driver version](#nvidia-drivers-choosing)
+ [Installing NVIDIA drivers](#nvidia-drivers-install-driver)
+ [Installing CUDA Toolkit](#nvidia-drivers-install-cuda)
+ [Removing the NVIDIA repositories](#nvidia-drivers-uninstall)

## About the NVIDIA repositories
<a name="nvidia-drivers-about"></a>

 For AL2027, we are moving from a single NVIDIA repository to a multi-repository structure:
+  One repository per NVIDIA GPU driver major version (`amazonlinux-nvidia-driver-{{major}}`). For example `amazonlinux-nvidia-driver-580` (Long Term Support Branch) and `amazonlinux-nvidia-driver-595` (Production Branch). Each repository follows the support timeline of the respective NVIDIA driver branch. You can enable repositories for different driver major versions at the same time.
+  A *products* repository (`amazonlinux-nvidia-products`) that provides everything *except* the GPU driver, such as CUDA Toolkit and related packages.

 AWS qualifies NVIDIA software with AL2027 release candidates before redistributing, and provides security advisories for the packages in these repositories.

 New Feature Branch (NFB) drivers are skipped, because they do not receive long-term security support. For more information about NVIDIA driver branches, see [NVIDIA driver lifecycle](https://docs.nvidia.com/datacenter/tesla/drivers/driver-lifecycle.html).

 The repositories are available in all AWS Commercial Regions, as well as the AWS GovCloud (US) Regions and AWS China Regions.

 The repositories provide NVIDIA Tesla (data center compute) and graphics drivers for the `x86_64` architecture only. GRID drivers, used for virtual display and remote workstation capabilities, are not included. For GRID driver installation, see [NVIDIA drivers for your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html) in the *Amazon EC2 User Guide*.

## AL2027 Public Preview limitations
<a name="nvidia-drivers-preview-limitations"></a>

 The following limitations apply to NVIDIA support on AL2027 during Public Preview:

**Important**
 NVIDIA Fabric Manager (`nvidia-fabricmanager`), which coordinates NVSwitch (the interconnect that links multiple GPUs on a single instance), is not yet available in the AL2027 NVIDIA repositories. GPU instances that require Fabric Manager (such as P4d, P5, and P6 instance types) are not yet supported on AL2027.

 NVIDIA Container Toolkit and NVIDIA Data Center GPU Manager (DCGM) are planned but are not yet available in the AL2027 NVIDIA repositories.

## Choosing an NVIDIA driver version
<a name="nvidia-drivers-choosing"></a>

 Each NVIDIA GPU driver major version is served from its own repository. You enroll a driver repository by installing an enrollment package. The enrollment package pulls in the `nvidia-release` package as a dependency, which adds the products repository (CUDA Toolkit and other NVIDIA products) and the NVIDIA GPG keys — so a single install gives you both the driver and products repositories. Choose the enrollment package that matches how you want to track driver versions:

| Enrollment package | Description |
| --- | --- |
| nvidia-release-driver-prod | Tracks the latest NVIDIA Production Branch driver major version. |
| nvidia-release-driver-lts | Tracks the latest NVIDIA Long Term Support Branch driver major version. |
| nvidia-release-driver-latest | Enrolls all supported driver major versions. The corresponding repositories coexist at equal priority, so dnf installs the highest available driver version and rolls forward across major versions as new ones are added. |
| nvidia-release-driver-{{major}} | Enrolls a specific driver major version only (for example, nvidia-release-driver-580). Use this to pin to a major version. |

 To see which driver major versions are currently available, list the enrollment packages. The numeric packages (`nvidia-release-driver-{{major}}`) correspond to the driver major versions that AL2027 provides:

```
[ec2-user ~]$ dnf list available "nvidia-release-driver-*"
```

 To keep the AL2023 behavior — a single enrollment that makes all driver major versions available, with `dnf` installing the latest and rolling forward as new major versions are added — install `nvidia-release-driver-latest`:

```
[ec2-user ~]$ sudo dnf install nvidia-release-driver-latest -y
```

 For example, to track the latest Production Branch driver:

```
[ec2-user ~]$ sudo dnf install nvidia-release-driver-prod -y
```

**Note**
 When more than one driver-major repository is enabled, they coexist at equal priority and `dnf` installs the highest available driver version (Epoch-Version-Release), rolling forward to a newer major version on the next `dnf upgrade`.
 To pin a specific major version, enroll only that version (`nvidia-release-driver-{{major}}`) and do not enroll `nvidia-release-driver-latest`, `-prod`, or `-lts`.
 Removing `nvidia-release-driver-latest` does not by itself pin your version. Because `dnf` distinguishes packages you install explicitly from packages pulled in as dependencies, the outcome depends on how each major version was enrolled:
 A major version you installed *explicitly* stays enrolled after you remove `nvidia-release-driver-latest`. If more than one remains enabled, the highest version still wins.
 A major version that was pulled in *only* as a dependency of `nvidia-release-driver-latest` is removed along with it. If the one enrollment left is the major version you want, you are effectively pinned to it.

## Installing NVIDIA drivers
<a name="nvidia-drivers-install-driver"></a>

 After enrolling a driver repository, you can install NVIDIA driver packages using `dnf`.

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
 To enable NVIDIA persistence mode, enable the `nvidia-persistenced` service (provided by the driver repository):

```
[ec2-user ~]$ sudo systemctl enable --now nvidia-persistenced
```

## Installing CUDA Toolkit
<a name="nvidia-drivers-install-cuda"></a>

 CUDA Toolkit is served from the products repository. If you enrolled a driver repository as described in [Choosing an NVIDIA driver version](#nvidia-drivers-choosing), the products repository is already present (`nvidia-release` was installed as a dependency), so you can install CUDA Toolkit directly:

```
[ec2-user ~]$ sudo dnf install cuda-toolkit -y
```

 To verify that the products repository is available, run `dnf repolist`. You should see the `amazonlinux-nvidia-products` repository in the list:

```
repo id                      repo name                                            status
amazonlinux                  Amazon Linux 2027 repository                         enabled
amazonlinux-nvidia-products  NVIDIA Products repository for Amazon Linux 2027     enabled
```

## Removing the NVIDIA repositories
<a name="nvidia-drivers-uninstall"></a>

 All NVIDIA repository packages — the products repository and each driver repository enrollment packages — depend on `nvidia-release`. Removing `nvidia-release` therefore removes every NVIDIA repository configuration package in the same `dnf` transaction, whatever combination you enrolled:

```
[ec2-user ~]$ sudo dnf remove nvidia-release -y
```

 To remove only a single driver repository, remove that driver's enrollment package instead. `dnf` also removes any alias enrollment package (`nvidia-release-driver-prod`, `-lts`, or `-latest`) that depends on the major version you remove:

```
[ec2-user ~]$ sudo dnf remove nvidia-release-driver-{{major}} -y
```

**Important**
 Removing repository configuration does not remove NVIDIA packages that are already installed, such as the GPU driver or CUDA Toolkit. Remove those packages separately if you no longer need them.
