---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2023-08-25-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on August 25, 2023
<a name="release-2023-08-25-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components and includes a platform deprecation announcement.

**Release date:** August 25, 2023

## Changes
<a name="release-2023-08-25-windows.changes"></a>

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
| **Windows security updates** | Applied August 2023 security updates for Windows.<br />See the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Platform deprecation** | Today we're announcing the future retirement for the following platform branches. +  Windows Server 2012 R2 running IIS 8.5 <br />+  Windows Server Core 2012 R2 running IIS 8.5 <br />These platform branches are now *deprecated*.<br />If you currently use these retiring platform branches, we strongly recommend that you start planning your migration to one of the *Windows Server version 2* platforms, which are current and fully supported:+  Windows Server 2019 with IIS 10.0 version 2.x <br />+  Windows Server 2016 with IIS 10.0 version 2.x <br />For full migration considerations, see [Major Version Migration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/dotnet-v2migration.html) in the *AWS Elastic Beanstalk Developer Guide*. <br />Deprecated platform branches aren't listed on the [Supported platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html) page of the *AWS Elastic Beanstalk Platforms* guide. They are listed on a separate page, [Retiring platform versions](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-retiring.html).<br />For more information about platform deprecation, see [Elastic Beanstalk platform support policy](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-support-policy.html) in the *AWS Elastic Beanstalk Developer Guide*.Addendum These release notes previously shared our plans to retire these platform branches on June 30, 2024. In accordance with our platform support policies, we are unable to provide End of Life software to our customers. ***Windows Server 2012 R2* and *Windows Server 2012 R2 Core* platform branches will now retire on December 4, 2023.** On December 4, these platform branches will be removed from Elastic Beanstalk console. Customers can continue to operate existing environments on these platform branches until March 4, 2024, which is 90 days after the December 4 retirement date. <br />Elastic Beanstalk will make Beanstalk Windows 2012 AMIs private after March 4, 2024. This will prevent customers from being able to launch instances in their Beanstalk environments if they are using the default Beanstalk AMI. In order to retain access to the AMIs, customers may copy the AMIs into their accounts to be used in their Beanstalk environments. For detailed instructions, see [Preserving access to an AMI for a retired platform](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.customenv-env-copy.html) in the *AWS Elastic Beanstalk Developer Guide*  |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2023-08-25-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2023-08-25-windows.html)  |
| **.NET Core** | Updated .NET 6 to version 6.0.21 on Windows Server 2019 and 2016 platform versions. |
| **AMI** | Updated the base AMI to version 2023.08.10. |
| **CloudWatch Agent** | Updated the CloudWatch Agent to version 1.300026.1b168. |
| **EC2Launch** | Updated EC2Launch V2 to version 2.0.1521.0. |
| **SSM Agent** | Updated the SSM Agent to version 3.1.2282.0. |

## New platform versions
<a name="release-2023-08-25-windows.platforms"></a>

### .NET on Windows Server
<a name="release-2023-08-25-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.11.7**  |  * 64bit Windows Server 2019 v2.11.7 running IIS 10.0 *  | .NET 6.0.21, supports 6.0.21, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.11.7**  |  * 64bit Windows Server Core 2019 v2.11.7 running IIS 10.0 *  | .NET 6.0.21, supports 6.0.21, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.11.7**  |  * 64bit Windows Server 2016 v2.11.7 running IIS 10.0 *  | .NET 6.0.21, supports 6.0.21, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.11.7**  |  * 64bit Windows Server Core 2016 v2.11.7 running IIS 10.0 *  | .NET 6.0.21, supports 6.0.21, 3.1.32<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2019 with IIS 10.0 version 2.11.7**  | 2023.08.10 | 3.7.617.0 |  | 3.1.2282.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.11.7**  | 2023.08.10 | 3.7.617.0 |  | 3.1.2282.0 | 3.6 | 3.2.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.11.7**  | 2023.08.10 | 3.7.617.0 |  | 3.1.2282.0 | 3.6 | 3.2.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.11.7**  | 2023.08.10 | 3.7.617.0 |  | 3.1.2282.0 | 3.6 | 3.2.0 |
