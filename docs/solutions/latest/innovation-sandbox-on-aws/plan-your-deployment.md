---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the [Regions](#supported-aws-regions), [cost](cost.md), [security](security-1.md), and other considerations prior to deploying the solution.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

Innovation Sandbox on AWS is available in the following AWS Regions. [Learn more](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html) about enabling regions.

| Region Name | Region Code |
| --- | --- |
| US East (Ohio) | us-east-2 |
| US East (N. Virginia) | us-east-1 |
| US West (N. California) | us-west-1 |
| US West (Oregon) | us-west-2 |
| Africa (Cape Town) | af-south-1 |
| Asia Pacific (Hong Kong) | ap-east-1 |
| Asia Pacific (Tokyo) | ap-northeast-1 |
| Asia Pacific (Seoul) | ap-northeast-2 |
| Asia Pacific (Osaka) | ap-northeast-3 |
| Asia Pacific (Mumbai) | ap-south-1 |
| Asia Pacific (Hyderabad) | ap-south-2 |
| Asia Pacific (Singapore) | ap-southeast-1 |
| Asia Pacific (Sydney) | ap-southeast-2 |
| Asia Pacific (Jakarta) | ap-southeast-3 |
| Asia Pacific (Melbourne) | ap-southeast-4 |
| Canada (Central) | ca-central-1 |
| Europe (Frankfurt) | eu-central-1 |
| Europe (Zurich) | eu-central-2 |
| Europe (Stockholm) | eu-north-1 |
| Europe (Milan) | eu-south-1 |
| Europe (Spain) | eu-south-2 |
| Europe (Ireland) | eu-west-1 |
| Europe (London) | eu-west-2 |
| Europe (Paris) | eu-west-3 |
| Middle East (UAE) | me-central-1 |
| Middle East (Bahrain) | me-south-1 |
| South America (São Paulo) | sa-east-1 |

Innovation Sandbox on AWS is **not** available in the following AWS Regions:

| Region Name | Region Code |
| --- | --- |
| Asia Pacific (Malaysia) | ap-southeast-5 |
| Asia Pacific (Thailand) | ap-southeast-7 |
| Canada West (Calgary) | ca-west-1 |
| China (Beijing) | cn-north-1 |
| China (Ningxia) | cn-northwest-1 |
| Israel (Tel Aviv) | il-central-1 |
| Mexico (Mexico City) | mx-central-1 |
| AWS GovCloud (US-East) | us-gov-east-1 |
| AWS GovCloud (US-West) | us-gov-west-1 |

For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

**Important**
 **CloudFront Access Logging Limitation**
As of September 2025, CloudFront access logging is automatically disabled in the following regions due to lack of support for standard logging (legacy):
Africa (Cape Town) - `af-south-1`
Asia Pacific (Hong Kong) - `ap-east-1`
Asia Pacific (Hyderabad) - `ap-south-2`
Asia Pacific (Jakarta) - `ap-southeast-3`
Asia Pacific (Melbourne) - `ap-southeast-4`
Canada West (Calgary) - `ca-west-1`
Europe (Milan) - `eu-south-1`
Europe (Spain) - `eu-south-2`
Europe (Zurich) - `eu-central-2`
Israel (Tel Aviv) - `il-central-1`
Middle East (Bahrain) - `me-south-1`
Middle East (UAE) - `me-central-1`
If you deploy the solution in one of these regions, the CloudFront distribution will function normally but will not generate access logs. If access logging is required for your use case, you can manually configure CloudFront Standard Logging V2 after deployment. For more information, refer to the [CloudFront Standard Logging V2 documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/standard-logging.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
