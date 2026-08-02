---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-08-19-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on August 19, 2025
<a name="release-2025-08-19-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** August 19, 2025

## Changes
<a name="release-2025-08-19-windows.changes"></a>

The following table lists the changes included in this release.

**Notes**
These release notes focus on changes to currently supported platform branches. For full version information of Elastic Beanstalk retiring (deprecated) platform branches, see [Elastic Beanstalk platform versions scheduled for retirement](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html) in the *AWS Elastic Beanstalk Platforms* guide.
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category** | **Description** |
| --- | --- |
| **Framework** | **Details** |
| --- | --- |
| **Component** | **Details** |
| --- | --- |
| **Windows security updates** | Applied August 2025 security updates for Windows.<br />This release includes updates from the monthly Microsoft *Patch Tuesday* Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-08-19-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-08-19-windows.html)  |
| **.NET Core** | Updated .NET 9 to version 9.0.8.<br />Updated .NET 8 to version 8.0.19. |
| **AMI** | Updated the base AMI to version 2025.08.13. |
| **AWS SDK for .NET** | Updated the SDK to version 3.7.1101.0. |
| **CloudWatch Agent** | Updated the CloudWatch Agent to version 1.300057.1b1167. |
| **EC2Launch** | Updated EC2Launch V2 to version 2.2.63. |
| **SSM Agent** | Updated the SSM Agent to version 3.3.2656.0. |

## New platform versions
<a name="release-2025-08-19-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2025-08-19-windows.platforms.net)

### .NET on Windows Server
<a name="release-2025-08-19-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2025 with IIS 10.0 version 2.19.4**  |  * 64bit Windows Server 2025 v2.19.4 running IIS 10.0 *  | .NET 9.0.8, supports 9.0.8, 8.0.19<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2025 with IIS 10.0 version 2.19.4**  |  * 64bit Windows Server Core 2025 v2.19.4 running IIS 10.0 *  | .NET 9.0.8, supports 9.0.8, 8.0.19<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2022 with IIS 10.0 version 2.19.4**  |  * 64bit Windows Server 2022 v2.19.4 running IIS 10.0 *  | .NET 9.0.8, supports 9.0.8, 8.0.19<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2022 with IIS 10.0 version 2.19.4**  |  * 64bit Windows Server Core 2022 v2.19.4 running IIS 10.0 *  | .NET 9.0.8, supports 9.0.8, 8.0.19<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2019 with IIS 10.0 version 2.19.4**  |  * 64bit Windows Server 2019 v2.19.4 running IIS 10.0 *  | .NET 9.0.8, supports 9.0.8, 8.0.19<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.19.4**  |  * 64bit Windows Server Core 2019 v2.19.4 running IIS 10.0 *  | .NET 9.0.8, supports 9.0.8, 8.0.19<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.19.4**  |  * 64bit Windows Server 2016 v2.19.4 running IIS 10.0 *  | .NET 9.0.8, supports 9.0.8, 8.0.19<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.19.4**  |  * 64bit Windows Server Core 2016 v2.19.4 running IIS 10.0 *  | .NET 9.0.8, supports 9.0.8, 8.0.19<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2025 with IIS 10.0 version 2.19.4**  | 2025.08.13 | 3.7.1101.0 |  | 3.3.2656.0 | 3.6 | 3.3.15 |
|  ** Windows Server Core 2025 with IIS 10.0 version 2.19.4**  | 2025.08.13 | 3.7.1101.0 |  | 3.3.2656.0 | 3.6 | 3.3.15 |
|  ** Windows Server 2022 with IIS 10.0 version 2.19.4**  | 2025.08.13 | 3.7.1101.0 |  | 3.3.2656.0 | 3.6 | 3.3.15 |
|  ** Windows Server Core 2022 with IIS 10.0 version 2.19.4**  | 2025.08.13 | 3.7.1101.0 |  | 3.3.2656.0 | 3.6 | 3.3.15 |
|  ** Windows Server 2019 with IIS 10.0 version 2.19.4**  | 2025.08.13 | 3.7.1101.0 |  | 3.3.2656.0 | 3.6 | 3.3.15 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.19.4**  | 2025.08.13 | 3.7.1101.0 |  | 3.3.2656.0 | 3.6 | 3.3.15 |
|  ** Windows Server 2016 with IIS 10.0 version 2.19.4**  | 2025.08.13 | 3.7.1101.0 |  | 3.3.2656.0 | 3.6 | 3.3.15 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.19.4**  | 2025.08.13 | 3.7.1101.0 |  | 3.3.2656.0 | 3.6 | 3.3.15 |
