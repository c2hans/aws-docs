---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/supported-aws-regions.html
---

# Supported AWS Regions
<a name="supported-aws-regions"></a>

 This guidance uses services which may not be currently available in all AWS Regions. Launch this guidance in an AWS Region where required services are available. For the most current availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/?nc1=h_ls).

 Clickstream Analytics on AWS provides two types of authentication for its web console, [Amazon Cognito User Pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) and [OpenID Connect (OIDC) Provider](https://openid.net/connect/). You must choose to launch the guidance with OpenID Connect in case one of the following scenarios:
+  Amazon Cognito User Pool is not available in your AWS Region.
+  You already have an OpenID Connect Provider and want to authenticate against it.

 **Supported Regions for web console deployment**

|  Region Name  |  Launch with Amazon Cognito user pool  |  Launch with OpenID Connect  |
| --- | --- | --- |
|  US East (N. Virginia)  |  Yes  |  Yes  |
|  US East (Ohio)  |  Yes  |  Yes  |
|  US West (N. California)  |  Yes  |  Yes  |
|  US West (Oregon)  |  Yes  |  Yes  |
|  Africa (Cape Town)  |  No  |  Yes  |
|  Asia Pacific (Hong Kong)  |  No  |  Yes  |
|  Asia Pacific (Jakarta)  |  No  |  Yes  |
|  Asia Pacific (Mumbai)  |  Yes  |  Yes  |
|  Asia Pacific (Osaka)  |  No  |  Yes  |
|  Asia Pacific (Seoul)  |  Yes  |  Yes  |
|  Asia Pacific (Singapore)  |  Yes  |  Yes  |
|  Asia Pacific (Sydney)  |  Yes  |  Yes  |
|  Asia Pacific (Tokyo)  |  Yes  |  Yes  |
|  Canada (Central)  |  Yes  |  Yes  |
|  Europe (Frankfurt)  |  Yes  |  Yes  |
|  Europe (Ireland)  |  Yes  |  Yes  |
|  Europe (London)  |  Yes  |  Yes  |
|  Europe (Milan)  |  No  |  Yes  |
|  Europe (Paris)  |  Yes  |  Yes  |
|  Europe (Stockholm)  |  Yes  |  Yes  |
|  Middle East (Bahrain)  |  No  |  Yes  |
|  South America (Sao Paulo)  |  Yes  |  Yes  |
|  China (Beijing) Region Operated by Sinnet  |  No  |  Yes  |
|  China (Ningxia) Region Operated by NWCD  |  No  |  Yes  |

 This guidance provides [modular components](architecture-overview.md#architecture-diagram) for supporting different data pipeline architecture. The data processing, and reporting modules are optional, that is, you can create a data pipeline without data processing and reporting modules if needed.

 **Pipeline modules availability**

|  Region Name  |  Data ingestion with MSK as buffer  |  Data ingestion with KDS as buffer  |  Data ingestion with S3 as buffer  |  Data processing  |  Data modeling with Redshift Serverless  |  Data modeling with Provisioned Redshift  |  Reporting with QuickSight  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  US East (N. Virginia)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  US East (Ohio)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  US West (N. California)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  No  |
|  US West (Oregon)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Africa (Cape Town)  |  Yes  |  Yes  |  Yes  |  No  |  No  |  No  |  No  |
|  Asia Pacific (Hong Kong)  |  Yes  |  Yes  |  Yes  |  Yes  |  No  |  Yes  |  No  |
|  Asia Pacific (Mumbai)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Asia Pacific (Osaka)  |  Yes  |  Yes  |  Yes  |  No  |  No  |  No  |  No  |
|  Asia Pacific (Seoul)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Asia Pacific (Singapore)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Asia Pacific (Sydney)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Asia Pacific (Tokyo)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Canada (Central)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Europe (Frankfurt)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Europe (Ireland)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Europe (London)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Europe (Milan)  |  Yes  |  Yes  |  Yes  |  No  |  No  |  No  |  No  |
|  Europe (Paris)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Europe (Stockholm)  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |
|  Middle East (Bahrain)  |  Yes  |  Yes  |  Yes  |  Yes  |  No  |  Yes  |  No  |
|  South America (Sao Paulo)  |  Yes  |  Yes  |  Yes  |  Yes  |  No  |  Yes  |  Yes  |
|  China (Beijing) Region Operated by Sinnet\*  |  Yes  |  Yes  |  Yes  |  Yes  |  No  |  Yes  |  Yes  |
|  China (Ningxia) Region Operated by NWCD\*  |  Yes  |  Yes  |  Yes  |  Yes  |  No  |  Yes  |  No  |

**Note**
AWS China Regions don't support using AWS Global Accelerator to accelerate the ingestion endpoint.
