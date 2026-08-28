---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/bedrockagentcore-runtime-private-network-required.html
---

# bedrockagentcore-runtime-private-network-required
<a name="bedrockagentcore-runtime-private-network-required"></a>

Checks if an Amazon Bedrock AgentCore runtime is configured with public network access. The rule is NON\_COMPLIANT if the runtime has NetworkMode set to PUBLIC.

**Identifier:** BEDROCKAGENTCORE\_RUNTIME\_PRIVATE\_NETWORK\_REQUIRED

**Resource Types:** AWS::BedrockAgentCore::Runtime

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d281c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
