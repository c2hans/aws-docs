---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-21-windows.html
---

# Release: AWS Elastic Beanstalk Windows Server platform update on December 21, 2018
<a name="release-2018-12-21-windows"></a>

This release applies Windows December 2018 security updates to the Windows Server platform for Elastic Beanstalk, and updates platform configurations. The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** December 21, 2018

## Changes
<a name="release-2018-12-21-windows.changes"></a>

| **Category** | **Description** |
| --- | --- |
| **Instance type** | **Regions** |
| --- | --- |
| **Windows security updates** | Applied December 2018 security updates for Windows.<br />See Microsoft's [Security TechCenter](https://portal.msrc.microsoft.com/en-us/) and [Security Advisories and Bulletins](https://technet.microsoft.com/en-us/library/security/). |
| **Instance types** | Added support for more Amazon EC2 instance types in some AWS Regions, as follows:[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-21-windows.html) |
| **T3** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-21-windows.html)  |
| **C5n** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-21-windows.html)  |
| **R5d** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-21-windows.html)  |
| **R5, C5d, M5d** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2018-12-21-windows.html)  |

## Updated platform configurations
<a name="release-2018-12-21-windows.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2018-12-21-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Configuration  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server Core 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  **Windows Server 2012 with IIS 8 version 1.2.0**  |  * 64bit Windows Server 2012 v1.2.0 running IIS 8 *  | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 |
|  **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**  |  * 64bit Windows Server 2008 R2 v1.2.0 running IIS 7.5 *  | .NET Core 2.1.6, supports 2.1.6, 2.0.9, 1.1.10, 1.0.13<br />.NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 |
|  **Windows Server 2012 R2 with IIS 8.5**  |  * 64bit Windows Server 2012 R2 running IIS 8.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  |  * 64bit Windows Server Core 2012 R2 running IIS 8.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  **Windows Server 2012 with IIS 8**  |  * 64bit Windows Server 2012 running IIS 8 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 8 |
|  **Windows Server 2008 R2 with IIS 7.5**  |  * 64bit Windows Server 2008 R2 running IIS 7.5 *  | .NET Framework 4.7.2, supports 4.x, 2.0, 1.x | IIS 7.5 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Configuration  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  | 2018.12.12 | 3.3.420.0 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.274.0 | 3.6 | 1.0.0 |
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  | 2018.12.12 | 3.3.420.0 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.274.0 | 3.6 | 1.0.0 |
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  | 2018.12.12 | 3.3.420.0 | 4.9.3067 | 2.3.235.0 | 3.6 | 1.0.0 |
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  | 2018.12.12 | 3.3.420.0 | 4.9.3067 | 2.3.235.0 | 3.6 | 1.0.0 |
|  **Windows Server 2012 with IIS 8 version 1.2.0**  | 2018.12.12 | 3.3.420.0 | 4.9.3067 | 2.3.235.0 | 3.6 | 1.0.0 |
|  **Windows Server 2008 R2 with IIS 7.5 version 1.2.0**  | 2018.12.12 | 3.3.420.0 | 4.9.3067 | 2.3.235.0 | 3.6 | 1.0.0 |
|  **Windows Server 2012 R2 with IIS 8.5**  | 2018.12.12 | 3.3.420.0 | 4.9.3067 | 2.3.235.0 | 3.6 | 1.0.0 |
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  | 2018.12.12 | 3.3.420.0 | 4.9.3067 | 2.3.235.0 | 3.6 | 1.0.0 |
|  **Windows Server 2012 with IIS 8**  | 2018.12.12 | 3.3.420.0 | 4.9.3067 | 2.3.235.0 | 3.6 | 1.0.0 |
|  **Windows Server 2008 R2 with IIS 7.5**  | 2018.12.12 | 3.3.420.0 | 4.9.3067 | 2.3.235.0 | 3.6 | 1.0.0 |
