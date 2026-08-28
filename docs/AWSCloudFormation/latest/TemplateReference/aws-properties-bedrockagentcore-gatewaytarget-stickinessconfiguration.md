---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-stickinessconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget StickinessConfiguration
<a name="aws-properties-bedrockagentcore-gatewaytarget-stickinessconfiguration"></a>

The configuration for session-sticky routing to a target. Session stickiness routes requests that share a session identifier to the same target.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-stickinessconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-stickinessconfiguration-syntax.json"></a>

```
{
  "[Identifier](#cfn-bedrockagentcore-gatewaytarget-stickinessconfiguration-identifier)" : {{String}},
  "[Timeout](#cfn-bedrockagentcore-gatewaytarget-stickinessconfiguration-timeout)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-stickinessconfiguration-syntax.yaml"></a>

```
  [Identifier](#cfn-bedrockagentcore-gatewaytarget-stickinessconfiguration-identifier): {{String}}
  [Timeout](#cfn-bedrockagentcore-gatewaytarget-stickinessconfiguration-timeout): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-stickinessconfiguration-properties"></a>

`Identifier`  <a name="cfn-bedrockagentcore-gatewaytarget-stickinessconfiguration-identifier"></a>
The expression that identifies where to extract the session identifier from the request (for example, `$context.header.x-session-id`).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timeout`  <a name="cfn-bedrockagentcore-gatewaytarget-stickinessconfiguration-timeout"></a>
The session stickiness timeout, in seconds. After this duration of inactivity, the session affinity expires. Valid values range from 1 to 86400.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
