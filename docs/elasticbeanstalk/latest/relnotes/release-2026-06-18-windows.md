---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-06-18-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on June 18, 2026
<a name="release-2026-06-18-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** June 18, 2026

## Changes
<a name="release-2026-06-18-windows.changes"></a>

The following table lists the changes included in this release.

**Note**
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category** | **Description** |
| --- | --- |
| **Framework** | **Details** |
| --- | --- |
| **Component** | **Details** |
| --- | --- |
| **Windows security updates** | Applied June 2026 security updates for Windows.<br />This release includes updates from the monthly Microsoft *Patch Tuesday* Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-06-18-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-06-18-windows.html)  |
| **.NET Core** | Updated .NET 10 to version [10.0.9](https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.9/10.0.9.md).<br />Updated .NET 9 to version [9.0.17](https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.17/9.0.17.md).<br />Updated .NET 8 to version [8.0.28](https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.28/8.0.28.md). |
| **AMI** | Updated the base AMI to version 2026.06.10. |
| **AWS SDK for .NET** | Updated the SDK to version [3.7.1252.1](https://github.com/aws/aws-sdk-net/releases/tag/3.7.1252.1) (Windows Server 2016, 2019, and 2022 platforms only). |
| **CloudWatch Agent** | Updated the CloudWatch Agent to version [1.300069.0b1529](https://github.com/aws/amazon-cloudwatch-agent/releases/tag/v1.300069.0). |
| **EC2Launch** | Updated EC2Launch to version 2.5.1. |
| **SSM Agent** | Updated the SSM Agent to version [3.3.4515.0](https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.4515.0). |
| **X-Ray daemon** | Updated the X-Ray daemon to version [3.6.5](https://github.com/aws/aws-xray-daemon/releases/tag/v3.6.5). |

## New platform versions
<a name="release-2026-06-18-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2026-06-18-windows.platforms.net)

### .NET on Windows Server
<a name="release-2026-06-18-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2025 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server 2025 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server Core 2025 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2022 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server 2022 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server Core 2022 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2019 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server 2019 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server Core 2019 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server 2016 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.2**  |  * 64bit Windows Server Core 2016 v2.23.2 running IIS 10.0 *  | .NET 10.0.9, supports 10.0.9, 9.0.17, 8.0.28<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2025 with IIS 10.0 version 2.23.2**  | 2026.06.10 |  | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 |
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.2**  | 2026.06.10 |  | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 |
|  ** Windows Server 2022 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 |
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 |
|  ** Windows Server 2019 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 |
|  ** Windows Server 2016 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.2**  | 2026.06.10 | 3.7.1252.1 | 2.5.1 | 3.3.4515.0 | 4.0 | 3.6.5 |
