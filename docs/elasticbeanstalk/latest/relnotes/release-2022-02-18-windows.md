---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-02-18-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on February 18, 2022
<a name="release-2022-02-18-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** February 18, 2022

**Windows Platform Version 2.8.3**
This release introduced TLS v1.2 to Elastic Beanstalk platform branches on *Windows Server 2019*. Subsequent *Windows Server 2019* platform releases include TLS v1.2 or later versions. For a list of the most recent and supported Windows Server platform versions, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.net) in the *AWS Elastic Beanstalk Platforms* guide.
As of December 31 2023, AWS started fully enforcing TLS 1.2 across all AWS API endpoints. Any environments running *Windows Server 2019* versions that are older than this release still use TLS 1.0 and 1.1. Applications running on these older versions, may no longer be able to perform actions such as configuration deployments, application deployments, auto scaling, new environment launch, log rotation and enhanced health reports.
To avoid the risk of availability impact, please upgrade your platform versions to a newer version as soon as possible.

## Changes
<a name="release-2022-02-18-windows.changes"></a>

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
| **Windows security updates** | Applied February 2022 security updates for Windows.<br />See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-02-18-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2022-02-18-windows.html)  |
| **.NET Core** | Updated .NET 5 to version 5.0.14 on Windows Server 2019 and 2016 platform versions. |
| **AWS SDK for .NET** | Updated the SDK to version 3.15.1546. |
| **AMI** | Updated the base AMI to version 2022.02.10. |
| **SSM Agent** | Updated the SSM Agent to version 3.1.804.0 on Windows Server 2019, 2016 and 2012 R2 platform versions. |
| **EC2Config** | Updated EC2Config to version 4.9.4536 on Windows Server 2012 R2 Core platform versions. |
| **EC2Launch** | Updated EC2Launch agent to version 2.0.698 on Windows Server 2019, 2016 and 2012 R2 platform versions. This does *not* include Windows Server 2012 R2 *Core* platform versions. |

## New platform versions
<a name="release-2022-02-18-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2022-02-18-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.8.3**  |  * 64bit Windows Server 2019 v2.8.3 running IIS 10.0 *  | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.8.3**  |  * 64bit Windows Server Core 2019 v2.8.3 running IIS 10.0 *  | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.8.3**  |  * 64bit Windows Server 2016 v2.8.3 running IIS 10.0 *  | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.8.3**  |  * 64bit Windows Server Core 2016 v2.8.3 running IIS 10.0 *  | .NET 5.0.14, supports 5.0.14, 3.1.22, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.8.3**  |  * 64bit Windows Server 2012 R2 v2.8.3 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.3**  |  * 64bit Windows Server Core 2012 R2 v2.8.3 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.1.30<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.8.3**  | 2022.02.10 | 3.15.1546 |  | 3.1.804.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.8.3**  | 2022.02.10 | 3.15.1546 |  | 3.1.804.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.8.3**  | 2022.02.10 | 3.15.1546 |  | 3.1.804.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.8.3**  | 2022.02.10 | 3.15.1546 |  | 3.1.804.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.8.3**  | 2022.02.10 | 3.15.1546 |  | 3.1.804.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.8.3**  | 2022.02.10 | 3.15.1546 | 4.9.4536 | 3.1.804.0 | 3.6 | 3.2.0 |
