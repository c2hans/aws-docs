---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-gatewayrule-matchmodelentry.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::GatewayRule MatchModelEntry
<a name="aws-properties-bedrockagentcore-gatewayrule-matchmodelentry"></a>

A model ID or pattern to match against the requested model, and the operator to use for the comparison.

## Syntax
<a name="aws-properties-bedrockagentcore-gatewayrule-matchmodelentry-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-gatewayrule-matchmodelentry-syntax.json"></a>

```
{
  "[Operator](#cfn-bedrockagentcore-gatewayrule-matchmodelentry-operator)" : {{}},
  "[Value](#cfn-bedrockagentcore-gatewayrule-matchmodelentry-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-gatewayrule-matchmodelentry-syntax.yaml"></a>

```
  [Operator](#cfn-bedrockagentcore-gatewayrule-matchmodelentry-operator): {{
    }}
  [Value](#cfn-bedrockagentcore-gatewayrule-matchmodelentry-value): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-gatewayrule-matchmodelentry-properties"></a>

`Operator`  <a name="cfn-bedrockagentcore-gatewayrule-matchmodelentry-operator"></a>
The operator to use when comparing the requested model to the value:
+ `StringEquals` – Requires an exact match.
+ `StringLike` – Supports wildcard patterns using `*` and `?`. This is the default.
*Required*: No
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-bedrockagentcore-gatewayrule-matchmodelentry-value"></a>
The model ID or pattern to match. With the `StringLike` operator, you can use `*` and `?` as wildcards, for example `anthropic.claude-*`.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-\._\*\?@:]+(/[a-zA-Z0-9\-\._\*\?@:]+)*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
