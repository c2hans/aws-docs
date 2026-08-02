---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the [cost](cost.md), [security](security.md), [Quotas](quotas.md), and other considerations prior to deploying the solution.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

Depending on the template input parameters values you define, this solution requires different resources. These resources (listed in the following table) might not be available in all AWS Regions. Therefore, you must launch this solution in an AWS Region where these services are available. For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

|  | AWS WAF Web ACL | AWS Glue | Amazon Athena | Amazon Kinesis Data Firehose |
| --- | --- | --- | --- | --- |
|  **Endpoint type**  |  |  |  |  |
| CloudFront | ✓ |  |  |  |
| Application Load Balancer (ALB) | ✓ |  |  |  |
|  **Activate HTTP Flood Protection**  |  |  |  |  |
| yes - AWS Lambda log parser |  |  |  | ✓ |
| yes - Amazon Athena log parser |  | ✓ | ✓ | ✓ |
|  **Activate Scanner & Probe Protection**  |  |  |  |  |
| yes - Amazon Athena log parser |  | ✓ | ✓ |  |

**Note**
If you choose `CloudFront` as your **Endpoint**, you must deploy the solution in the US East (N. Virginia) Region (`us-east-1`).
