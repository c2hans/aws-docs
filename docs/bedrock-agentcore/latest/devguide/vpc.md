---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc.html
---

# Protecting your data using VPC and AWS PrivateLink
<a name="vpc"></a>

You can use Amazon Virtual Private Cloud (Amazon VPC) and AWS PrivateLink to create private connections between your VPC and Amazon Bedrock AgentCore.

**Topics**
+ [Use interface VPC endpoints (AWS PrivateLink) to create a private connection between your VPC and your Amazon Bedrock AgentCore resources](vpc-interface-endpoints.md)
+ [Configure Amazon Bedrock AgentCore Gateway VPC Egress for Gateway Targets](gateway-vpc-egress.md)
+ [Connect to private resources in your VPC using VPC Lattice](vpc-egress-private-endpoints.md)
+ [Configure Amazon Bedrock AgentCore Runtime and tools for VPC](agentcore-vpc.md)
+ [Use IAM condition keys with AgentCore VPC settings](security-vpc-condition.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
