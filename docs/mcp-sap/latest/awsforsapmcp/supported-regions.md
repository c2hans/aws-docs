---
source_url: https://docs.aws.amazon.com/mcp-sap/latest/awsforsapmcp/supported-regions.html
---

# Supported AWS Regions
<a name="supported-regions"></a>

The AWS for SAP Model Context Protocol (MCP) Server runs on Amazon Bedrock AgentCore Runtime. You can deploy the MCP Server in any AWS Region where AgentCore Runtime is available and where the AWS for SAP MCP Server container image is published.

## Region availability
<a name="region-availability"></a>

The following table shows the AWS Regions where the AWS for SAP MCP Server is supported.

|  AWS Region name | Region code | Support |
| --- | --- | --- |
| US East (N. Virginia) |  `us-east-1`  | ✓ |
| US East (Ohio) |  `us-east-2`  | ✓ |
| US West (Oregon) |  `us-west-2`  | ✓ |
| Europe (Frankfurt) |  `eu-central-1`  | ✓ |
| Europe (Ireland) |  `eu-west-1`  | ✓ |
| Europe (London) |  `eu-west-2`  | ✓ |
| Europe (Paris) |  `eu-west-3`  | ✓ |
| Europe (Stockholm) |  `eu-north-1`  | ✓ |
| Asia Pacific (Mumbai) |  `ap-south-1`  | ✓ |
| Asia Pacific (Singapore) |  `ap-southeast-1`  | ✓ |
| Asia Pacific (Sydney) |  `ap-southeast-2`  | ✓ |
| Asia Pacific (Tokyo) |  `ap-northeast-1`  | ✓ |
| Asia Pacific (Seoul) |  `ap-northeast-2`  | ✓ |
| Canada (Central) |  `ca-central-1`  | ✓ |

**Note**
The AWS for SAP MCP Server requires Amazon Bedrock AgentCore Runtime and Amazon Bedrock AgentCore Identity. Verify that both services are available in your target Region before deployment. For the latest AgentCore region availability, see [Supported AWS Regions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html) in the Amazon Bedrock AgentCore documentation.

## Region considerations
<a name="region-considerations"></a>

When you choose a Region for your AWS for SAP MCP Server deployment, consider the following:
+  **Proximity to your SAP system** — Deploy the MCP Server in the same Region (or closest Region) to your SAP system to minimize network latency for OData (Open Data Protocol) requests.
+  **Data residency requirements** — Choose a Region that meets your organization’s data residency and compliance requirements for SAP data processing.
+  **Dependent AWS services** — The MCP Server uses AWS Secrets Manager, Amazon S3, and Amazon Bedrock AgentCore Identity. These services must be available in your chosen Region.
+  **Network connectivity** — Ensure that the VPC and subnets in your chosen Region have network connectivity to your SAP system, whether through AWS Direct Connect, VPN, or internal routing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MCP Servers for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mcp-sap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
