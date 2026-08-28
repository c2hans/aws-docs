---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the cost, network security, supported AWS Regions, quotas, and other considerations prior to deploying the solution.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

**Important**
Enabling optional features in the solution may reduce the list of regions supported for deployment. In other words, the list below only applies to the core components of the solution. For example, if you choose to enable the Web UI, you will not be able to deploy the solution in GovCloud regions since [CloudFront is not supported in GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/setting-up-cloudfront.html).

| Region name | Region code |
| --- | --- |
| US East (Ohio) | us-east-2 |
| US East (N. Virginia) | us-east-1 |
| US West (Northern California) | us-west-1 |
| US West (Oregon) | us-west-2 |
| Africa (Cape Town) | af-south-1 |
| Asia Pacific (Hong Kong) | ap-east-1 |
| Asia Pacific (Hyderabad) | ap-south-2 |
| Asia Pacific (Jakarta) | ap-southeast-3 |
| Asia Pacific (Melbourne) | ap-southeast-4 |
| Asia Pacific (Mumbai) | ap-south-1 |
| Asia Pacific (Osaka) | ap-northeast-3 |
| Asia Pacific (Seoul) | ap-northeast-2 |
| Asia Pacific (Singapore) | ap-southeast-1 |
| Asia Pacific (Sydney) | ap-southeast-2 |
| Asia Pacific (Tokyo) | ap-northeast-1 |
| Canada (Central) | ca-central-1 |
| Europe (Frankfurt) | eu-central-1 |
| Europe (Ireland) | eu-west-1 |
| Europe (London) | eu-west-2 |
| Europe (Milan) | eu-south-1 |
| Europe (Paris) | eu-west-3 |
| Europe (Spain) | eu-south-2 |
| Europe (Stockholm) | eu-north-1 |
| Europe (Zurich) | eu-central-2 |
| Middle East (Bahrain) | me-south-1 |
| Middle East (UAE) | me-central-1 |
| South America (Sao Paulo) | sa-east-1 |
| AWS GovCloud (US-East) | us-gov-east-1 |
| AWS GovCloud (US-West) | us-gov-west-1 |
| China (Beijing) | cn-north-1 |
| China (Ningxia) | cn-northwest-1 |
| Israel (Tel Aviv) | il-central-1 |
| Canada West (Calgary) | ca-west-1 |
| Mexico (Mexico City) | mx-central-1 |
| Asia Pacific (Thailand) | ap-southeast-7 |
| Asia Pacific (Malaysia) | ap-southeast-5 |
| Asia Pacific (Taipei) | ap-east-2 |
| Asia Pacific (New Zealand) | ap-southeast-6 |

**Note**
Any new AWS regions not listed may be supported via local deployment but not one-click deployment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Security Response on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
