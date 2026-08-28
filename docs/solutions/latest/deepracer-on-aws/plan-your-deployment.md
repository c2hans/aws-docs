---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section provides an overview of the cost, security, service quotas, and other key factors to consider prior to deploying the solution in your AWS account.

 **Topics**
+  [Prerequisites](prerequisites.md)
+  [Cost](cost.md)
+  [Security](security-1.md)
+  [Service quotas](quotas.md)

<a name="supported-aws-regions"></a> **Supported AWS regions**

DeepRacer on AWS is available in the following AWS Regions.

| Region Name | Region Code |
| --- | --- |
| US East (N. Virginia) | us-east-1 |
| US East (Ohio) | us-east-2 |
| US West (Oregon) | us-west-2 |
| Africa (Cape Town) | af-south-1 |
| Asia Pacific (Hong Kong) | ap-east-1 |
| Asia Pacific (Mumbai) | ap-south-1 |
| Asia Pacific (Seoul) | ap-northeast-2 |
| Asia Pacific (Singapore) | ap-southeast-1 |
| Asia Pacific (Sydney) | ap-southeast-2 |
| Asia Pacific (Tokyo) | ap-northeast-1 |
| Canada (Central) | ca-central-1 |
| Europe (Frankfurt) | eu-central-1 |
| Europe (Ireland) | eu-west-1 |
| Europe (London) | eu-west-2 |
| Europe (Paris) | eu-west-3 |
| Europe (Spain) | eu-south-2 |
| Middle East (Bahrain) | me-south-1 |
| South America (São Paulo) | sa-east-1 |

For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

**Important**
 **SES Region Availability Limitation**
If you choose to deploy the solution using Amazon SES as the email delivery method for authentication emails, the following regions are not supported due to Amazon SES not being available:
Europe (Spain) - `eu-south-2`
Asia Pacific (Hong Kong) - `ap-east-1`

**Important**
 **CloudFront Access Logging Limitation**
CloudFront access logging is automatically disabled in the following regions due to lack of support for standard logging (legacy):
Africa (Cape Town) - `af-south-1`
Asia Pacific (Hong Kong) - `ap-east-1`
Europe (Spain) - `eu-south-2`
Middle East (Bahrain) - `me-south-1`
If you deploy the solution in one of these regions, the CloudFront distribution will function normally but will not generate access logs. If access logging is required for your use case, you can manually configure CloudFront Standard Logging V2 after deployment. For more information, refer to the [CloudFront Standard Logging V2 documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/standard-logging.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
