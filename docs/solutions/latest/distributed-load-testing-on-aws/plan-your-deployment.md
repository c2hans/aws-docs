---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes cost, security, supported Regions, quotas, and other considerations you should review before deploying the solution.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

Distributed Load Testing on AWS is available in the following AWS Regions:

**Note**
For the most current availability of the AWS services used in this solution by Region, refer to the [AWS Regional Services List](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

| Region name | Region code |
| --- | --- |
| US East (N. Virginia) | us-east-1 |
| US East (Ohio) | us-east-2 |
| US West (N. California) | us-west-1 |
| US West (Oregon) | us-west-2 |
| Canada (Central) | ca-central-1 |
| Europe (Frankfurt) | eu-central-1 |
| Europe (Ireland) | eu-west-1 |
| Europe (London) | eu-west-2 |
| Europe (Paris) | eu-west-3 |
| Europe (Stockholm) | eu-north-1 |
| Asia Pacific (Mumbai) | ap-south-1 |
| Asia Pacific (Tokyo) | ap-northeast-1 |
| Asia Pacific (Seoul) | ap-northeast-2 |
| Asia Pacific (Singapore) | ap-southeast-1 |
| Asia Pacific (Sydney) | ap-southeast-2 |
| South America (São Paulo) | sa-east-1 |
| AWS GovCloud (US-East) | us-gov-east-1 |
| AWS GovCloud (US-West) | us-gov-west-1 |

**Note**
In AWS GovCloud (US) Regions, the default CloudFront \+ S3 web console hosting option is not available because Amazon CloudFront is not available in the AWS GovCloud (US) partition. Use the ALB \+ ECS Fargate template or the headless template, and follow the deployment steps in [Deploy in AWS GovCloud (US) Regions](deploy-govcloud.md).

### MCP Server supported AWS Regions (Optional)
<a name="mcp-server-regions"></a>

If you plan to deploy the optional MCP Server integration, you must deploy the solution in an AWS Region where AgentCore Gateway is available. The MCP Server feature is only available in the following AWS Regions:

| Region name | Region code |
| --- | --- |
| US East (N. Virginia) | us-east-1 |
| US East (Ohio) | us-east-2 |
| US West (Oregon) | us-west-2 |
| Canada (Central) | ca-central-1 |
| Europe (Frankfurt) | eu-central-1 |
| Europe (Ireland) | eu-west-1 |
| Europe (London) | eu-west-2 |
| Europe (Paris) | eu-west-3 |
| Europe (Stockholm) | eu-north-1 |
| Asia Pacific (Mumbai) | ap-south-1 |
| Asia Pacific (Tokyo) | ap-northeast-1 |
| Asia Pacific (Seoul) | ap-northeast-2 |
| Asia Pacific (Singapore) | ap-southeast-1 |
| Asia Pacific (Sydney) | ap-southeast-2 |
| South America (São Paulo) | sa-east-1 |

For the most current availability of AgentCore Gateway by Region, refer to [Amazon Bedrock AgentCore endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock_agentcore.html) in the *AWS General Reference*.

**Tip**
If you want to use the MCP Server but need to send load testing traffic from an AWS Region where AgentCore Gateway is not supported, you can deploy the main hub stack (with the MCP Server enabled) in a supported AgentCore Gateway Region and then deploy the regional stack (see [Multi-Region deployment](multi-region-deployment.md)) in the AWS Region where you want to generate test traffic. This allows you to use the MCP Server for AI-assisted analysis while still running load tests from your desired Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Distributed Load Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
