---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-04-17-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on April 17, 2025
<a name="release-2025-04-17-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk, Windows security updates, and updates framework and AWS components. This release removes support for .NET 6.

**Release date:** April 17, 2025

## Changes
<a name="release-2025-04-17-windows.changes"></a>

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
| **Windows security updates** | Applied April 2025 security updates for Windows.<br />This release includes updates from the monthly Microsoft *Patch Tuesday* Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-04-17-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-04-17-windows.html)  |
| **.NET Core** | Updated .NET 8 to version 8.0.15.<br />.NET 6 is being removed from all Windows Server platform versions because it's past Microsoft's end of support date. For more information, see [.NET and .NET Core Support Policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) on the Microsoft website.+  Windows Server 2016, 2019, 2022 and 2025 platforms — .NET 6 removed  |
| **AMI** | Updated the base AMI to version 2025.04.09. |
| **AWS SDK for .NET** | Updated the SDK to version 3.7.1020.0. |
| **CloudWatch Agent** | Updated the CloudWatch Agent to version 1.300054.0b1074. |
| **EC2Launch** | Updated EC2Launch V2 to version 2.0.2107. |
| **SSM Agent** | Updated the SSM Agent to version 3.3.1957.0. |
| **Deployment logging** | Added timestamps and severity information to deployment logs. |
| **Environment variables** | Fixed an issue where the platform would throw an error when environment variables have empty values. |

## New platform versions
<a name="release-2025-04-17-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2025-04-17-windows.platforms.net)

### .NET on Windows Server
<a name="release-2025-04-17-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2025 with IIS 10.0 version 2.19.0**  |  * 64bit Windows Server 2025 v2.19.0 running IIS 10.0 *  | .NET 8.0.15, supports 8.0.15<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2025 with IIS 10.0 version 2.19.0**  |  * 64bit Windows Server Core 2025 v2.19.0 running IIS 10.0 *  | .NET 8.0.15, supports 8.0.15<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2022 with IIS 10.0 version 2.19.0**  |  * 64bit Windows Server 2022 v2.19.0 running IIS 10.0 *  | .NET 8.0.15, supports 8.0.15<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2022 with IIS 10.0 version 2.19.0**  |  * 64bit Windows Server Core 2022 v2.19.0 running IIS 10.0 *  | .NET 8.0.15, supports 8.0.15<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2019 with IIS 10.0 version 2.19.0**  |  * 64bit Windows Server 2019 v2.19.0 running IIS 10.0 *  | .NET 8.0.15, supports 8.0.15<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.19.0**  |  * 64bit Windows Server Core 2019 v2.19.0 running IIS 10.0 *  | .NET 8.0.15, supports 8.0.15<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.19.0**  |  * 64bit Windows Server 2016 v2.19.0 running IIS 10.0 *  | .NET 8.0.15, supports 8.0.15<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.19.0**  |  * 64bit Windows Server Core 2016 v2.19.0 running IIS 10.0 *  | .NET 8.0.15, supports 8.0.15<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2025 with IIS 10.0 version 2.19.0**  | 2025.04.09 | 3.7.1020.0 |  | 3.3.1957.0 | 3.6 | 3.3.14 |
|  ** Windows Server Core 2025 with IIS 10.0 version 2.19.0**  | 2025.04.09 | 3.7.1020.0 |  | 3.3.1957.0 | 3.6 | 3.3.14 |
|  ** Windows Server 2022 with IIS 10.0 version 2.19.0**  | 2025.04.09 | 3.7.1020.0 |  | 3.3.1957.0 | 3.6 | 3.3.14 |
|  ** Windows Server Core 2022 with IIS 10.0 version 2.19.0**  | 2025.04.09 | 3.7.1020.0 |  | 3.3.1957.0 | 3.6 | 3.3.14 |
|  ** Windows Server 2019 with IIS 10.0 version 2.19.0**  | 2025.04.09 | 3.7.1020.0 |  | 3.3.1957.0 | 3.6 | 3.3.14 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.19.0**  | 2025.04.09 | 3.7.1020.0 |  | 3.3.1957.0 | 3.6 | 3.3.14 |
|  ** Windows Server 2016 with IIS 10.0 version 2.19.0**  | 2025.04.09 | 3.7.1020.0 |  | 3.3.1957.0 | 3.6 | 3.3.14 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.19.0**  | 2025.04.09 | 3.7.1020.0 |  | 3.3.1957.0 | 3.6 | 3.3.14 |
