---
source_url: https://docs.aws.amazon.com/solutions/latest/live-streaming-on-aws-with-amazon-s3/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the [cost](cost.md), [security](security.md), [Regions](#supported-aws-regions), and other considerations prior to deploying the solution.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

This solution uses the MediaLive service, which is not currently available in all AWS Regions. For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

To use an AWS Elemental Link device as an input, you must launch this solution in the AWS Region where the device is configured.

Live Streaming on AWS with Amazon S3 is available in the following AWS Regions:

| Region name |  |
| --- | --- |
| US East (Ohio) | Canada (Central) |
| US East (N. Virginia) | Europe (Frankfurt) |
| US West (Oregon) | Europe (Ireland) |
| Asia Pacific (Mumbai) | Europe (London) |
| Asia Pacific (Seoul) | Europe (Paris) |
| Asia Pacific (Singapore) | Europe (Stockholm) |
| Asia Pacific (Sydney) | South America (Sao Paulo) |
| Asia Pacific (Tokyo) |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Live Streaming on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
