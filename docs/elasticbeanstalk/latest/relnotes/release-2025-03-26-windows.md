---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-03-26-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on March 26, 2025
<a name="release-2025-03-26-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk, Windows security updates, and updates framework and AWS components. This release also introduces a feature that adds support for Elastic Beanstalk environment variables to store secrets and parameters from AWS Secrets Manager and AWS Systems Manager Parameter Store.

**Release date:** March 26, 2025

## Changes
<a name="release-2025-03-26-windows.changes"></a>

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
| **Windows security updates** | Applied March 2025 security updates for Windows.<br />This release includes updates from the monthly Microsoft *Patch Tuesday* Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-03-26-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2025-03-26-windows.html)  |
| **\*\*New\!\*\* — Elastic Beanstalk supports configuration of environment variables to store secret and parameter data.** | Starting with this release Elastic Beanstalk supports the option to reference AWS Secrets Manager secrets and Systems Manager Parameter Store parameters with environment variables.<br />To learn more about this feature, see [Using Elastic Beanstalk with Secrets Manager and Systems Manager Parameter Store](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.secrets.html). |
| **.NET Core** | Updated .NET 8 to version 8.0.14. |
| **AMI** | Updated the base AMI to version 2025.03.12. |
| **AWS SDK for .NET** | Updated the SDK to version 3.7.1000.0. |
| **CloudWatch Agent** | Updated the CloudWatch Agent to version 1.300053.0b1046. |
| **EC2Launch** | Updated EC2Launch V2 to version 2.0.2081. |
| **AWS X-Ray** | Updated the X-Ray daemon to version 3.3.14. |

## New platform versions
<a name="release-2025-03-26-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2025-03-26-windows.platforms.net)

### .NET on Windows Server
<a name="release-2025-03-26-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2025 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server 2025 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2025 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server Core 2025 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2022 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server 2022 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2022 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server Core 2022 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2019 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server 2019 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server Core 2019 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server 2016 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.18.0**  |  * 64bit Windows Server Core 2016 v2.18.0 running IIS 10.0 *  | .NET 8.0.14, supports 8.0.14, 6.0.36<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2025 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 |
|  ** Windows Server Core 2025 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 |
|  ** Windows Server 2022 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 |
|  ** Windows Server Core 2022 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 |
|  ** Windows Server 2019 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 |
|  ** Windows Server 2016 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.18.0**  | 2025.03.12 | 3.7.1000.0 |  | 3.3.1611.0 | 3.6 | 3.3.14 |
