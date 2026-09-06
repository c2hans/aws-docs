---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the [cost](cost.md), [security](security-1.md), [Region](#supported-aws-regions), and [quota](quotas.md) considerations for planning your deployment.

**Important**
This solution leverages Amazon Bedrock as the primary service for accessing AI-generated models. You must first request access to models before they are available for use within the solution. For details, refer to [Model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in the *Amazon Bedrock User Guide*.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

**Important**
This solution optionally uses the Amazon Bedrock and Amazon Kendra services, which are not currently available in all AWS Regions. You must launch this solution in an AWS Region where these services are available. For the most current availability of AWS services by Region, see the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

Generative AI Application Builder on AWS is supported in the following AWS Regions:

| Region name |  |
| --- | --- |
| US East (Ohio) | Canada (Central) |
| US East (N. Virginia) | Europe (Frankfurt) |
| US West (Northern California) | Europe (Ireland) |
| US West (Oregon) | Europe (London) |
| Asia Pacific (Mumbai) | Europe (Milan) |
| Asia Pacific (Seoul) | Europe (Paris) |
| Asia Pacific (Singapore) | Europe (Stockholm) |
| Asia Pacific (Sydney) | Middle East (Bahrain) |
| Asia Pacific (Tokyo) | South America (São Paulo) |

**Note**
If using a foundation model accessed outside of AWS in your deployments, check with the model provider which Regions their APIs are available in. If their APIs are only available in certain Regions, you might experience instability in the form of high latency or even time outs. It’s also important to check with your organization’s legal and compliance teams to evaluate the considerations of data crossing regional boundaries.
