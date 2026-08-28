---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessagentcoregatewayconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessAgentCoreGatewayConfig
<a name="aws-properties-bedrockagentcore-harness-harnessagentcoregatewayconfig"></a>

Configuration for AgentCore Gateway.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessagentcoregatewayconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessagentcoregatewayconfig-syntax.json"></a>

```
{
  "[GatewayArn](#cfn-bedrockagentcore-harness-harnessagentcoregatewayconfig-gatewayarn)" : {{String}},
  "[OutboundAuth](#cfn-bedrockagentcore-harness-harnessagentcoregatewayconfig-outboundauth)" : {{HarnessGatewayOutboundAuth}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessagentcoregatewayconfig-syntax.yaml"></a>

```
  [GatewayArn](#cfn-bedrockagentcore-harness-harnessagentcoregatewayconfig-gatewayarn): {{String}}
  [OutboundAuth](#cfn-bedrockagentcore-harness-harnessagentcoregatewayconfig-outboundauth): {{
    HarnessGatewayOutboundAuth}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessagentcoregatewayconfig-properties"></a>

`GatewayArn`  <a name="cfn-bedrockagentcore-harness-harnessagentcoregatewayconfig-gatewayarn"></a>
The ARN of the desired AgentCore Gateway.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutboundAuth`  <a name="cfn-bedrockagentcore-harness-harnessagentcoregatewayconfig-outboundauth"></a>
How harness authenticates to this Gateway. Defaults to AWS\_IAM (SigV4) if omitted.
*Required*: No
*Type*: [HarnessGatewayOutboundAuth](aws-properties-bedrockagentcore-harness-harnessgatewayoutboundauth.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
