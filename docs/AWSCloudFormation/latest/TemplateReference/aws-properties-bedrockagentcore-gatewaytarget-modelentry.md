---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewaytarget-modelentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayTarget ModelEntry
<a name="aws-properties-bedrockagentcore-gatewaytarget-modelentry"></a>

A model entry that specifies a model supported for an inference operation.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewaytarget-modelentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewaytarget-modelentry-syntax.json"></a>

```
{
  "[Model](#cfn-bedrockagentcore-gatewaytarget-modelentry-model)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewaytarget-modelentry-syntax.yaml"></a>

```
  [Model](#cfn-bedrockagentcore-gatewaytarget-modelentry-model): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewaytarget-modelentry-properties"></a>

`Model`  <a name="cfn-bedrockagentcore-gatewaytarget-modelentry-model"></a>
The model ID or glob pattern that identifies the model (for example, `anthropic.claude-opus-*` or `openai.gpt-oss-*`).
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-\._\*\?@]+(/[a-zA-Z0-9\-\._\*\?@]+)*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
