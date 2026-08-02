---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the Region, [cost](cost.md), [security](aws-well-architected-design-considerations.md#security), and other considerations prior to deploying the solution.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

This solution uses the Amazon Cognito service, which is not currently available in all AWS Regions. For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

Workload Discovery on AWS is available in the following AWS Regions:

| Region Name |  |
| --- | --- |
| US East (N. Virginia) | Canada (Central) |
| US East (Ohio) | Europe (London) |
| US West (Oregon) | Europe (Frankfurt) |
| Asia Pacific (Mumbai) | Europe (Ireland) |
| Asia Pacific (Seoul) | Europe (Paris) |
| Asia Pacific (Singapore) | Europe (Stockholm) |
| Asia Pacific (Sydney) | South America (São Paulo) |
| Asia Pacific (Tokyo) |  |

Workload Discovery on AWS is not available in the following AWS Regions:

| Region Name | Unavailable Service |
| --- | --- |
| AWS GovCloud (US-East) | AWS AppSync |
| AWS GovCloud (US-West) | AWS AppSync |
| China (Beijing) | Amazon Cognito |
| China (Ningxia) | Amazon Cognito |
