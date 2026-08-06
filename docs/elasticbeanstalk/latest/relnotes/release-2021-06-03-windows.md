---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2021-06-03-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on June 3, 2021
<a name="release-2021-06-03-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components and includes a platform deprecation announcement.

**Release date:** June 3, 2021

## Changes
<a name="release-2021-06-03-windows.changes"></a>

The following table lists the changes included in this release.

**Note**
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category** | **Description** |
| --- | --- |
| **Framework** | **Details** |
| --- | --- |
| **Component** | **Details** |
| --- | --- |
| **Windows security updates** | Applied May 2021 security updates for Windows.<br />See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Platform deprecation** | Today we're announcing that platform branch **Windows Server 2012 with IIS 8** *will retire on May 31, 2022*. *This platform branch is now deprecated.* This retiring platform branch is composed of two platform versions: *Windows Server 2012 with IIS 8* **version 0.1.0** and *Windows Server 2012 with IIS 8* **version 1.2.0**. <br />If you currently use this retiring platform branch, we strongly recommend that you start planning your migration to one of the *Windows Server version 2* platforms, which are current and fully supported:+  Windows Server 2019 with IIS 10.0 version 2.x <br />+  Windows Server 2016 with IIS 10.0 version 2.x <br />+  Windows Server 2012 R2 with IIS 8.5 version 2.x <br />For full migration considerations, see [Major Version Migration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-v2migration.html) in the *AWS Elastic Beanstalk Developer Guide*. <br />Deprecated platform branches aren't listed on the [Supported platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html) page of the *AWS Elastic Beanstalk Platforms* guide. They are listed on a separate page, [Retiring platform versions](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html).<br />For more information about platform deprecation, see [Elastic Beanstalk platform support policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html) in the *AWS Elastic Beanstalk Developer Guide*. |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2021-06-03-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2021-06-03-windows.html)  |
| **.NET Core** | Updated .NET Core 2.1 to version 2.1.28.<br />Updated .NET Core 3 to version 3.1.15 on Windows Server 2019 and 2016 platform versions.<br />Updated .NET 5 to version 5.0.6 on Windows Server 2019 and 2016 platform versions. |
| **AWS SDK for .NET** | Updated the SDK to version 3.15.1302. |
| **AMI** | Updated the base AMI to version 2021.05.11. |
| **EC2Config** | Updated EC2Config to version 4.9.4381 on Windows Server 2012 platform versions. |
| **CloudWatch Agent** | Updated the CloudWatch Agent to version 1.247347.6. |

## New platform versions
<a name="release-2021-06-03-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2021-06-03-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.6.6**  |  * 64bit Windows Server 2019 v2.6.6 running IIS 10.0 *  | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.6.6**  |  * 64bit Windows Server Core 2019 v2.6.6 running IIS 10.0 *  | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.6.6**  |  * 64bit Windows Server 2016 v2.6.6 running IIS 10.0 *  | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.6.6**  |  * 64bit Windows Server Core 2016 v2.6.6 running IIS 10.0 *  | .NET 5.0.6, supports 5.0.6, 3.1.15, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.6.6**  |  * 64bit Windows Server 2012 R2 v2.6.6 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.6**  |  * 64bit Windows Server Core 2012 R2 v2.6.6 running IIS 8.5 *  | .NET Core 3.0.0, supports 3.0.0, 2.2.8, 2.1.28<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.6.6**  | 2021.05.11 | 3.15.1302 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.6.6**  | 2021.05.11 | 3.15.1302 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.6.6**  | 2021.05.11 | 3.15.1302 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.6.6**  | 2021.05.11 | 3.15.1302 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 3.0.529.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2012 R2 with IIS 8.5 version 2.6.6**  | 2021.05.11 | 3.15.1302 | 4.9.4381 | 3.0.529.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2012 R2 Server Core with IIS 8.5 version 2.6.6**  | 2021.05.11 | 3.15.1302 | 4.9.4381 | 3.0.529.0 | 3.6 | 3.2.0 |
