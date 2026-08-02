---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-03-16-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on March 16, 2022
<a name="release-2022-03-16-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** March 16, 2022

## Changes
<a name="release-2022-03-16-windows.changes"></a>

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
| **Windows security updates** | Applied March 2022 security updates for Windows.<br />See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-03-16-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-03-16-windows.html)  |
| **.NET Core** | Updated .NET Core 3 to version 3.1.23 on Windows Server 2019 and 2016 platform versions.<br />Updated .NET 5 to version 5.0.15 on Windows Server 2019 and 2016 platform versions.<br />The following runtime versions are being removed from the listed platform versions, because they're past Microsoft’s end of support dates. For more information, see [.NET and .NET Core Support Policy](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core) on the Microsoft website.[See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-03-16-windows.html) |
| **AWS SDK for .NET** | Updated the SDK to version 3.15.1583. |
| **AMI** | Updated the base AMI to version 2022.03.09. |
| **CloudWatch Agent** | Updated the CloudWatch Agent to version 1.247350.0. |
| **SSM Agent** | Updated the SSM Agent to version 3.1.1045.0 |
| **EC2Config** | Updated EC2Config to version 4.9.4556 on Windows Server 2012 R2 Server Core platform versions. |

## New platform versions
<a name="release-2022-03-16-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2022-03-16-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.9.0**  |  * 64bit Windows Server 2019 v2.9.0 running IIS 10.0 *  | .NET 5.0.15, supports 5.0.15, 3.1.23<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.9.0**  |  * 64bit Windows Server Core 2019 v2.9.0 running IIS 10.0 *  | .NET 5.0.15, supports 5.0.15, 3.1.23<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.9.0**  |  * 64bit Windows Server 2016 v2.9.0 running IIS 10.0 *  | .NET 5.0.15, supports 5.0.15, 3.1.23<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.9.0**  |  * 64bit Windows Server Core 2016 v2.9.0 running IIS 10.0 *  | .NET 5.0.15, supports 5.0.15, 3.1.23<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.9.0**  |  * 64bit Windows Server 2012 R2 v2.9.0 running IIS 8.5 *  | .NET Core 2.1.30, supports 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.9.0**  |  * 64bit Windows Server Core 2012 R2 v2.9.0 running IIS 8.5 *  | .NET Core 2.1.30, supports 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.9.0**  | 2022.03.09 | 3.15.1583 |  | 3.1.1045.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.9.0**  | 2022.03.09 | 3.15.1583 |  | 3.1.1045.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.9.0**  | 2022.03.09 | 3.15.1583 |  | 3.1.1045.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.9.0**  | 2022.03.09 | 3.15.1583 |  | 3.1.1045.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.9.0**  | 2022.03.09 | 3.15.1583 |  | 3.1.1045.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.9.0**  | 2022.03.09 | 3.15.1583 | 4.9.4556 | 3.1.1045.0 | 3.6 | 3.2.0 |
