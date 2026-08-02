---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2023-03-28-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on March 28, 2023
<a name="release-2023-03-28-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** March 28, 2023

## Changes
<a name="release-2023-03-28-windows.changes"></a>

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
| **Windows security updates** | Applied March 2023 security updates for Windows.<br />See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2023-03-28-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2023-03-28-windows.html)  |
| **.NET Core** | Updated .NET 6 to version 6.0.15 on Windows Server 2019 and 2016 platform versions. |
| **AMI** | Updated the base AMI to version 2023.03.15. |
| **CloudWatch Agent** | Updated the CloudWatch Agent to version 1.247358.0b252413. |
| **EC2Launch** | Updated EC2Launch V2 to version 2.0.1245. |
| **SSM Agent** | Updated the SSM Agent to version 3.1.2144.0 on Windows Server 2012 R2 platform versions. |
| **EC2Config** | Updated EC2Config to version 4.9.5288 on Windows Server Core 2012 R2 platform versions. |

## New platform versions
<a name="release-2023-03-28-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2023-03-27-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.11.2**  |  * 64bit Windows Server 2019 v2.11.2 running IIS 10.0 *  | .NET 6.0.15, supports 6.0.15, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.11.2**  |  * 64bit Windows Server Core 2019 v2.11.2 running IIS 10.0 *  | .NET 6.0.15, supports 6.0.15, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.11.2**  |  * 64bit Windows Server 2016 v2.11.2 running IIS 10.0 *  | .NET 6.0.15, supports 6.0.15, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.11.2**  |  * 64bit Windows Server Core 2016 v2.11.2 running IIS 10.0 *  | .NET 6.0.15, supports 6.0.15, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.11.2**  |  * 64bit Windows Server 2012 R2 v2.11.2 running IIS 8.5 *  | .NET Core 2.1.30, supports 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.2**  |  * 64bit Windows Server Core 2012 R2 v2.11.2 running IIS 8.5 *  | .NET Core 2.1.30, supports 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.11.2**  | 2023.03.15 | 3.15.1998 |  | 3.1.1856.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.11.2**  | 2023.03.15 | 3.15.1998 |  | 3.1.1856.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.11.2**  | 2023.03.15 | 3.15.1998 |  | 3.1.1856.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.11.2**  | 2023.03.15 | 3.15.1998 |  | 3.1.1856.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.11.2**  | 2023.03.15 | 3.15.1998 |  | 3.1.2144.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.11.2**  | 2023.03.15 | 3.15.1998 | 4.9.5288 | 3.1.2144.0 | 3.6 | 3.2.0 |
