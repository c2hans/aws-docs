---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/supported-aws-regions.html
---

# Supported AWS Regions
<a name="supported-aws-regions"></a>

This solution uses Amazon Cognito and Amazon QuickSight, which are currently available in specific AWS Regions only. Therefore, you must launch this solution in a Region where these services are available. For the most current service availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

**Note**
Data transfer during the migration process is not affected by Regional deployments.

Cloud Migration Factory on AWS is available in the following AWS Regions:

| Region names |  |
| --- | --- |
| US East (Ohio) | Canada (Central) |
| US East (N. Virginia) | \*Canada West (Calgary) |
| US West (N. California) | Europe (Frankfurt) |
| US West (Oregon) | Europe (Ireland) |
| \*Africa (Cape Town) | Europe (London) |
| \*Asia Pacific (Hong Kong) | \*Europe (Milan) |
| \*Asia Pacific (Hyderabad) | \*Europe (Spain) |
| \*Asia Pacific (Jakarta) | Europe (Paris) |
| \*Asia Pacific (Melbourne) | Europe (Stockholm) |
| Asia Pacific (Mumbai) | \*Europe (Zurich) |
| Asia Pacific (Osaka) | \*Israel (Tel Aviv) |
| Asia Pacific (Seoul) | \*Middle East (Bahrain) |
| Asia Pacific (Singapore) | \*Middle East (UAE) |
| Asia Pacific (Sydney) | South America (São Paulo) |
| Asia Pacific (Tokyo) |  |

**Important**
\*Only available for private deployment type due to Amazon CloudFront access logging, see [Configuring and using standard logs (access logs)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) in the *Amazon CloudFront Developer Guide* for latest details.

Cloud Migration Factory on AWS is not available in the following AWS Regions:

| Region name | Unavailable service(s) or service option |
| --- | --- |
| AWS GovCloud (US-East) | Amazon Cognito |
| AWS GovCloud (US-West) | Amazon Cognito |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
