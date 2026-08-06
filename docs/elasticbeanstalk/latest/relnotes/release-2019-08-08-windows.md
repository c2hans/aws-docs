---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-08-08-windows.html
---

# Release: AWS Elastic Beanstalk Windows Server platform update on August 8, 2019
<a name="release-2019-08-08-windows"></a>

This release applies Windows July 2019 security updates to the Windows Server platform for Elastic Beanstalk, and updates platform versions. The release also adds Amazon EC2 instance types in certain AWS Regions.

**Release date:** August 8, 2019

## Changes
<a name="release-2019-08-08-windows.changes"></a>

| **Category** | **Description** |
| --- | --- |
| **Instance types** | **Regions** |
| --- | --- |
| **Windows security updates** | Applied July 2019 security updates for Windows.<br />See Microsoft's [Security TechCenter](https://portal.msrc.microsoft.com/en-us/) and [Security Advisories and Bulletins](https://technet.microsoft.com/en-us/library/security/). |
| **Instance types** | Added support for more Amazon EC2 instance types in some AWS Regions, as follows: [See the AWS documentation website for more details](http://docs.aws.amazon.com/elasticbeanstalk/latest/relnotes/release-2019-08-08-windows.html) |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, m5a.16xlarge,**<br />**r5a.8xlarge, r5a.16xlarge, T3a** |  + US East (Ohio) – us-east-2  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge, M5a, R5a, T3a** |  + US West (N. California) – us-west-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, r5.8xlarge, r5.16xlarge,**<br />**r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, m5a.16xlarge, r5a.8xlarge** |  + US West (Oregon) – us-west-2  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge** |  + Asia Pacific (Hong Kong) – ap-east-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge** |  + Asia Pacific (Mumbai) – ap-south-1<br />+ Asia Pacific (Seoul) – ap-northeast-2<br />+ Canada (Central) – ca-central-1<br />+ Europe (London) – eu-west-2<br />+ Europe (Paris) – eu-west-3<br />+ Europe (Stockholm) – eu-north-1  |
| **M5, M5d, R5, R5d** |  + Asia Pacific (Osaka) – ap-northeast-3  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, m5a.16xlarge,**<br />**r5a.8xlarge, r5a.16xlarge** |  + Asia Pacific (Singapore) – ap-southeast-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.metal, r5d.8xlarge, r5d.16xlarge, r5d.metal** |  + Asia Pacific (Tokyo) – ap-northeast-1  |
| **r5.8xlarge, r5.16xlarge, r5d.8xlarge, M5, M5d, T3a** |  + China (Beijing) – cn-north-1  |
| **r5d.8xlarge, r5d.16xlarge, M5, M5d, T3a** |  + China (Ningxia) – cn-northwest-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, r5.8xlarge, r5.16xlarge,**<br />**r5d.8xlarge, r5d.16xlarge, m5a.large, m5a.xlarge, m5a.2xlarge,**<br />**m5a.4xlarge, m5a.8xlarge, m5a.12xlarge, m5a.24xlarge, r5a.large,**<br />**r5a.xlarge, r5a.2xlarge, r5a.4xlarge, r5a.8xlarge, r5a.12xlarge,**<br />**r5a.24xlarge** |  + Europe (Frankfurt) – eu-central-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge, m5a.8xlarge, r5a.8xlarge,**<br />**T3a** |  + Europe (Ireland) – eu-west-1  |
| **m5.8xlarge, m5.16xlarge** |  + South America (São Paulo) – sa-east-1  |
| **m5.8xlarge, m5.16xlarge, m5d.8xlarge, m5d.16xlarge, r5.8xlarge,**<br />**r5.16xlarge, r5d.8xlarge, r5d.16xlarge, T3a** |  + AWS GovCloud (US-East) – us-gov-east-1<br />+ AWS GovCloud (US-West) – us-gov-west-1  |
| **g3.4xlarge, g3.8xlarge, g3.16xlarge** |  + China (Beijing) – cn-north-1<br />+ Europe (London) – eu-west-2  |
| **g3s.xlarge** |  + Europe (London) – eu-west-2  |

## New platform versions
<a name="release-2019-08-08-windows.platforms"></a>

### .NET on Windows Server with IIS
<a name="release-2019-08-08-windows.platforms.net"></a>

#### Configuration basics
<a name="platforms-supported.net.basics"></a>

****

|  Platform Version  |  Solution Stack Name  |  Framework  |  Proxy Server  |
| --- | --- | --- | --- |
|  **Windows Server 2016 with IIS 10.0 version 2.2.0**  |  * 64bit Windows Server 2016 v2.2.0 running IIS 10.0 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  **Windows Server Core 2016 with IIS 10.0 version 2.2.0**  |  * 64bit Windows Server Core 2016 v2.2.0 running IIS 10.0 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  **Windows Server 2012 R2 with IIS 8.5 version 2.2.0**  |  * 64bit Windows Server 2012 R2 v2.2.0 running IIS 8.5 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.0**  |  * 64bit Windows Server Core 2012 R2 v2.2.0 running IIS 8.5 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  |  * 64bit Windows Server Core 2016 v1.2.0 running IIS 10.0 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 10.0 |
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  |  * 64bit Windows Server Core 2012 R2 v1.2.0 running IIS 8.5 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  **Windows Server 2012 with IIS 8 version 1.2.0**  |  * 64bit Windows Server 2012 v1.2.0 running IIS 8 *  | .NET Core 2.2.6, supports 2.2.6, 2.1.12, 2.0.9, 1.1.14, 1.0.16<br />.NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 |
|  **Windows Server 2012 R2 with IIS 8.5**  |  * 64bit Windows Server 2012 R2 running IIS 8.5 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  |  * 64bit Windows Server Core 2012 R2 running IIS 8.5 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8.5 |
|  **Windows Server 2012 with IIS 8**  |  * 64bit Windows Server 2012 running IIS 8 *  | .NET Framework 4.8, supports 4.x, 2.0, 1.x | IIS 8 |

#### More details
<a name="platforms-supported.net.details"></a>

****

|  Platform Version  |  AMI version  |  AWS SDK for .NET  |  EC2Config  |  SSM Agent  |  Web Deploy  |  AWS X‑Ray  |
| --- | --- | --- | --- | --- | --- | --- |
|  **Windows Server 2016 with IIS 10.0 version 2.2.0**  | 2019.07.12 | 3.15.780 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server Core 2016 with IIS 10.0 version 2.2.0**  | 2019.07.12 | 3.15.780 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server 2012 R2 with IIS 8.5 version 2.2.0**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 2.2.0**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server 2016 with IIS 10.0 version 1.2.0**  | 2019.07.12 | 3.15.780 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server Core 2016 with IIS 10.0 version 1.2.0**  | 2019.07.12 | 3.15.780 |  * [SSM only](https://docs.aws.amazon.com/systems-manager/latest/userguide/) *  | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server 2012 R2 with IIS 8.5 version 1.2.0**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server 2012 R2 Server Core with IIS 8.5 version 1.2.0**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server 2012 with IIS 8 version 1.2.0**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server 2012 R2 with IIS 8.5**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server 2012 R2 Server Core with IIS 8.5**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 |
|  **Windows Server 2012 with IIS 8**  | 2019.07.12 | 3.15.780 | 4.9.3429 | 2.3.542.0 | 3.6 | 3.1.0 |
