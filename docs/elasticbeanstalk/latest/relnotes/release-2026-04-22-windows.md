---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-04-22-windows.html
---

# Release: Elastic Beanstalk Windows Server platform update on April 22, 2026
<a name="release-2026-04-22-windows"></a>

This release provides new Windows Server platform versions for AWS Elastic Beanstalk. The release applies Windows security updates. It also updates framework and AWS components. This release adds AI-powered environment analysis and deployment logs to Windows Server platforms.

**Release date:** April 22, 2026

## Changes
<a name="release-2026-04-22-windows.changes"></a>

The following table lists the changes included in this release.

**Note**
Be aware that at the time these release notes are published, the new platform versions might not yet be available in all the AWS Regions that Elastic Beanstalk supports. It might take a few hours for the release to complete.

| **Category** | **Description** |
| --- | --- |
| **Framework** | **Details** |
| --- | --- |
| **Component** | **Details** |
| --- | --- |
| **Windows security updates** | Applied April 2026 security updates for Windows.<br />This release includes updates from the monthly Microsoft *Patch Tuesday* Windows release. Windows security updates in this release are current up to the second Tuesday of the month.<br />For more details and a list of security updates, see the Microsoft [Security Update Guide](https://portal.msrc.microsoft.com/en-us/security-guidance). |
| **Framework updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-04-22-windows.html)  |
| **AWS component updates** |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2026-04-22-windows.html)  |
| **Additional changes with this release** | This release adds AI-powered environment analysis to Windows Server platforms. This feature uses Amazon Bedrock to analyze environment health issues and provide actionable recommendations. It is available through the Elastic Beanstalk console and AWS CLI for environments with enhanced health reporting enabled. To learn more about this feature, see [AI-powered environment analysis](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/health-ai-analysis.html).<br />This release adds deployment logs to Windows Server platforms. You can now view step-by-step deployment logs directly from the Deployments tab in the Elastic Beanstalk console, including while a deployment is still in progress. To learn more, see [Deployment logs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-deployment-logs.html). |
| **.NET Core** | Updated .NET 10 to version [10.0.7](https://github.com/dotnet/core/blob/main/release-notes/10.0/10.0.7/10.0.7.md).<br />Updated .NET 9 to version [9.0.15](https://github.com/dotnet/core/blob/main/release-notes/9.0/9.0.15/9.0.15.md).<br />Updated .NET 8 to version [8.0.26](https://github.com/dotnet/core/blob/main/release-notes/8.0/8.0.26/8.0.26.md). |
| **AMI** | Updated the base AMI to version 2026.04.15. |
| **AWS SDK for .NET** | Updated the SDK to version [3.7.1251.0](https://github.com/aws/aws-sdk-net/releases/tag/3.7.1251.0). |
| **CloudWatch Agent** | Updated the CloudWatch Agent to version [1.300066.1b1374](https://github.com/aws/amazon-cloudwatch-agent/releases/tag/v1.300066.1). |
| **SSM Agent** | Updated the SSM Agent to version [3.3.4121.0](https://github.com/aws/amazon-ssm-agent/releases/tag/3.3.4121.0). |
| **X-Ray daemon** | Updated the X-Ray daemon to version [3.6.2](https://github.com/aws/aws-xray-daemon/releases/tag/v3.6.2). |

## New platform versions
<a name="release-2026-04-22-windows.platforms"></a>

**Topics**
+ [.NET on Windows Server](#release-2026-04-22-windows.platforms.net)

### .NET on Windows Server
<a name="release-2026-04-22-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  ** Windows Server 2025 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server 2025 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server Core 2025 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2022 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server 2022 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server Core 2022 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8.1, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2019 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server 2019 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server Core 2019 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server 2016 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server 2016 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.0**  |  * 64bit Windows Server Core 2016 v2.23.0 running IIS 10.0 *  | .NET 10.0.7, supports 10.0.7, 9.0.15, 8.0.26<br />.NET Framework 4.8, supports 4.x, 2.0 | IIS 10.0 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Launch  |  SSM Agent  |  Web Deploy  |  AWS X-Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  ** Windows Server 2025 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 |
|  ** Windows Server Core 2025 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 |
|  ** Windows Server 2022 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 |
|  ** Windows Server Core 2022 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 |
|  ** Windows Server 2019 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 |
|  ** Windows Server Core 2019 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 |
|  ** Windows Server 2016 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 |
|  ** Windows Server Core 2016 with IIS 10.0 version 2.23.0**  | 2026.04.15 | 3.7.1251.0 | 2.4.0.0 | 3.3.4121.0 | 4.0 | 3.6.2 |
