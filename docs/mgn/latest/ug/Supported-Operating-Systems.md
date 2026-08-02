---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Operating systems supported by MGN
<a name="Supported-Operating-Systems"></a>

AWS Transform MGN supports replication of physical, virtual or cloud-based source servers for multiple versions of Window and Linux operating systems.

## Supported Windows operating systems
<a name="Supported-Operating-Systems-Windows"></a>

AWS Transform MGN allows replication of physical, virtual or cloud-based source servers to the AWS Cloud for multiple versions of Windows.

### General Notes
<a name="General-Notes"></a>

**Important**
** Support deprecation notes**
 **Windows 2003**: Effective February 15, 2026, this operating system is no longer supported.
**Windows 2008**: Effective December 30, 2026, this operating system is no longer supported.
**Windows 7**: Effective December 30, 2026, this operating system is no longer supported.
+ [Review the AWS Replication Agent installation requirements.](installation-requirements.md)
+ Windows source servers require a minimum of 2 GB of free disk space to launch a test or cutover instance.
+ The WMI service must be activated to install the AWS Replication Agent.

**These Windows operating systems are supported:**

| Operating system | Supported versions | Prerequisites and Limitations |
| --- | --- | --- |
| Microsoft Windows Server 2025 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  |
| Microsoft Windows Server 2022 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  |
| Microsoft Windows Server 2019 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  |
| Microsoft Windows Server 2016 64-bit |  | Requires .Net Framework version 4.5 or above to be installed by the end user.  |
| Microsoft Windows 11 64-bit |   | Ensure that the [auto sleep function](https://support.microsoft.com/en-us/windows/shut-down-sleep-or-hibernate-your-pc-2941d165-7d0a-a5e8-c5ad-8c972e8e6eff) is disabled. Data replication may be interrupted if the feature is activated. |
| Microsoft Windows 10 64-bit |   | Ensure that the [auto sleep function in Windows 10](https://answers.microsoft.com/en-us/windows/forum/all/turn-off-auto-sleep-in-windows-10/79f2d86c-3378-495f-8da2-4d78021876d4) is disabled. Data replication may be interrupted if the feature is activated. |
| Microsoft Windows Server 2012 <br />This version has reached end of life. We recommend that you update to a more recent version. | 64-bit and R2 64-bit | Requires .Net Framework version 4.5 or above to be installed by the end user. |
| Microsoft Windows Server 2008 <br />This version has reached end of life. We recommend that you update to a more recent version. | 64-bit and R2 64-bit | [See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)  |
| Microsoft Windows Server 2003 64-bit<br />This version has reached end of life. We recommend that you update to a more recent version. |  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)  |
| Microsoft Windows 7 64-bit<br />This version has reached end of life. We recommend that you update to a more recent version. |  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)  |

## Supported Linux operating systems
<a name="Supported-Operating-Systems-Linux"></a>

### General Notes
<a name="General-Notes"></a>

**Important**
** Support deprecation notes **
**Red Hat Enterprise Linux (RHEL) version 5.x and CentOS version 5.x**: Effective December 30, 2025, these operating systems are no longer supported.
**Debian 6.x- 9.x**: Effective April 30, 2026, these operating systems are no longer supported.
**Ubuntu 12.04**: Effective August 20, 2026, this operating system is no longer supported.
**Oracle versions 6.x**: Effective August 28, 2026, these operating systems are no longer supported.
**CentOS versions 6.x**: Effective August 28, 2026, these operating systems are no longer supported.
**SLES versions 11.x**: Effective August 28, 2026, these operating systems are no longer supported.
**CentOS 7-7.9**: Effective November 20, 2026, these operating systems are no longer supported.
**Amazon Linux 1 (AL1)**: Effective November 20, 2026, this operating system is no longer supported.
**Ubuntu 14.04**: Effective December 20, 2026, this operating system is no longer supported.
**Debian 10**: Effective December 30, 2026, this operating system is no longer supported.
**Red Hat Enterprise Linux (RHEL) versions 6.x**: Effective December 30, 2026, these operating systems are no longer supported.
**CentOS versions 8.x**: Effective December 30, 2026, these operating systems are no longer supported.
+ [Review the AWS Replication Agent installation requirements.](installation-requirements.md)
+ MGN does not support 32 bit versions of Linux.
+ For source machines configured with LVM, on RHEL/Oracle version less than or equal to 9.4, please make sure to update the lvm package to `lvm2-2.03.23-1.el9` or latest.
+  Kernel version 4.9.256 is not supported. Agent installation fails on servers that run this kernel version.
+  Kernel versions earlier than 2.6.18-164 are not supported by AWS Transform MGN. Therefore, servers that run these kernel versions cannot be replicated by AWS Transform MGN.

**These Linux operating systems are supported:**

| Operating system | Supported versions | Prerequisites and Limitations |
| --- | --- | --- |
| Amazon Linux | 1, 2, 2023 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)  |
| RHEL | 6.0 to 9.8, 10, 10.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)  |
| CentOS | 6.0 to 8.0, Stream 9, Stream 10 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)  |
| Oracle Linux | 6.0 to 7.8, 8.5 to 8.9, 9.0 to 9.4, 9.7, and 10.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)  |
| Rocky Linux | 8 to 9.8, 10, 10.1 | For Rocky Linux 8.x, a prerequisite is to run `$ sudo yum install elfutils-libelf-devel`  |
| SUSE Linux Enterprise Server | 11 SP4 to 15 SP7 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)  |
| Ubuntu | 12.04 to 24.04 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)  |
| Debian | 10 to 11 |  Only Kernel 3.x or above are supported  |
| AlmaLinux | 9.6, 9.7, 9.8, 10, 10.1 | Before you install the agent on AlmaLinux, complete the following prerequisites:[See the AWS documentation website for more details](http://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html) |
