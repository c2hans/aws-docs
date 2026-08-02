---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2020-09-04-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on September 4, 2020
<a name="release-2020-09-04-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components.

**Release date:** September 4, 2020

## Changes
<a name="release-2020-09-04-windows.changes"></a>

The following table lists the changes included in this release.

**Note**
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category** | **Description** |
| --- | --- |
| **Framework** | **Details** |
| --- | --- |
| **Component** | **Details** |
| --- | --- |
| **Windows security updates** | Applied August 2020 security updates for Windows.<br />See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2020-09-04-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2020-09-04-windows.html)  |
| **.NET Core** | Updated .NET Core 3.1 to version 3.1.7.<br />Updated .NET Core 2.1 to version 2.1.21. |
| **AWS SDK for .NET** | Updated the SDK to version 3.15.1084. |
| **AMI** | Updated the base AMI to version 2020.08.12. |

## New platform versions
<a name="release-2020-09-04-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2020-09-04-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.5.9**  |  * 64bit Windows Server 2019 v2.5.9 running IIS 10.0 *  | .NET Core 3.1.7, supports 3.1.7, 2.2.8, 2.1.21<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.5.9**  |  * 64bit Windows Server Core 2019 v2.5.9 running IIS 10.0 *  | .NET Core 3.1.7, supports 3.1.7, 2.2.8, 2.1.21<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.5.9**  |  * 64bit Windows Server 2016 v2.5.9 running IIS 10.0 *  | .NET Core 3.1.7, supports 3.1.7, 2.2.8, 2.1.21<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.5.9**  |  * 64bit Windows Server Core 2016 v2.5.9 running IIS 10.0 *  | .NET Core 3.1.7, supports 3.1.7, 2.2.8, 2.1.21<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.5.9**  |  * 64bit Windows Server 2012 R2 v2.5.9 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.21<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.9**  |  * 64bit Windows Server Core 2012 R2 v2.5.9 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.21<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.5.9**  | 2020.08.12 | 3.15.1084 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.842.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.5.9**  | 2020.08.12 | 3.15.1084 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.842.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.5.9**  | 2020.08.12 | 3.15.1084 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.842.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.5.9**  | 2020.08.12 | 3.15.1084 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.842.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.5.9**  | 2020.08.12 | 3.15.1084 | 4.9.4222 | 2.3.842.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.5.9**  | 2020.08.12 | 3.15.1084 | 4.9.4222 | 2.3.842.0 | 3.6 | 3.2.0 |
