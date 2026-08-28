---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/bedrockagentcore-gateway-authorizer-enabled.html
---

# bedrockagentcore-gateway-authorizer-enabled
<a name="bedrockagentcore-gateway-authorizer-enabled"></a>

Checks whether an Amazon Bedrock AgentCore Gateway requires authentication for inbound requests. The rule is NON\_COMPLIANT if the gateway has AuthorizerType set to NONE.

**Identifier:** BEDROCKAGENTCORE\_GATEWAY\_AUTHORIZER\_ENABLED

**Resource Types:** AWS::BedrockAgentCore::Gateway

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d279c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
