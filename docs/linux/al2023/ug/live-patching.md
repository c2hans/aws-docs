---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/live-patching.html
---

# Kernel Live Patching on AL2023
<a name="live-patching"></a>

You can use Kernel Live Patching for AL2023 to apply specific security vulnerability and critical bug patches to a running Linux kernel without rebooting or disrupting running applications. In addition, Kernel Live Patching can help improve your application's availability while applying these fixes until the system can be rebooted.

AWS releases two types of kernel live patches for AL2023:
+ **Security updates** – Include updates for Linux common vulnerabilities and exposures (CVE). These updates are typically rated as *important* or *critical* using the Amazon Linux Security Advisory ratings. In some cases, AWS might provide updates before a CVE is assigned. In these cases, the patches might appear as bug fixes. Kernel live patches for security updates are provided on a *best-effort basis* -- not all important or critical CVEs may be available as live patches for a given kernel version. To determine whether a specific CVE has been addressed by a live patch, check [ Amazon Linux Security Advisories ](https://alas.aws.amazon.com/alas2023.html).
+ **Bug fixes** – Include fixes for critical bugs and stability issues that aren't associated with CVEs.

AWS provides kernel live patches for an AL2023 kernel version for up to 3 months after its release. After this period, you must update to a later kernel version to continue to receive kernel live patches.

AL2023 kernel live patches are made available as signed RPM packages in the existing AL2023 repositories. The patches can be installed on individual instances using existing **DNF package manager** workflows. Or, they can be installed on a group of managed instances using AWS Systems Manager.

Kernel Live Patching on AL2023 is provided at no additional cost.

**Topics**
+ [Limitations](#live-patching-limitations)
+ [Supported configurations and prerequisites](#live-patching-prereq)
+ [Work with Kernel Live Patching](#working-with-live-patching)

## Limitations
<a name="live-patching-limitations"></a>

While applying a kernel live patch, you can't perform hibernation, use advanced debugging tools (such as `SystemTap`, `kprobes`, and `eBPF`-based tools), or access `ftrace` output files used by the Kernel Live Patching infrastructure.

**Note**
Due to technical limitations, some issues cannot be addressed with live patching. Because of that, these fixes will not be shipped in the kernel live patch package but only in the native kernel package update. You can install the native kernel package and [update and reboot](https://docs.aws.amazon.com/linux/al2023/ug/updating.html) the system to activate the patches as usual.

## Supported configurations and prerequisites
<a name="live-patching-prereq"></a>

Kernel Live Patching is supported on Amazon EC2 instances and on-premises virtual machines that run AL2023.

To use Kernel Live Patching on AL2023, you must use the following:
+ A 64-bit `x86_64` or `ARM64` architecture
+ Kernel version `6.1` or `6.12`

### Policy requirements
<a name="policy-requirements"></a>

To download packages from AL2023 repositories, Amazon EC2 needs access to service owned Amazon S3 buckets. If you are using a Amazon Virtual Private Cloud (VPC) endpoint for Amazon S3 in your environment, ensure that your VPC endpoint policy allows access to those public buckets. The following table describes the Amazon S3 bucket that Amazon EC2 might need to access for Kernel Live Patching.

| S3 bucket ARN | Description |
| --- | --- |
| arn:aws:s3:::al2023-repos-{{region}}-de612dc2/\* | Amazon S3 bucket containing AL2023 repositories |

## Work with Kernel Live Patching
<a name="working-with-live-patching"></a>

You can enable and use Kernel Live Patching on individual instances using the command line on the instance itself. Alternatively, you can enable and use Kernel Live Patching on a group of managed instances using AWS Systems Manager.

The following sections explain how to enable and use Kernel Live Patching on individual instances using the command line.

For more information about enabling and using Kernel Live Patching on a group of managed instances, see [Use Kernel Live Patching on AL2023 instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/kernel-live-patching.html) in the *AWS Systems Manager User Guide*.

**Topics**
+ [Enable Kernel Live Patching](#live-patching-enable)
+ [View the available kernel live patches](#live-patching-view-available)
+ [Apply kernel live patches](#live-patching-apply)
+ [View the applied kernel live patches](#live-patching-view)
+ [Disable Kernel Live Patching](#live-patching-disable)

### Enable Kernel Live Patching
<a name="live-patching-enable"></a>

Kernel Live Patching is disabled by default on AL2023. To use live patching, you must install the **DNF** plugin for Kernel Live Patching and enable the live patching functionality.

**To enable Kernel Live Patching**

1. Kernel live patches are available for AL2023 with kernel version `6.1`. To check your kernel version, run the following command.

   ```
   $ sudo dnf list kernel
   ```

1. Install the **DNF** plugin for Kernel Live Patching.

   ```
   $ sudo dnf install -y kpatch-dnf
   ```

1. Enable the **DNF** plugin for Kernel Live Patching.

   ```
   $ sudo dnf kernel-livepatch -y auto
   ```

   This command also installs the latest version of the kernel live patch RPM from the configured repositories.

1. To confirm that the **DNF** plugin for kernel live patching installed successfully, run the following command.

   When you enable Kernel Live Patching, an empty kernel live patch RPM is automatically applied. If Kernel Live Patching was successfully enabled, this command returns a list that includes the initial empty kernel live patch RPM (and another RPM setting up the DNF repository containing the livepatches).

   ```
   $ sudo rpm -qa | grep kernel-livepatch
   kernel-livepatch-repo-s3-2023.7.20250428-0.amzn2023.noarch
   kernel-livepatch-6.1.134-150.224-1.0-0.amzn2023.x86_64
   ```

1. Install the **kpatch** package.

   ```
   $ sudo dnf install -y kpatch-runtime
   ```

1. Update the **kpatch** service if it was previously installed.

   ```
   $ sudo dnf upgrade kpatch-runtime
   ```

1. Start the **kpatch** service. This service loads all of the kernel live patches upon initialization or at boot.

   ```
   $ sudo systemctl enable kpatch.service && sudo systemctl start kpatch.service
   ```

### View the available kernel live patches
<a name="live-patching-view-available"></a>

Amazon Linux security alerts are published to the Amazon Linux Security Center. For more information about the AL2023 security alerts, including alerts for kernel live patches, see the [Amazon Linux Security Center](https://alas.aws.amazon.com/alas2023.html). Kernel live patches are prefixed with `ALASLIVEPATCH`. The Amazon Linux Security Center might not list kernel live patches that address bugs.

You can also discover the available kernel live patches for advisories and CVEs using the command line.

**To list all available kernel live patches for advisories**
Use the following command.

```
$ sudo dnf updateinfo list
Last metadata expiration check: 1:06:23 ago on Mon 13 Feb 2023 09:28:19 PM UTC.
ALAS2LIVEPATCH-2021-123   important/Sec. kernel-livepatch-6.1.12-17.42-1.0-4.amzn2023.x86_64
ALAS2LIVEPATCH-2022-124   important/Sec. kernel-livepatch-6.1.12-17.42-1.0-3.amzn2023.x86_64
```

**To list all available kernel live patches for CVEs**
Use the following command.

```
$ sudo dnf updateinfo list cves
Last metadata expiration check: 1:07:26 ago on Mon 13 Feb 2023 09:28:19 PM UTC.
CVE-2022-0123    important/Sec. kernel-livepatch-6.1.12-17.42-1.0-4.amzn2023.x86_64
CVE-2022-3210    important/Sec. kernel-livepatch-6.1.12-17.42-1.0-3.amzn2023.x86_64
```

### Apply kernel live patches
<a name="live-patching-apply"></a>

You apply kernel live patches using the **DNF** package manager in the same way that you apply regular updates. The **DNF** plugin for Kernel Live Patching manages the kernel live patches that are available to be applied.

**Tip**
We recommend that you update your kernel regularly using Kernel Live Patching to ensure that it receives specific security fixes until the system can be rebooted. Please also check if additional fixes have been made available to the native kernel package that cannot be deployed as live patches and [update and reboot](https://docs.aws.amazon.com/linux/al2023/ug/updating.html) into the kernel update for those cases.

You can choose to apply a specific kernel live patch, or to apply any available kernel live patches along with your regular security updates.

**To apply a specific kernel live patch**

1. Get the kernel live patch version using one of the commands described in [View the available kernel live patches](#live-patching-view-available).

1. Apply the kernel live patch for your AL2023 kernel.

   ```
   $ sudo dnf install kernel-livepatch-{{kernel_version}}-{{package_version}}.amzn2023.x86_64
   ```

   For example, the following command applies a kernel live patch for AL2023 kernel version `6.1.12-17.42`

   ```
   $ sudo dnf install kernel-livepatch-6.1.12-17.42-1.0-4.amzn2023.x86_64
   ```

**To apply any available kernel live patches along with your regular security updates**
Use the following command.

```
$ sudo dnf upgrade --security
```

Omit the `--security` option to include bug fixes.

**Important**
The kernel version isn't updated after applying kernel live patches. The version is only updated to the new version after the instance is rebooted.
An AL2023 kernel receives kernel live patches for 3 months. After this period, no new kernel live patches are released for that kernel version.
To continue to receive kernel live patches after 3 months, you must reboot the instance to move to the new kernel version. The instance continues to receive kernel live patches for the next 3 months after you update it.
To check the support window for your kernel version, run the following command:

  ```
  $ sudo dnf kernel-livepatch support
  The current version of the Linux kernel you are running will no longer receive live patches after 2025-07-22.
  ```

### View the applied kernel live patches
<a name="live-patching-view"></a>

**To view the applied kernel live patches**
Use the following command.

```
$ sudo kpatch list
Loaded patch modules:
livepatch_CVE_2022_36946 [enabled]

Installed patch modules:
livepatch_CVE_2022_36946 (6.1.57-29.131.amzn2023.x86_64)
livepatch_CVE_2022_36946 (6.1.57-30.131.amzn2023.x86_64)
```

The command returns a list of the loaded and installed security update kernel live patches. The following is example output.

**Note**
A single kernel live patch can include and install multiple live patches.

### Disable Kernel Live Patching
<a name="live-patching-disable"></a>

If you no longer need to use Kernel Live Patching, you can disable it at any time.
+ Disable the use of livepatches:

  1. Disable the plugin:

     ```
     $ sudo dnf kernel-livepatch manual
     ```

  1. Disable the kpatch service:

     ```
     $ sudo systemctl disable --now kpatch.service
     ```
+ Fully remove the livepatch tools:

  1. Remove the plugin:

     ```
     $ sudo dnf remove kpatch-dnf
     ```

  1. Remove kpatch-runtime:

     ```
     $ sudo dnf remove kpatch-runtime
     ```

  1. Remove any installed livepatches:

     ```
     $ sudo dnf remove kernel-livepatch\*
     ```
