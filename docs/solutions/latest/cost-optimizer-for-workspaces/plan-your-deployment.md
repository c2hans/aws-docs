---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the [cost](cost.md), [security](security.md), and [quota](quotas.md) considerations prior to deploying the solution.

## Supported AWS Regions
<a name="supported-regions"></a>

You must launch the solution in an AWS Region that supports AWS Lambda, Amazon WorkSpaces, and AWS Fargate services. Once deployed, the solution will monitor WorkSpaces in any supported AWS Region within the same partition. For example, a deployment in US East (N. Virginia) can monitor WorkSpaces in US West (Oregon) and other commercial regions. For AWS GovCloud, deploy the solution in AWS GovCloud (US-West) to monitor WorkSpaces in both AWS GovCloud (US-West) and AWS GovCloud (US-East). Cross-partition monitoring (for example, from a commercial region to a GovCloud region) is not supported.

For the most current availability by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

Cost Optimizer for Amazon Workspaces is supported in the following AWS Regions:

| Region name |  |
| --- | --- |
| US East (Ohio) | Asia Pacific (Seoul) |
| US East (N. Virginia) | Europe (Paris) |
| US West (Northern California) | Middle East (Bahrain) |
| US West (Oregon) | AWS GovCloud (US-West) |
| Africa (Cape Town) | Europe (Ireland) |
| Europe (London) | Europe (Stockholm) |
| Canada (Central) | Europe (Frankfurt) |
| Asia Pacific (Mumbai) | Asia Pacific (Osaka) |
| Asia Pacific (Singapore) | Asia Pacific (Sydney) |
| Asia Pacific (Tokyo) | South America (Sao Paulo) |
