---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-10-28-windows.html
---

# Release: AWS Elastic Beanstalk Windows Server platform update on October 28, 2019
<a name="release-2019-10-28-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also adds support for .NET Core 3.0.0, removes Windows Server 2008 platform versions, and adds support for additional Amazon EC2 instance types in certain AWS Regions.

**Release date:** October 28, 2019

## Changes
<a name="release-2019-10-28-windows.changes"></a>

| **Category** | **Description** |
| --- | --- |
| **OS** | **Details** |
| --- | --- |
| **Framework** | **Details** |
| --- | --- |
| **Instance types** | **Regions** |
| --- | --- |
| **Windows security updates** | Applied October 2019 security updates for Windows.<br />See Microsoft's [Security TechCenter](https://portal.msrc.microsoft.com/en-us/) and [Security Advisories and Bulletins](https://technet.microsoft.com/en-us/library/security/). |
| **Operating system updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-10-28-windows.html)  |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-10-28-windows.html)  |
| **Instance types** | Added support for more Amazon EC2 instance types in some AWS Regions, as follows: [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-10-28-windows.html)<br />For more information about G4 instances, see [Amazon EC2 G4 Instances](https://aws.amazon.com/ec2/instance-types/g4/). |
| **Windows 2008 Server** | Removed Windows 2008 Server platform versions. They had been previously available as retiring platforms, with an announced end date of October 16, 2019. For more information from Microsoft, see [Prepare for Windows Server 2008 end of support](https://www.microsoft.com/en-us/cloud-platform/windows-server-2008). |
| **.NET Core 3.0** *New* | Added support for .NET Core 3.0. For details from Microsoft, see [What's new in .NET Core 3.0](https://docs.microsoft.com/en-us/dotnet/core/whats-new/dotnet-core-3-0).<br />.NET Core 3.0 supports Windows Server 2012 R2 or later. We don't support it on the Windows Server 2012 platform versions. |
| **g4dn.xlarge, g4dn.2xlarge, g4dn.12xlarge** |  + US East (Ohio) – us-east-2<br />+ US West (N. California) – us-west-1<br />+ Asia Pacific (Sydney) – ap-southeast-2<br />+ Europe (Ireland) – eu-west-1<br />+ Europe (London) – eu-west-2  |

## New platform versions
<a name="release-2019-10-28-windows.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2019-10-24-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2016 with IIS 10.0 version 2.3.0**  |  * 64bit Windows Server 2016 v2.3.0 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.3.0**  |  * 64bit Windows Server Core 2016 v2.3.0 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.3.0**  |  * 64bit Windows Server 2012 R2 v2.3.0 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.0**  |  * 64bit Windows Server Core 2012 R2 v2.3.0 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server 2016 v1.2.0 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server Core 2016 v1.2.0 running IIS 10.0 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2012 with IIS 8 version 1.2.0**  |  * 64bit Windows Server 2012 v1.2.0 running IIS 8 *  | .NET Core 2.2.7, supports 2.2.7, 2.1.13, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 |
|  ** Windows Server 2012 R2 with IIS 8.5 **  |  * 64bit Windows Server 2012 R2 running IIS 8.5 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 **  |  * 64bit Windows Server Core 2012 R2 running IIS 8.5 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2012 with IIS 8 **  |  * 64bit Windows Server 2012 running IIS 8 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2016 with IIS 10.0 version 2.3.0**  | 2019.10.09 | 3.15.846 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.3.0**  | 2019.10.09 | 3.15.846 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.3.0**  | 2019.10.09 | 3.15.846 | 4.9.3519 | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.3.0**  | 2019.10.09 | 3.15.846 | 4.9.3519 | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server 2016 with IIS 10.0 version 1.2.0**  | 2019.10.09 | 3.15.846 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 1.2.0**  | 2019.10.09 | 3.15.846 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  | 2019.10.09 | 3.15.846 | 4.9.3519 | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  | 2019.10.09 | 3.15.846 | 4.9.3519 | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server 2012 with IIS 8 version 1.2.0**  | 2019.10.09 | 3.15.846 | 4.9.3519 | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 **  | 2019.10.09 | 3.15.846 | 4.9.3519 | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 **  | 2019.10.09 | 3.15.846 | 4.9.3519 | 2.3.634.0 | 3.6 | 3.1.0 |
|  ** Windows Server 2012 with IIS 8 **  | 2019.10.09 | 3.15.846 | 4.9.3519 | 2.3.634.0 | 3.6 | 3.1.0 |
