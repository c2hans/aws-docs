---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Linux.html
---

# AWS DRS supported Linux operating systems
<a name="Supported-Operating-Systems-Linux"></a>

## General Notes
<a name="General-Notes"></a>
+ [Review the AWS Replication Agent installation requirements.](installation-requirements.md)
+ Linux kernel versions up to 6.14 are supported.
+ For source machines configured with LVM, on RHEL/Oracle version less than or equal to 9.4, please make sure to update the lvm package to `lvm2-2.03.23-1.el9` or later.
+ AWS Elastic Disaster Recovery does not support 32 bit versions of Linux.
+ Hard reboots, disk changes, and crashes trigger a rescan. Graceful reboots do not trigger a rescan in the following versions:
  + RHEL/CentOS/Oracle Linux 6\+ (kernel versions 2.6.32–431 and above)
  + SUSE 12\+
  + Ubuntu 16\+ LTS
  + AL 2 and AL 2023
  + Rocky 8\+
  + Debian 9\+

**Support removal notices**
The following operating systems are no longer supported, or will no longer be supported after the listed date. AWS does not provide troubleshooting assistance or compatibility fixes for unsupported operating systems.
**RHEL 5.x and CentOS 5.x** — Support ended December 30, 2025.
**Debian 6.x–9.x** — Support ended April 30, 2026.
**Ubuntu 12.04** — Support ends August 20, 2026.
**CentOS 6.x, SUSE (SLES) 11.x, and Oracle Linux 6.x** — Support ends August 28, 2026.

**These Linux operating systems are supported:**

| Operating system | Supported versions | Prerequisites and Limitations |
| --- | --- | --- |
| Amazon Linux | 1, 2, 2023 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Linux.html)  |
| RHEL | 6.0 to 10.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Linux.html)  |
| CentOS | 6.0 to 8.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Linux.html)  |
| Oracle Linux | 6.0 to 7.0, 8.5 to 8.10, and 9.0 to 9.4 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Linux.html)  |
| Rocky Linux | 8, 9.7 | For Rocky Linux 8.x, a prerequisite is to run `$ sudo yum install elfutils-libelf-devel`  |
| SUSE | 11 SP4 to 15 SP5 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Linux.html)  |
| Ubuntu | 12.04 to 24.04 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Linux.html)  |
| Debian | 10 to 13 |  Only Kernel 3.x or above are supported  |
