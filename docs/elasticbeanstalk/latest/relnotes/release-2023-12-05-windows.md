---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2023-12-05-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on December 05, 2023
<a name="release-2023-12-05-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates and updates to framework components, adding support for .NET 8 in this release. It also updates AWS components.

**Release date:** December 05, 2023

## Changes
<a name="release-2023-12-05-windows.changes"></a>

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
| **Windows security updates** | Applied November 2023 security updates for Windows.<br />See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2023-12-05-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2023-12-05-windows.html)  |
| **.NET Core** | Updated .NET 6 to version 6.0.25.<br />Added support for .NET 8. This platform includes .NET 8 version: 8.0.0. |
| **AMI** | Updated the base AMI to version 2023.11.15. |
| **AWS SDK for .NET** | Updated the SDK to version 3.7.686.0. |
| **CloudWatch Agent** | Updated the CloudWatch Agent to version 1.300031.0b313. |
| **SSM Agent** | Updated the SSM Agent to version 3.2.1705.0. |
| **AWSPowershell** | Updated AWSPowershell to version 4.1.447. |

## New platform versions
<a name="release-2023-12-05-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2023-12-05-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.13.0**  |  * 64bit Windows Server 2019 v2.13.0 running IIS 10.0 *  | .NET 8.0.0, supports 8.0.0, 6.0.25<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.13.0**  |  * 64bit Windows Server Core 2019 v2.13.0 running IIS 10.0 *  | .NET 8.0.0, supports 8.0.0, 6.0.25<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.13.0**  |  * 64bit Windows Server 2016 v2.13.0 running IIS 10.0 *  | .NET 8.0.0, supports 8.0.0, 6.0.25<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.13.0**  |  * 64bit Windows Server Core 2016 v2.13.0 running IIS 10.0 *  | .NET 8.0.0, supports 8.0.0, 6.0.25<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.13.0**  | 2023.11.15 | 3.7.686.0 |  | 3.2.1705.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.13.0**  | 2023.11.15 | 3.7.686.0 |  | 3.2.1705.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.13.0**  | 2023.11.15 | 3.7.686.0 |  | 3.2.1705.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.13.0**  | 2023.11.15 | 3.7.686.0 |  | 3.2.1705.0 | 3.6 | 3.2.0 |
